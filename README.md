# Rapid X AI - Premium Voice Assistant 🎙️

A high-performance, real-time AI voice assistant powered by **LiveKit**, **Groq**, and **Saravam AI**.

## 🚀 Features
- **Web UI**: A stunning, modern web interface for direct browser interaction.
- **Ultra-Low Latency**: Powered by Groq's Llama 3.3 for lightning-fast responses.
- **Multilingual Support**: Uses Saravam AI for high-quality Indian-accented voices and multi-lingual capabilities.
- **Real-time Visualization**: Beautiful animated visualizers for voice activity.

## 🛠️ Tech Stack
- **Frontend**: Next.js 15, Tailwind CSS 4, Framer Motion, Lucide Icons.
- **Backend**: LiveKit Agents (Python), LiveKit Server SDK (Node.js).
- **AI Models**:
  - **LLM**: Groq (Llama 3.3 70B)
  - **TTS**: Saravam AI (Anushka/Bulbul)
  - **STT**: Deepgram (Nova-2)

## 📦 Installation

### 1. Agent (Python)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the agent
python agent.py dev
```

### 2. Dashboard (Next.js)
```bash
cd dashboard

# Install dependencies
npm install

# Run the development server
npm run dev
```

## ⚙️ Configuration
Create a `.env` file in the root directory with the following:
```env
LIVEKIT_URL=wss://ai-ol2pplrk.livekit.cloud
LIVEKIT_API_KEY=APIcQJUjL2RsZ76
LIVEKIT_API_SECRET=cz4KAupg36SJb0gI5pEmC4wwUe53gum8neQw06CLMLq

SARVAM_API_KEY=sk_ep68lfyw...
DEEPGRAM_API_KEY=283fe15e...
GROQ_API_KEY=gsk_qzAX8lId...
```

## 🤝 Socials
- **Instagram**: [@ai.w.raj](https://instagram.com/ai.w.raj)
- **X**: [@topR9595](https://x.com/topR9595)
- **YouTube**: [Shreyas Raj](https://youtube.com/@ShreyasRaj)
