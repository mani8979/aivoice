import { AccessToken, AgentDispatchClient } from 'livekit-server-sdk';
import { NextRequest, NextResponse } from 'next/server';

const AGENT_NAME = process.env.LIVEKIT_AGENT_NAME || 'outbound-caller';

function toLiveKitApiUrl(url: string) {
  return url.replace(/^wss:\/\//, 'https://').replace(/^ws:\/\//, 'http://');
}

export async function GET(req: NextRequest) {
  const room = req.nextUrl.searchParams.get('room');
  const identity = req.nextUrl.searchParams.get('identity') || `user_${Math.floor(Math.random() * 10000)}`;

  if (!room) {
    return NextResponse.json({ error: 'Missing room parameter' }, { status: 400 });
  }

  const apiKey = process.env.LIVEKIT_API_KEY;
  const apiSecret = process.env.LIVEKIT_API_SECRET;
  const wsUrl = process.env.LIVEKIT_URL;

  if (!apiKey || !apiSecret || !wsUrl) {
    return NextResponse.json({ error: 'Server misconfigured' }, { status: 500 });
  }

  try {
    const dispatchClient = new AgentDispatchClient(toLiveKitApiUrl(wsUrl), apiKey, apiSecret);
    await dispatchClient.createDispatch(room, AGENT_NAME);
  } catch (error) {
    console.error('Failed to dispatch LiveKit agent:', error);
    return NextResponse.json(
      {
        error: `Could not dispatch agent "${AGENT_NAME}". Make sure the Python agent is running with: python agent.py dev`,
      },
      { status: 503 },
    );
  }

  const at = new AccessToken(apiKey, apiSecret, {
    identity: identity,
  });

  at.addGrant({
    roomJoin: true,
    room: room,
    canPublish: true,
    canSubscribe: true,
  });

  return NextResponse.json({
    token: await at.toJwt(),
    url: wsUrl,
  });
}
