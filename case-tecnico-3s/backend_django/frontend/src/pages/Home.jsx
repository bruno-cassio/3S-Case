import CardMenu from "../components/CardMenu";
import Dashboard from "../components/Dashboard";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  return (
    <Dashboard>
      <CardMenu
        title="Auditoria"
        description="Ver registros do backend e API"
        onClick={() => navigate("/auditoria")}
      />

      <CardMenu
        title="API FastAPI"
        description="Explorar as 4 questões com interface interativa"
        onClick={() => navigate("/api")}
      />
    </Dashboard>
  );
}
