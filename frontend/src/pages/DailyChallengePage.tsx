import { useState, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { useDailyChallenge, useProgress } from "../hooks/useApi";
import GameShell from "../components/ui/GameShell";
import GameDispatcher from "../components/games/GameDispatcher";
import Celebration from "../components/ui/Celebration";
import { motion } from "framer-motion";

export default function DailyChallengePage() {
  const navigate = useNavigate();
  const { levels, loading } = useDailyChallenge();
  const { progress, completeLevel } = useProgress();
  const [currentIdx, setCurrentIdx] = useState(0);
  const [showCelebration, setShowCelebration] = useState(false);
  const [attempts, setAttempts] = useState(0);

  const level = levels[currentIdx];

  const handleCorrect = useCallback(async () => {
    if (!level) return;
    const stars = attempts === 0 ? 3 : attempts === 1 ? 2 : 1;
    await completeLevel(level.id, stars, level.reward.peaches);
    setShowCelebration(true);
  }, [level, attempts, completeLevel]);

  const handleWrong = useCallback(() => {
    setAttempts((a) => a + 1);
  }, []);

  const handleContinue = useCallback(() => {
    setShowCelebration(false);
    setAttempts(0);
    if (currentIdx < levels.length - 1) {
      setCurrentIdx(currentIdx + 1);
    } else {
      navigate("/");
    }
  }, [currentIdx, levels.length, navigate]);

  if (loading || !level) {
    return (
      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center" }}>
        <motion.div animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 1 }} style={{ fontSize: 48 }}>
          ⭐
        </motion.div>
      </div>
    );
  }

  return (
    <>
      <GameShell
        level={level}
        peaches={progress?.total_peaches ?? 0}
        onBack={() => navigate("/")}
      >
        <div style={{ fontSize: 14, color: "#666", textAlign: "center" }}>
          Daily Challenge {currentIdx + 1} / {levels.length}
        </div>
        <GameDispatcher level={level} onCorrect={handleCorrect} onWrong={handleWrong} />
      </GameShell>

      {showCelebration && (
        <Celebration reward={level.reward} onContinue={handleContinue} />
      )}
    </>
  );
}
