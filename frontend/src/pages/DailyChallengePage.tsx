import { useState, useCallback, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useDailyChallenge, useProgress } from "../hooks/useApi";
import { useSpeech } from "../hooks/useSpeech";
import GameShell from "../components/ui/GameShell";
import GameDispatcher from "../components/games/GameDispatcher";
import Celebration from "../components/ui/Celebration";
import FeedbackToast from "../components/ui/FeedbackToast";
import { motion } from "framer-motion";

export default function DailyChallengePage() {
  const navigate = useNavigate();
  const { levels, loading } = useDailyChallenge();
  const { progress, completeLevel } = useProgress();
  const { speak, stop } = useSpeech();
  const [currentIdx, setCurrentIdx] = useState(0);
  const [showCelebration, setShowCelebration] = useState(false);
  const [attempts, setAttempts] = useState(0);
  const [feedback, setFeedback] = useState<"correct" | "wrong" | null>(null);

  const level = levels[currentIdx];

  // Read question aloud when level changes
  useEffect(() => {
    if (level) {
      const timer = setTimeout(() => {
        speak(level.question.text);
      }, 500);
      return () => clearTimeout(timer);
    }
  }, [level, speak]);

  useEffect(() => {
    return () => stop();
  }, [stop]);

  const showFeedbackToast = useCallback((type: "correct" | "wrong") => {
    setFeedback(type);
    setTimeout(() => setFeedback(null), type === "correct" ? 1200 : 1500);
  }, []);

  const handleCorrect = useCallback(async () => {
    if (!level) return;
    showFeedbackToast("correct");
    speak("正确! 太棒了!", "zh-CN");
    const stars = attempts === 0 ? 3 : attempts === 1 ? 2 : 1;
    await completeLevel(level.id, stars, level.reward.peaches);
    setTimeout(() => setShowCelebration(true), 1200);
  }, [level, attempts, completeLevel, showFeedbackToast, speak]);

  const handleWrong = useCallback(() => {
    showFeedbackToast("wrong");
    speak("错误，再试一次!", "zh-CN");
    setAttempts((a) => a + 1);
  }, [showFeedbackToast, speak]);

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

      <FeedbackToast type={feedback} />

      {showCelebration && (
        <Celebration reward={level.reward} onContinue={handleContinue} />
      )}
    </>
  );
}
