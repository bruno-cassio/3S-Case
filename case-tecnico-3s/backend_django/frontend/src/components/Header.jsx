import { Link } from "react-router-dom"

export default function Header() {
  return (
    <header className="bg-secondary border-b border-border px-6 py-4 flex justify-between items-center">
      <h1 className="text-xl font-bold text-accent">CASE 3S</h1>
      <nav className="flex gap-6 text-sm">
        <Link to="/" className="hover:text-accent">Início</Link>
        <Link to="/auditoria" className="hover:text-accent">Auditoria</Link>
      </nav>
    </header>
  )
}
