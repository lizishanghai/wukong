import { useCallback, useEffect, useState } from "react";
import type { Level, WorldInfo, PlayerProgress, Costume } from "../types/game";

const BASE = "/api";

async function fetchJson<T>(url: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${url}`, {
    headers: { "Content-Type": "application/json" },
    ...init,
  });
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return res.json();
}

export function useWorlds() {
  const [worlds, setWorlds] = useState<WorldInfo[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetchJson<WorldInfo[]>("/levels/worlds").then(setWorlds).finally(() => setLoading(false));
  }, []);
  return { worlds, loading };
}

export function useWorldLevels(worldId: string) {
  const [levels, setLevels] = useState<Level[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetchJson<Level[]>(`/levels/world/${worldId}`).then(setLevels).finally(() => setLoading(false));
  }, [worldId]);
  return { levels, loading };
}

export function useLevel(levelId: string) {
  const [level, setLevel] = useState<Level | null>(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetchJson<Level>(`/levels/level/${levelId}`).then(setLevel).finally(() => setLoading(false));
  }, [levelId]);
  return { level, loading };
}

export function useDailyChallenge() {
  const [levels, setLevels] = useState<Level[]>([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetchJson<Level[]>("/levels/daily").then(setLevels).finally(() => setLoading(false));
  }, []);
  return { levels, loading };
}

export function useProgress() {
  const [progress, setProgress] = useState<PlayerProgress | null>(null);

  const refresh = useCallback(() => {
    fetchJson<PlayerProgress>("/progress/").then(setProgress);
  }, []);

  useEffect(() => { refresh(); }, [refresh]);

  const completeLevel = useCallback(async (levelId: string, stars: number, peaches: number) => {
    const updated = await fetchJson<PlayerProgress>("/progress/complete", {
      method: "POST",
      body: JSON.stringify({ level_id: levelId, stars, peaches_earned: peaches }),
    });
    setProgress(updated);
    return updated;
  }, []);

  return { progress, refresh, completeLevel };
}

export function useCostumes() {
  const [costumes, setCostumes] = useState<Costume[]>([]);
  useEffect(() => {
    fetchJson<Costume[]>("/progress/costumes").then(setCostumes);
  }, []);
  return { costumes };
}
