import React, { useState } from "react";
import QuestionCard from "../components/QuestionCard";
import QuestionForm from "../components/QuestionForm";

const DESCR = {
  1: "Normaliza o texto e verifica a regra do enunciado (ex.: 'BeA').",
  2: "Calcula/valida a série numérica a partir do valor x.",
  3: "Calcula mínimo de turnos e combinações com base no nº de casas.",
  4: "Valida a data e retorna proporcionalidades definidas no desafio.",
};

export default function FastAPI() {
  const [selected, setSelected] = useState(null);

  return (
    <div className="p-6 text-gray-200">
      <h1 className="text-2xl font-bold mb-6">Módulo FastAPI — Questões</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {[1, 2, 3, 4].map((q) => (
          <QuestionCard
            key={q}
            numero={q}
            description={DESCR[q]}
            onClick={() => setSelected(q)}
            isActive={selected === q}
          />
        ))}
      </div>

      {selected && (
        <div className="mt-8">
          <QuestionForm numero={selected} />
        </div>
      )}
    </div>
  );
}
