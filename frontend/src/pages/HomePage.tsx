import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import { useProgress } from "../hooks/useApi";

export default function HomePage() {
  const navigate = useNavigate();
  const { progress } = useProgress();

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        background: "linear-gradient(180deg, #87CEEB 0%, #98FB98 50%, #90EE90 100%)",
        gap: 20,
        padding: 20,
        position: "relative",
        overflow: "hidden",
      }}
    >
      {/* Decorative clouds */}
      <motion.div
        animate={{ x: [0, 30, 0] }}
        transition={{ duration: 8, repeat: Infinity }}
        style={{ position: "absolute", top: 40, left: 20, fontSize: 48, opacity: 0.6 }}
      >
        ☁️
      </motion.div>
      <motion.div
        animate={{ x: [0, -20, 0] }}
        transition={{ duration: 6, repeat: Infinity }}
        style={{ position: "absolute", top: 80, right: 40, fontSize: 36, opacity: 0.5 }}
      >
        ☁️
      </motion.div>

      {/* Title */}
      <motion.div
        initial={{ y: -30, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ type: "spring" }}
        style={{ textAlign: "center" }}
      >
        <motion.div
          animate={{ rotate: [0, -5, 5, 0] }}
          transition={{ duration: 2, repeat: Infinity }}
          style={{ fontSize: 80 }}
        >
          🐵
        </motion.div>
        <h1
          style={{
            fontSize: 36,
            color: "#5D4037",
            textShadow: "2px 2px 0 rgba(255,255,255,0.8)",
            margin: "8px 0",
          }}
        >
          Wukong Math Quest
        </h1>
        <p style={{ fontSize: 18, color: "#795548" }}>
          悟空数学大冒险
        </p>
      </motion.div>

      {/* Peach counter */}
      {progress && (
        <div style={{ fontSize: 22, color: "#5D4037" }}>
          🍑 {progress.total_peaches} peaches collected
        </div>
      )}

      {/* Play button */}
      <motion.button
        whileHover={{ scale: 1.08 }}
        whileTap={{ scale: 0.92 }}
        onClick={() => navigate("/worlds")}
        style={{
          padding: "18px 60px",
          fontSize: 28,
          fontWeight: "bold",
          background: "linear-gradient(135deg, #FFD700, #FFA000)",
          color: "white",
          border: "none",
          borderRadius: 40,
          cursor: "pointer",
          boxShadow: "0 6px 20px rgba(255,160,0,0.4)",
          marginTop: 10,
        }}
      >
        ▶ Play!
      </motion.button>

      {/* Daily challenge */}
      <motion.button
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        onClick={() => navigate("/daily")}
        style={{
          padding: "12px 36px",
          fontSize: 18,
          background: "rgba(255,255,255,0.8)",
          color: "#FF9800",
          border: "2px solid #FF9800",
          borderRadius: 30,
          cursor: "pointer",
          fontWeight: "bold",
        }}
      >
        ⭐ Daily Challenge
      </motion.button>

      {/* Bottom decoration */}
      <div style={{ position: "absolute", bottom: 20, fontSize: 14, color: "#999" }}>
        🌺 Journey to the West 🌺
      </div>
    </div>
  );
}
