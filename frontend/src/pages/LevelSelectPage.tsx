import { motion } from "framer-motion";
import { useNavigate, useParams } from "react-router-dom";
import { useWorldLevels, useProgress } from "../hooks/useApi";
import { WORLD_COLORS, WORLD_EMOJIS } from "../utils/constants";
import type { World } from "../types/game";

const GAME_TYPE_EMOJI: Record<string, string> = {
  counting: "🔢",
  addition: "➕",
  subtraction: "➖",
  comparison: "⚖️",
  ordering: "📊",
  pattern: "🔄",
  classification: "📦",
  memory: "🧠",
  find_difference: "🔍",
  maze: "🗺️",
};

export default function LevelSelectPage() {
  const { worldId } = useParams<{ worldId: string }>();
  const navigate = useNavigate();
  const { levels, loading } = useWorldLevels(worldId ?? "");
  const { progress } = useProgress();

  const color = WORLD_COLORS[(worldId as World) ?? "flower_fruit_mountain"] ?? "#4CAF50";
  const emoji = WORLD_EMOJIS[(worldId as World) ?? "flower_fruit_mountain"] ?? "🌍";

  if (loading) {
    return (
      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center" }}>
        <motion.div animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 1 }} style={{ fontSize: 48 }}>
          🐵
        </motion.div>
      </div>
    );
  }

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        background: `linear-gradient(135deg, ${color}11, ${color}33)`,
        padding: 20,
        overflowY: "auto",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 20 }}>
        <button onClick={() => navigate("/worlds")} style={backStyle}>← Back</button>
        <h2 style={{ fontSize: 24, color: "#333" }}>
          {emoji} Levels
        </h2>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(140px, 1fr))",
          gap: 12,
        }}
      >
        {levels.map((level, idx) => {
          const completed = progress?.levels[level.id]?.completed ?? false;
          const stars = progress?.levels[level.id]?.stars ?? 0;

          return (
            <motion.div
              key={level.id}
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ delay: idx * 0.04 }}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => navigate(`/play/${level.id}`)}
              style={{
                padding: "14px 12px",
                borderRadius: 16,
                background: completed ? "#E8F5E9" : "white",
                border: `2px solid ${completed ? "#4CAF50" : "#ddd"}`,
                cursor: "pointer",
                textAlign: "center",
                boxShadow: "0 2px 8px rgba(0,0,0,0.06)",
              }}
            >
              <div style={{ fontSize: 28, marginBottom: 4 }}>
                {GAME_TYPE_EMOJI[level.game_type] ?? "🎮"}
              </div>
              <div style={{ fontSize: 14, fontWeight: "bold", color: "#333", marginBottom: 2 }}>
                {level.name}
              </div>
              <div style={{ fontSize: 12, color: "#999" }}>
                {level.game_type}
              </div>
              <div style={{ fontSize: 16, marginTop: 4 }}>
                {[1, 2, 3].map((s) => (
                  <span key={s}>{s <= stars ? "⭐" : "☆"}</span>
                ))}
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}

const backStyle: React.CSSProperties = {
  background: "none",
  border: "none",
  fontSize: 20,
  cursor: "pointer",
  padding: "4px 8px",
};
