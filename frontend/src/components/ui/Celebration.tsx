import { motion } from "framer-motion";
import type { LevelReward } from "../../types/game";

interface Props {
  reward: LevelReward;
  onContinue: () => void;
}

const confettiColors = ["#FFD700", "#FF6B6B", "#4CAF50", "#2196F3", "#FF9800", "#E91E63"];

export default function Celebration({ reward, onContinue }: Props) {
  const charEmoji =
    reward.character === "wukong" ? "🐵" :
    reward.character === "bajie" ? "🐷" :
    reward.character === "sha_wujing" ? "🧔" : "🧙";

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      style={{
        position: "fixed",
        inset: 0,
        background: "rgba(0,0,0,0.5)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        zIndex: 1000,
      }}
    >
      {/* Confetti particles */}
      {Array.from({ length: 20 }).map((_, i) => (
        <motion.div
          key={i}
          initial={{
            x: Math.random() * window.innerWidth,
            y: -20,
            rotate: 0,
            scale: Math.random() * 0.5 + 0.5,
          }}
          animate={{
            y: window.innerHeight + 20,
            rotate: 360 * (Math.random() > 0.5 ? 1 : -1),
          }}
          transition={{
            duration: 2 + Math.random() * 2,
            ease: "easeIn",
            delay: Math.random() * 0.5,
          }}
          style={{
            position: "fixed",
            width: 12,
            height: 12,
            borderRadius: Math.random() > 0.5 ? "50%" : 2,
            background: confettiColors[i % confettiColors.length],
            zIndex: 1001,
          }}
        />
      ))}

      {/* Card */}
      <motion.div
        initial={{ scale: 0.5, y: 50 }}
        animate={{ scale: 1, y: 0 }}
        transition={{ type: "spring", damping: 12 }}
        style={{
          background: "white",
          borderRadius: 24,
          padding: "32px 40px",
          textAlign: "center",
          maxWidth: 360,
          boxShadow: "0 8px 40px rgba(0,0,0,0.3)",
          zIndex: 1002,
        }}
      >
        <motion.div
          animate={{ rotate: [0, -10, 10, -10, 10, 0] }}
          transition={{ duration: 0.6, delay: 0.3 }}
          style={{ fontSize: 64 }}
        >
          {charEmoji}
        </motion.div>

        <h2 style={{ margin: "12px 0 8px", fontSize: 24, color: "#333" }}>
          {reward.dialogue}
        </h2>

        <div style={{ fontSize: 28, margin: "8px 0 16px" }}>
          {"🍑".repeat(reward.peaches)} +{reward.peaches}
        </div>

        <div style={{ display: "flex", gap: 6, justifyContent: "center", marginBottom: 20 }}>
          {[1, 2, 3].map((s) => (
            <motion.span
              key={s}
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ delay: 0.3 + s * 0.2 }}
              style={{ fontSize: 32 }}
            >
              {s <= reward.peaches ? "⭐" : "☆"}
            </motion.span>
          ))}
        </div>

        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={onContinue}
          style={{
            padding: "14px 40px",
            fontSize: 20,
            fontWeight: "bold",
            background: "linear-gradient(135deg, #FFD700, #FFA000)",
            color: "white",
            border: "none",
            borderRadius: 30,
            cursor: "pointer",
            boxShadow: "0 4px 12px rgba(255,160,0,0.4)",
          }}
        >
          Continue →
        </motion.button>
      </motion.div>
    </motion.div>
  );
}
