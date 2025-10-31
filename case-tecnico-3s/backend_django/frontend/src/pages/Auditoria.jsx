import { useEffect, useState } from "react"

export default function Auditoria() {
  const [auditorias, setAuditorias] = useState([])

  useEffect(() => {
    fetch("http://localhost:8001/graphql/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: "{ auditorias { modulo acao sucesso } }" }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("🔍 Retorno GraphQL:", data)
        setAuditorias(data.data?.auditorias || [])
      })
      .catch((err) => console.error("Erro no GraphQL:", err))
  }, [])



  return (
    <div>
      <h2 className="text-2xl mb-4 font-semibold">Auditorias</h2>
      <table className="w-full border-collapse border border-border text-sm">
        <thead className="bg-secondary text-accent">
          <tr>
            <th className="border border-border px-4 py-2">Módulo</th>
            <th className="border border-border px-4 py-2">Ação</th>
            <th className="border border-border px-4 py-2">Sucesso</th>
          </tr>
        </thead>
        <tbody>
          {auditorias.map((a, i) => (
            <tr key={i} className="hover:bg-secondary/70">
              <td className="border border-border px-4 py-2">{a.modulo}</td>
              <td className="border border-border px-4 py-2">{a.acao}</td>
              <td className="border border-border px-4 py-2">
                {a.sucesso ? "✅" : "❌"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
