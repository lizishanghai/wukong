"""Pydantic models for the Wukong game."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class World(str, Enum):
    FLOWER_FRUIT_MOUNTAIN = "flower_fruit_mountain"
    DRAGON_PALACE = "dragon_palace"
    HEAVEN_PALACE = "heaven_palace"
    WHITE_BONE_CAVE = "white_bone_cave"
    FLAMING_MOUNTAIN = "flaming_mountain"
    JOURNEY_ROAD = "journey_road"


class GameType(str, Enum):
    COUNTING = "counting"
    ADDITION = "addition"
    SUBTRACTION = "subtraction"
    COMPARISON = "comparison"
    ORDERING = "ordering"
    PATTERN = "pattern"
    CLASSIFICATION = "classification"
    MEMORY = "memory"
    FIND_DIFFERENCE = "find_difference"
    MAZE = "maze"


class Difficulty(int, Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


# ---------------------------------------------------------------------------
# Level schema
# ---------------------------------------------------------------------------

class LevelQuestion(BaseModel):
    text: str = Field(..., description="Question text (also used as voice narration)")
    visual_objects: list[str] = Field(default_factory=list, description="Object IDs to render")
    options: list[Any] = Field(default_factory=list, description="Answer options")
    correct_answer: Any = Field(..., description="The correct answer")
    pairs: list[list[str]] | None = Field(None, description="For memory match: list of pairs")
    grid: list[list[int]] | None = Field(None, description="For maze: 2D grid (0=path,1=wall)")
    start: list[int] | None = Field(None, description="Maze start position [row,col]")
    end: list[int] | None = Field(None, description="Maze end position [row,col]")
    sequence: list[Any] | None = Field(None, description="For pattern/ordering games")
    groups: dict[str, list[str]] | None = Field(None, description="For classification")
    scene_a: list[str] | None = Field(None, description="Find-difference scene A")
    scene_b: list[str] | None = Field(None, description="Find-difference scene B")
    differences: list[str] | None = Field(None, description="List of difference descriptions")


class LevelReward(BaseModel):
    peaches: int = Field(1, ge=1, le=3)
    animation: str = "celebrate"
    dialogue: str = "Great job!"
    character: str = "wukong"


class LevelHints(BaseModel):
    hints: list[str] = Field(default_factory=list)


class Level(BaseModel):
    id: str = Field(..., description="Unique level id, e.g. 'w1_01'")
    world: World
    level_number: int = Field(..., ge=1)
    name: str
    story_intro: str = Field(..., description="Short story setup for this level")
    character: str = Field("wukong", description="Character who speaks in this level")
    game_type: GameType
    difficulty: Difficulty = Difficulty.EASY
    question: LevelQuestion
    reward: LevelReward = Field(default_factory=LevelReward)
    hints: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# World metadata
# ---------------------------------------------------------------------------

class WorldInfo(BaseModel):
    id: World
    name: str
    name_cn: str
    description: str
    theme_color: str
    characters: list[str]
    level_count: int


# ---------------------------------------------------------------------------
# Player progress
# ---------------------------------------------------------------------------

class LevelProgress(BaseModel):
    level_id: str
    completed: bool = False
    stars: int = Field(0, ge=0, le=3)
    attempts: int = 0


class PlayerProgress(BaseModel):
    player_id: str = "default"
    total_peaches: int = 0
    current_world: World = World.FLOWER_FRUIT_MOUNTAIN
    current_costume: str = "default"
    unlocked_costumes: list[str] = Field(default_factory=lambda: ["default"])
    levels: dict[str, LevelProgress] = Field(default_factory=dict)
    streak_days: int = 0
