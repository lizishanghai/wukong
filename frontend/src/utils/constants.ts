import type { World } from "../types/game";

export const WORLD_COLORS: Record<World, string> = {
  flower_fruit_mountain: "#4CAF50",
  dragon_palace: "#2196F3",
  heaven_palace: "#FFC107",
  white_bone_cave: "#9C27B0",
  flaming_mountain: "#FF5722",
  journey_road: "#FF9800",
};

export const WORLD_EMOJIS: Record<World, string> = {
  flower_fruit_mountain: "🌺",
  dragon_palace: "🐉",
  heaven_palace: "☁️",
  white_bone_cave: "🦴",
  flaming_mountain: "🔥",
  journey_road: "🛤️",
};

/** Emoji representations for visual objects in the game. */
export const OBJECT_EMOJI: Record<string, string> = {
  peach: "🍑",
  monkey: "🐵",
  banana: "🍌",
  flower: "🌸",
  coconut: "🥥",
  fish: "🐟",
  shell: "🐚",
  pearl: "⚪",
  gem: "💎",
  coral: "🪸",
  star: "⭐",
  cloud: "☁️",
  moon: "🌙",
  lantern: "🏮",
  bone: "🦴",
  mask: "🎭",
  mirror: "🪞",
  candle: "🕯️",
  flame: "🔥",
  fan: "🪭",
  rock: "🪨",
  ember: "✨",
  spark: "💥",
  scroll: "📜",
  staff: "🏑",
  hat: "👒",
  // Separator for comparison
  "|": "│",
};

export function objectToEmoji(obj: string): string {
  // Handle "_new" suffix for addition visual objects
  const clean = obj.replace(/_new$/, "");
  return OBJECT_EMOJI[clean] ?? "❓";
}
