import { AccessToken, AgentDispatchClient } from 'livekit-server-sdk';
import { NextRequest, NextResponse } from 'next/server';

const AGENT_NAME = process.env.LIVEKIT_AGENT_NAME || 'outbound-caller';

function toLiveKitApiUrl(url: string) {
  return url.replace(/^wss:\/\//, 'https://').replace(/^ws:\/\//, 'http://');
}

export async function GET(req: NextRequest) {
  const room = req.nextUrl.searchParams.get('room');
  const identity =
    req.nextUrl.searchParams.get('identity') ||
    `user_${Math.floor(Math.random() * 10000)}`;

  if (!room) {
    return NextResponse.json({ error: 'Missing room parameter' }, { status: 400 });
  }

  const apiKey = process.env.LIVEKIT_API_KEY;
  const apiSecret = process.env.LIVEKIT_API_SECRET;
  const wsUrl = process.env.LIVEKIT_URL;

  if (!apiKey || !apiSecret || !wsUrl) {
    return NextResponse.json({ error: 'Server misconfigured' }, { status: 500 });
  }

  // ✅ Generate the token immediately — don't wait for dispatch
  const at = new AccessToken(apiKey, apiSecret, { identity });
  at.addGrant({
    roomJoin: true,
    room,
    canPublish: true,
    canSubscribe: true,
  });
  const token = await at.toJwt();

  // 🚀 Dispatch agent in background — fire and forget (does NOT block the response)
  const dispatchClient = new AgentDispatchClient(toLiveKitApiUrl(wsUrl), apiKey, apiSecret);
  dispatchClient
    .createDispatch(room, AGENT_NAME)
    .then(() => console.log(`[token] Agent "${AGENT_NAME}" dispatched to room "${room}"`))
    .catch((err) => console.error(`[token] Dispatch warning (agent may already be registered):`, err));

  // ✅ Return token immediately — user connects to room while agent starts up
  return NextResponse.json({ token, url: wsUrl });
}
