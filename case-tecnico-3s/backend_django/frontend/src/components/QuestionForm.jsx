import { useMemo, useState } from "react";

const BASE = import.meta.env.VITE_API_URL || "http://localhost:8001/api";


const QUESTIONS = {
  1: {
    title: "Questão 1 – Normalização de texto (BeA)",
    help: "Informe um texto qualquer. O serviço normaliza e verifica se a palavra começa com 'B' e termina com 'A'.",
    inputs: [
      { name: "texto", label: "Texto", type: "text", placeholder: "Ex.: bea / bEa / BEA", required: true },
    ],
    // fallback: envia também 's' para cobrir variação de nome de parâmetro
    extraParams: (vals) => ({ s: vals.texto }),
  },
  2: {
    title: "Questão 2 – Série numérica",
    help: "Informe um número inteiro x. O serviço calcula/valida o valor que ocupa a posição informada na série sequencial: (11, 18, 25, 32, 39... ).",
    inputs: [
      { name: "x", label: "Valor de x", type: "number", min: 0, step: 1, placeholder: "Ex.: 5", required: true },
    ],
  },
  3: {
    title: "Questão 3 – Probabilidade & combinações",
    help: "Informe o número de casas (inteiro ≥ 3). Calcula mínimo de turnos e combinações possíveis.",
    inputs: [
      { name: "casas", label: "Nº de casas", type: "number", min: 3, step: 1, placeholder: "Ex.: 5", required: true },
    ],
  },
  4: {
    title: "Questão 4 – Cálculo de Férias e 13º",
    help: "Informe as datas e o salário base para calcular o valor proporcional de férias e décimo terceiro.",
    inputs: [
      { name: "data_admissao", label: "Data de admissão", type: "date", required: true },
      { name: "data_demissao", label: "Data de demissão", type: "date", required: true },
      { name: "salario_base", label: "Salário base (R$)", type: "number", step: "0.01", required: true },
    ],
  },

};

export default function QuestionForm({ numero }) {
  const cfg = useMemo(() => QUESTIONS[numero], [numero]);
  const [values, setValues] = useState({});
  const [loading, setLoading] = useState(false);
  const [resp, setResp] = useState(null);
  const [erro, setErro] = useState("");

  if (!cfg) return null;

  const onChange = (name, val) => setValues((v) => ({ ...v, [name]: val }));

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErro("");
    setResp(null);

    try {
      // monta query params com os campos configurados
      const params = new URLSearchParams();
      for (const field of cfg.inputs) {
        const val = values[field.name];
        if (field.required && (val === undefined || val === "")) {
          setErro(`Preencha o campo obrigatório: ${field.label}`);
          return;
        }
        if (val !== undefined && val !== "") params.append(field.name, val);
      }
      // envia também parâmetros alternativos (cobrir variações de nome no backend)
      if (cfg.extraParams) {
        const extras = cfg.extraParams(values) || {};
        Object.entries(extras).forEach(([k, v]) => {
          if (v !== undefined && v !== "") params.append(k, v);
        });
      }

      setLoading(true);
      const res = await fetch(`${BASE}/questao/${numero}/?${params.toString()}`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setResp(data);
    } catch (err) {
      console.error(err);
      setErro("Falha ao chamar API");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mt-6 p-5 rounded-2xl border border-border bg-secondary/40">
      <h2 className="text-xl font-semibold mb-2">{cfg.title}</h2>
      <p className="text-sm text-gray-300 mb-4">{cfg.help}</p>

      <form onSubmit={handleSubmit} className="space-y-4">
        {cfg.inputs.map((f) => (
          <div key={f.name} className="flex flex-col gap-1">
            <label className="text-sm">{f.label}</label>
            <input
            className="bg-background border border-border rounded-lg px-3 py-2 text-gray-900 placeholder-gray-500 outline-none focus:border-accent"
            type={f.type}
            min={f.min}
            step={f.step}
            placeholder={f.placeholder}
            required={f.required}
            onChange={(e) => onChange(f.name, e.target.value)}
            />
          </div>
        ))}

        <button
          type="submit"
          disabled={loading}
          className="px-4 py-2 rounded-lg bg-accent text-black font-semibold hover:opacity-90 disabled:opacity-60"
        >
          {loading ? "Executando..." : "Executar"}
        </button>
      </form>

      {/* Resultado / Erro */}
      <div className="mt-4">
        {erro && <div className="text-red-400 text-sm">⚠️ {erro}</div>}
        {resp && (
          <pre className="mt-2 p-3 rounded-lg bg-background border border-border text-sm overflow-x-auto">
{JSON.stringify(resp, null, 2)}
          </pre>
        )}
      </div>
    </div>
  );
}
