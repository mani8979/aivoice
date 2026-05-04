import VoiceAssistant from '@/components/VoiceAssistant';
import { Twitter, Youtube, Instagram } from 'lucide-react';

export default function Home() {
  return (
    <main className="min-h-screen bg-[#050505] text-white flex flex-col items-center justify-between p-8 relative overflow-hidden selection:bg-purple-500/30">

      {/* Ambient Background Lights */}
      <div className="fixed top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
        <div className="absolute top-[-10vh] left-[10vw] w-[70vh] h-[70vh] bg-blue-600/10 rounded-full blur-[128px] animate-pulse"></div>
        <div className="absolute bottom-[-10vh] right-[10vw] w-[80vh] h-[80vh] bg-purple-600/10 rounded-full blur-[128px] animate-pulse delay-1000"></div>
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[100vh] h-[100vh] bg-indigo-600/5 rounded-full blur-[128px]"></div>
      </div>

      {/* Grid Pattern Overlay */}
      <div className="fixed inset-0 bg-[url('/grid.svg')] bg-center [mask-image:radial-gradient(ellipse_at_center,white,transparent)] opacity-20 pointer-events-none"></div>

      <div className="z-10 flex flex-col items-center gap-12 w-full max-w-7xl pt-12">
        <header className="text-center space-y-6 animate-in fade-in slide-in-from-top-8 duration-1000">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 text-xs font-semibold text-purple-300 mb-2 backdrop-blur-md">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
            </span>
            Sarvam Telugu & Groq Powered
          </div>

          <h1 className="text-7xl md:text-8xl font-black tracking-tighter">
            <span className="text-white">Rapid X</span>
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500"> Estates</span>
          </h1>
          <p className="text-xl md:text-2xl text-gray-400 max-w-3xl mx-auto font-medium leading-relaxed">
            Voice assistance for land buyers, plot enquiries, documents, and site visits.
            <span className="block text-gray-600 text-lg mt-2 font-normal">Speak in Telugu, English, or Hindi.</span>
          </p>
        </header>

        <div className="w-full flex justify-center animate-in fade-in zoom-in-95 duration-1000 delay-300">
          <VoiceAssistant />
        </div>
      </div>

      <footer className="z-10 w-full max-w-7xl flex flex-col md:flex-row items-center justify-between gap-8 pt-12 pb-4 border-t border-white/5 mt-20">
        <div className="flex flex-col gap-2">
          <h4 className="text-lg font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500">Rapid X Estates</h4>
          <p className="text-sm text-gray-500">Real estate voice assistance for land and plot enquiries.</p>
        </div>

        <div className="flex gap-6 items-center">
          <SocialLink href="https://instagram.com/ai.w.raj" icon={<Instagram size={20} />} label="Instagram" />
          <SocialLink href="https://x.com/topR9595" icon={<Twitter size={20} />} label="Twitter" />
          <SocialLink href="https://youtube.com/@ShreyasRaj" icon={<Youtube size={20} />} label="YouTube" />
        </div>
      </footer>
    </main>
  );
}

function SocialLink({ href, icon, label }: { href: string; icon: React.ReactNode; label: string }) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className="text-gray-500 hover:text-white transition-all duration-300 hover:scale-110 flex items-center gap-2 group"
      aria-label={label}
    >
      {icon}
      <span className="text-xs font-medium opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">{label}</span>
    </a>
  );
}
