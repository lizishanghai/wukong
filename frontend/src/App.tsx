import { HashRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import WorldSelectPage from "./pages/WorldSelectPage";
import LevelSelectPage from "./pages/LevelSelectPage";
import PlayLevelPage from "./pages/PlayLevelPage";
import DailyChallengePage from "./pages/DailyChallengePage";

export default function App() {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/worlds" element={<WorldSelectPage />} />
        <Route path="/world/:worldId" element={<LevelSelectPage />} />
        <Route path="/play/:levelId" element={<PlayLevelPage />} />
        <Route path="/daily" element={<DailyChallengePage />} />
      </Routes>
    </HashRouter>
  );
}
