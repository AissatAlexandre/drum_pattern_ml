from pydantic import BaseModel
from typing import List, Optional
from src.data_models.sound_preview import SoundPreview


class Sound(BaseModel):
    id: int
    name: str
    tags: List[str]
    description: str
    duration: float
    category: str
    subcategory: str
    previews: Optional[SoundPreview] = None
    model_config = {"extra": "ignore"}


class SoundList(BaseModel):
    count: int
    next: Optional[str] = None
    previous: Optional[str] = None
    results: List[Sound]
