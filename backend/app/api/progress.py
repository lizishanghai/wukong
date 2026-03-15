"""Player progress API endpoints.

Uses a simple JSON file for storage. In production, swap for a database.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..core.config import DATA_DIR, COSTUMES

router = APIRouter(prefix="/api/progress", tags=["progress"])

PROGRESS_FILE = DATA_DIR / "progress.json"


def _load_progress() -> dict[str, Any]:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return _default_progress()


def _save_progress(data: dict[str, Any]) -> None:
    PROGRESS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _default_progress() -> dict[str, Any]:
    return {
        "player_id": "default",
        "total_peaches": 0,
        "current_world": "flower_fruit_mountain",
        "current_costume": "default",
        "unlocked_costumes": ["default"],
        "levels": {},
        "streak_days": 0,
    }


# ---- Endpoints ----


@router.get("/")
def get_progress() -> dict[str, Any]:
    """Return current player progress."""
    return _load_progress()


class LevelCompleteRequest(BaseModel):
    level_id: str
    stars: int = 1  # 1-3 based on attempts
    peaches_earned: int = 1


@router.post("/complete")
def complete_level(req: LevelCompleteRequest) -> dict[str, Any]:
    """Mark a level as completed and award peaches."""
    progress = _load_progress()

    level_data = progress["levels"].get(req.level_id, {
        "level_id": req.level_id,
        "completed": False,
        "stars": 0,
        "attempts": 0,
    })

    level_data["completed"] = True
    level_data["attempts"] += 1
    level_data["stars"] = max(level_data["stars"], req.stars)
    progress["levels"][req.level_id] = level_data
    progress["total_peaches"] += req.peaches_earned

    _save_progress(progress)
    return progress


class CostumePurchaseRequest(BaseModel):
    costume_id: str


@router.post("/costume")
def buy_costume(req: CostumePurchaseRequest) -> dict[str, Any]:
    """Purchase a costume with peaches."""
    if req.costume_id not in COSTUMES:
        raise HTTPException(404, f"Costume '{req.costume_id}' not found")

    progress = _load_progress()
    costume = COSTUMES[req.costume_id]

    if req.costume_id in progress["unlocked_costumes"]:
        raise HTTPException(400, "Costume already owned")

    if progress["total_peaches"] < costume["cost"]:
        raise HTTPException(400, "Not enough peaches")

    progress["total_peaches"] -= costume["cost"]
    progress["unlocked_costumes"].append(req.costume_id)
    progress["current_costume"] = req.costume_id

    _save_progress(progress)
    return progress


@router.post("/reset")
def reset_progress() -> dict[str, Any]:
    """Reset all progress (parent action)."""
    progress = _default_progress()
    _save_progress(progress)
    return progress


@router.get("/costumes")
def list_costumes() -> list[dict[str, Any]]:
    """List all available costumes with prices."""
    progress = _load_progress()
    result = []
    for cid, meta in COSTUMES.items():
        result.append({
            "id": cid,
            "name": meta["name"],
            "cost": meta["cost"],
            "owned": cid in progress["unlocked_costumes"],
        })
    return result
