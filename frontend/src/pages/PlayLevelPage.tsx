import { useState, useCallback, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useLevel, useProgress } from "../hooks/useApi";
import { useSpeech } from "../hooks/useSpeech";
import { useGameStore } from "../stores/gameStore";
import GameShell from "../components/ui/GameShell";
import GameDispatcher from "../components/games/GameDispatcher";
import Celebration from "../components/ui/Celebration";
import FeedbackToast from "../components/ui/FeedbackToast";
import { motion } from "framer-motion";

export default function PlayLevelPage() {
  const { levelId } = useParams<{ levelId: string }>();
  const navigate = useNavigate();
  const { level, loading } = useLevel(levelId ?? "");
  const { progress, completeLevel } = useProgress();
  const { attempts, addAttempt, resetAttempts } = useGameStore();
  const { speak, stop } = useSpeech();

  const [showCelebration, setShowCelebration] = useState(false);
  const [hintIdx, setHintIdx] = useState(0);
  const [showHint, setShowHint] = useState(false);
  const [feedback, setFeedback] = useState<"correct" | "wrong" | null>(null);

  // Read the question aloud when the level loads
  useEffect(() => {
    if (level) {
      // Small delay to let the page render first
      const timer = setTimeout(() => {
        speak(level.question.text);
      }, 500);
      return () => clearTimeout(timer);
    }
  }, [level, speak]);

  // Stop speech on unmount
  useEffect(() => {
    return () => stop();
  }, [stop]);

  const showFeedback = useCallback((type: "correct" | "wrong") => {
    setFeedback(type);
    setTimeout(() => setFeedback(null), type === "correct" ? 1200 : 1500);
  }, []);

  const handleCorrect = useCallback(async () => {
    if (!level) return;
    showFeedback("correct");
    speak("正确! 太棒了!", "zh-CN");
    const stars = attempts === 0 ? 3 : attempts === 1 ? 2 : 1;
    await completeLevel(level.id, stars, level.reward.peaches);
    // Show celebration after the feedback toast fades
    setTimeout(() => setShowCelebration(true), 1200);
  }, [level, attempts, completeLevel, showFeedback, speak]);

  const handleWrong = useCallback(() => {
    showFeedback("wrong");
    speak("错误，再试一次!", "zh-CN");
    addAttempt();
    // Show hint after 2 wrong attempts
    if (attempts >= 1) {
      setShowHint(true);
    }
  }, [addAttempt, attempts, showFeedback, speak]);

  const handleContinue = useCallback(() => {
    setShowCelebration(false);
    resetAttempts();
    setShowHint(false);
    setHintIdx(0);
    // Navigate to next level or back to world
    if (level) {
      const parts = level.id.split("_");
      const worldPrefix = parts.slice(0, -1).join("_");
      const num = parseInt(parts[parts.length - 1], 10);
      const nextId = `${worldPrefix}_${String(num + 1).padStart(2, "0")}`;
      // Try to go to next level, fall back to world page
      navigate(`/play/${nextId}`);
    } else {
      navigate("/worlds");
    }
  }, [level, navigate, resetAttempts]);

  if (loading) {
    return (
      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center" }}>
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ repeat: Infinity, duration: 1 }}
          style={{ fontSize: 48 }}
        >
          🐵
        </motion.div>
      </div>
    );
  }

  if (!level) {
    return (
      <div style={{ width: "100%", height: "100%", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 16 }}>
        <div style={{ fontSize: 48 }}>🎉</div>
        <h2>World Complete!</h2>
        <p>You've finished all levels!</p>
        <button
          onClick={() => navigate("/worlds")}
          style={{
            padding: "12px 30px",
            fontSize: 18,
            background: "#FFD700",
            border: "none",
            borderRadius: 20,
            cursor: "pointer",
          }}
        >
          Back to Worlds
        </button>
      </div>
    );
  }

  return (
    <>
      <GameShell
        level={level}
        peaches={progress?.total_peaches ?? 0}
        onBack={() => navigate(`/world/${level.world}`)}
      >
        <GameDispatcher
          level={level}
          onCorrect={handleCorrect}
          onWrong={handleWrong}
        />

        {/* Hint display */}
        {showHint && level.hints.length > 0 && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            style={{
              padding: "10px 20px",
              background: "rgba(255,243,224,0.95)",
              borderRadius: 12,
              fontSize: 16,
              color: "#E65100",
              border: "2px solid #FFB74D",
              maxWidth: 300,
              textAlign: "center",
            }}
          >
            💡 {level.hints[Math.min(hintIdx, level.hints.length - 1)]}
          </motion.div>
        )}
      </GameShell>

      {/* Feedback toast: 正确! / 错误! */}
      <FeedbackToast type={feedback} />

      {showCelebration && (
        <Celebration reward={level.reward} onContinue={handleContinue} />
      )}
    </>
  );
}
