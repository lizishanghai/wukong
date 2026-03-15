import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import { useWorlds, useProgress } from "../hooks/useApi";
import { WORLD_EMOJIS } from "../utils/constants";
import type { World } from "../types/game";

const WORLD_ORDER: World[] = [
  "flower_fruit_mountain",
  "dragon_palace",
  "heaven_palace",
  "white_bone_cave",
  "flaming_mountain",
  "journey_road",
];

export default function WorldSelectPage() {
  const navigate = useNavigate();
  const { worlds, loading } = useWorlds();
  const { progress } = useProgress();

  if (loading) return <LoadingScreen />;

  // Determine which worlds are unlocked based on progress
  const completedWorlds = new Set<string>();
  if (progress) {
    // A world is "completed" if all its levels are completed
    // For simplicity, unlock next world if any level in current world is completed
    for (const [levelId, data] of Object.entries(progress.levels)) {
      if (data.completed) {
        const worldPrefix = levelId.split("_").slice(0, -1).join("_");
        // Just mark that the player has been active
        completedWorlds.add(worldPrefix);
      }
    }
  }

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        background: "linear-gradient(180deg, #E3F2FD, #BBDEFB)",
        padding: 20,
        overflowY: "auto",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 20 }}>
        <button onClick={() => navigate("/")} style={backStyle}>← Home</button>
        <h2 style={{ fontSize: 24, color: "#333" }}>Choose a World</h2>
        {progress && <span style={{ marginLeft: "auto", fontSize: 18 }}>🍑 {progress.total_peaches}</span>}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
        {WORLD_ORDER.map((worldId, idx) => {
          const world = worlds.find((w) => w.id === worldId);
          // For now, unlock all worlds (in production, gate by progress)
          const unlocked = true;

          return (
            <motion.div
              key={worldId}
              initial={{ x: -40, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              transition={{ delay: idx * 0.1 }}
              whileHover={unlocked ? { scale: 1.02 } : {}}
              whileTap={unlocked ? { scale: 0.98 } : {}}
              onClick={() => unlocked && navigate(`/world/${worldId}`)}
              style={{
                display: "flex",
                alignItems: "center",
                gap: 16,
                padding: "16px 20px",
                borderRadius: 20,
                background: unlocked ? "white" : "rgba(200,200,200,0.5)",
                cursor: unlocked ? "pointer" : "not-allowed",
                boxShadow: unlocked ? "0 4px 16px rgba(0,0,0,0.08)" : "none",
                border: `3px solid ${world?.theme_color ?? "#ddd"}`,
                opacity: unlocked ? 1 : 0.5,
              }}
            >
              <span style={{ fontSize: 48 }}>
                {WORLD_EMOJIS[worldId] ?? "🌍"}
              </span>
              <div>
                <h3 style={{ fontSize: 20, margin: 0, color: "#333" }}>
                  {world?.name ?? worldId} {world?.name_cn ? `(${world.name_cn})` : ""}
                </h3>
                <p style={{ fontSize: 14, color: "#777", margin: "4px 0 0" }}>
                  {world?.description ?? ""}
                </p>
                <p style={{ fontSize: 13, color: "#999", margin: "2px 0 0" }}>
                  {world?.level_count ?? 0} levels
                </p>
              </div>
              {!unlocked && (
                <span style={{ marginLeft: "auto", fontSize: 28 }}>🔒</span>
              )}
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}

function LoadingScreen() {
  return (
    <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <motion.div animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 1 }} style={{ fontSize: 48 }}>
        🐵
      </motion.div>
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
