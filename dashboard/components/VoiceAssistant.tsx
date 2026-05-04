'use client';

import {
  LiveKitRoom,
  useVoiceAssistant,
  BarVisualizer,
  RoomAudioRenderer,
  VoiceAssistantControlBar,
  DisconnectButton,
} from '@livekit/components-react';
import { useCallback, useState } from 'react';
import { motion } from 'framer-motion';
import { Mic, PhoneOff, Zap, ShieldCheck, Globe } from 'lucide-react';
import { cn } from '@/lib/utils';

export default function VoiceAssistant() {
  const [token, setToken] = useState<string | null>(null);
  const [url, setUrl] = useState<string | null>(null);
  const [isConnecting, setIsConnecting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const startCall = useCallback(async () => {
    setIsConnecting(true);
    setError(null);
    try {
      const roomName = `room_${Math.random().toString(36).substring(7)}`;
      const identity = `user_${crypto.randomUUID()}`;
      const response = await fetch(`/api/token?room=${roomName}&identity=${identity}`);
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Failed to start the voice session');
      }

      setToken(data.token);
      setUrl(data.url);
    } catch (error) {
      console.error('Failed to get token:', error);
      setError(error instanceof Error ? error.message : 'Failed to start the voice session');
    } finally {
      setIsConnecting(false);
    }
  }, []);

  if (!token || !url) {
    return (
      <div className="w-full max-w-md mx-auto">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white/5 border border-white/10 rounded-3xl p-8 backdrop-blur-xl shadow-2xl relative overflow-hidden group"
        >
          <div className="absolute inset-0 bg-gradient-to-br from-blue-600/10 via-purple-600/10 to-pink-600/10 opacity-50 group-hover:opacity-100 transition-opacity duration-500" />
          
          <div className="relative z-10 space-y-6">
            <div className="flex justify-center">
              <div className="w-20 h-20 rounded-2xl bg-gradient-to-tr from-blue-500 to-purple-600 flex items-center justify-center shadow-lg shadow-blue-500/20">
                <Mic className="w-10 h-10 text-white" />
              </div>
            </div>
            
            <div className="text-center space-y-2">
              <h2 className="text-2xl font-bold text-white">Rapid X Estates</h2>
              <p className="text-gray-400 text-sm">Ask about lands, plots, pricing, documents, and site visits in Telugu, English, or Hindi.</p>
            </div>

            <div className="grid grid-cols-3 gap-4 py-4">
              <div className="flex flex-col items-center gap-2">
                <Zap className="w-5 h-5 text-yellow-400" />
                <span className="text-[10px] uppercase tracking-wider text-gray-500">Groq LLM</span>
              </div>
              <div className="flex flex-col items-center gap-2">
                <Globe className="w-5 h-5 text-blue-400" />
                <span className="text-[10px] uppercase tracking-wider text-gray-500">Telugu TTS</span>
              </div>
              <div className="flex flex-col items-center gap-2">
                <ShieldCheck className="w-5 h-5 text-green-400" />
                <span className="text-[10px] uppercase tracking-wider text-gray-500">LiveKit</span>
              </div>
            </div>

            <button
              onClick={startCall}
              disabled={isConnecting}
              className={cn(
                "w-full py-4 rounded-xl font-semibold text-white transition-all duration-300 flex items-center justify-center gap-2 shadow-lg shadow-purple-600/20",
                isConnecting 
                  ? "bg-purple-600/50 cursor-not-allowed" 
                  : "bg-gradient-to-r from-blue-600 to-purple-600 hover:scale-[1.02] active:scale-[0.98]"
              )}
            >
              {isConnecting ? (
                <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
              ) : (
                <>
                  <Mic className="w-5 h-5" />
                  Start Property Call
                </>
              )}
            </button>

            {error && (
              <p className="text-sm text-red-300 text-center leading-relaxed">
                {error}
              </p>
            )}
          </div>
        </motion.div>
      </div>
    );
  }

  return (
    <LiveKitRoom
      token={token}
      serverUrl={url}
      connect={true}
      audio={true}
      video={false}
      onDisconnected={() => {
        setToken(null);
        setUrl(null);
      }}
      className="flex flex-col items-center justify-center w-full max-w-4xl mx-auto"
    >
      <div className="w-full bg-white/5 border border-white/10 rounded-3xl p-12 backdrop-blur-xl shadow-2xl relative overflow-hidden flex flex-col items-center gap-8">
        <div className="absolute inset-0 bg-gradient-to-br from-blue-600/5 via-purple-600/5 to-pink-600/5" />
        
        <AgentStatusDisplay />
        
        <div className="relative z-10 w-full h-48 flex items-center justify-center">
          <BarVisualizer className="w-full max-w-lg h-32 text-purple-500" />
        </div>

        <div className="relative z-10 flex flex-col items-center gap-6">
          <div className="p-4 rounded-full bg-white/5 border border-white/10 flex gap-4">
             <VoiceAssistantControlBar controls={{ leave: false }} />
             <DisconnectButton className="lk-button !bg-red-600/20 !text-red-400 !border-red-600/30 hover:!bg-red-600/30 transition-all px-6 py-2 rounded-xl flex items-center gap-2">
                <PhoneOff className="w-4 h-4" />
                End Call
             </DisconnectButton>
          </div>
        </div>
      </div>
      <RoomAudioRenderer />
    </LiveKitRoom>
  );
}

function AgentStatusDisplay() {
  const { state } = useVoiceAssistant();
  
  return (
    <div className="relative z-10 text-center space-y-4">
      <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-purple-500/10 border border-purple-500/20">
        <div className={cn(
          "w-2 h-2 rounded-full animate-pulse",
          state === 'listening' ? "bg-blue-400" : 
          state === 'speaking' ? "bg-green-400" : "bg-purple-400"
        )} />
        <span className="text-xs font-bold uppercase tracking-widest text-purple-300">
          {state === 'idle' ? 'Estate Assistant Ready' : state}
        </span>
      </div>
      
      <h3 className="text-3xl font-bold text-white tracking-tight">
        {state === 'listening' && "I'm Listening..."}
        {state === 'speaking' && "AI Speaking"}
        {state === 'thinking' && "Thinking..."}
        {state === 'idle' && "Ask about land or plots..."}
      </h3>
    </div>
  );
}
