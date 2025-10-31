import { PlayCircle } from "lucide-react";

export default function QuestionCard({ numero, onClick, isActive, description }) {
  return (
    <button
      onClick={onClick}
      className={`text-left p-4 rounded-2xl border transition ${
        isActive ? "border-accent bg-secondary/60" : "border-border hover:bg-secondary/40"
      }`}
    >
      <h3 className="text-lg font-semibold mb-2 flex items-center gap-2">
        <PlayCircle size={18} className="text-accent" /> Questão {numero}
      </h3>
      <p className="text-gray-300 text-sm">{description}</p>
    </button>
  );
}
