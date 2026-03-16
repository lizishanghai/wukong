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
  // Sight words / Phonics images
  apple: "🍎",
  ant: "🐜",
  ball: "⚽",
  bear: "🐻",
  bee: "🐝",
  bird: "🐦",
  book: "📚",
  bus: "🚌",
  cake: "🎂",
  car: "🚗",
  cat: "🐱",
  cow: "🐄",
  cup: "☕",
  dog: "🐶",
  duck: "🦆",
  egg: "🥚",
  elephant: "🐘",
  eye: "👁️",
  frog: "🐸",
  grape: "🍇",
  hand: "✋",
  hat_item: "🎩",
  horse: "🐴",
  house: "🏠",
  ice: "🧊",
  juice: "🧃",
  key: "🔑",
  kite: "🪁",
  leaf: "🍃",
  lion: "🦁",
  milk: "🥛",
  nest: "🪺",
  orange: "🍊",
  pen: "🖊️",
  pig: "🐷",
  queen: "👑",
  rain: "🌧️",
  ring: "💍",
  rose: "🌹",
  ship: "🚢",
  shoe: "👟",
  snake: "🐍",
  sun: "☀️",
  table: "🪑",
  tree: "🌳",
  umbrella: "☂️",
  van: "🚐",
  water: "💧",
  whale: "🐋",
  zebra: "🦓",
  // Shapes
  red_circle: "🔴",
  blue_circle: "🔵",
  green_circle: "🟢",
  yellow_circle: "🟡",
  red_square: "🟥",
  blue_square: "🟦",
  green_square: "🟩",
  yellow_square: "🟨",
  red_triangle: "🔺",
  blue_diamond: "🔷",
  orange_diamond: "🔶",
  purple_heart: "💜",
  red_heart: "❤️",
  star_shape: "⭐",
  // Separator for comparison
  "|": "│",
};

export function objectToEmoji(obj: string): string {
  // Handle "_new" suffix for addition visual objects
  const clean = obj.replace(/_new$/, "");
  return OBJECT_EMOJI[clean] ?? "❓";
}

/** Resolves a relative image path using the app base URL. */
export function resolveAssetPath(path: string): string {
  if (path.startsWith("http")) return path;
  const base = import.meta.env.BASE_URL ?? "/";
  return `${base}${path}`;
}

/** Returns true if the string looks like an image path. */
export function isImagePath(s: string): boolean {
  return s.startsWith("images/") || s.startsWith("/images/");
}
