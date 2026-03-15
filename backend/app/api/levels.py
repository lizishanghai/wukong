"""Level API endpoints."""

from __future__ import annotations

import json
from typing import Any

from fastapi import APIRouter, HTTPException, Query

from ..core.config import LEVELS_FILE, WORLDS_META
from ..core.level_generator import generate_daily_challenge, generate_level

router = APIRouter(prefix="/api/levels", tags=["levels"])

# Cache loaded levels in memory
_levels_cache: list[dict[str, Any]] | None = None


def _load_levels() -> list[dict[str, Any]]:
    global _levels_cache
    if _levels_cache is None:
        with open(LEVELS_FILE, encoding="utf-8") as f:
            _levels_cache = json.load(f)
    return _levels_cache


@router.get("/")
def list_levels(
    world: str | None = Query(None, description="Filter by world id"),
    game_type: str | None = Query(None, description="Filter by game type"),
) -> list[dict[str, Any]]:
    """Return all levels, optionally filtered by world or game type."""
    levels = _load_levels()
    if world:
        levels = [lv for lv in levels if lv["world"] == world]
    if game_type:
        levels = [lv for lv in levels if lv["game_type"] == game_type]
    return levels


@router.get("/worlds")
def list_worlds() -> list[dict[str, Any]]:
    """Return world metadata in order."""
    levels = _load_levels()
    result = []
    for world_id, meta in WORLDS_META.items():
        count = sum(1 for lv in levels if lv["world"] == world_id)
        result.append({**meta, "id": world_id, "level_count": count})
    return result


@router.get("/world/{world_id}")
def get_world_levels(world_id: str) -> list[dict[str, Any]]:
    """Return all levels for a specific world."""
    levels = _load_levels()
    world_levels = [lv for lv in levels if lv["world"] == world_id]
    if not world_levels:
        raise HTTPException(404, f"World '{world_id}' not found")
    return world_levels


@router.get("/level/{level_id}")
def get_level(level_id: str) -> dict[str, Any]:
    """Return a single level by ID."""
    levels = _load_levels()
    for lv in levels:
        if lv["id"] == level_id:
            return lv
    raise HTTPException(404, f"Level '{level_id}' not found")


@router.get("/daily")
def get_daily_challenge() -> list[dict[str, Any]]:
    """Return 3 AI-generated daily challenge levels."""
    return generate_daily_challenge()


@router.get("/generate")
def generate_new_level(
    world: str = Query("flower_fruit_mountain"),
    game_type: str = Query("counting"),
    difficulty: int = Query(1, ge=1, le=3),
) -> dict[str, Any]:
    """Generate a single AI level on demand."""
    return generate_level(world, game_type, difficulty)
