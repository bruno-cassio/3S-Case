import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import FastAPI from "./pages/FastAPI";
import Auditoria from "./pages/Auditoria";
import NotFound from "./pages/NotFound";
import Header from "./components/Header";

export default function App() {
  console.log("🔧 App.jsx renderizou");
  return (
    <div className="bg-gray-900 text-white min-h-screen flex flex-col">
      <Header />
      <div className="p-4">
        <Routes>
          <Route index element={<Home />} />
          <Route path="/api" element={<FastAPI />} />
          <Route path="/auditoria" element={<Auditoria />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </div>
  );
}
