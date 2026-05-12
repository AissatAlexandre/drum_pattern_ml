from pydantic import BaseModel
from typing import List, Optional


class FreesoundPreview(BaseModel):
    preview_hq_mp3: Optional[str]


class FreesoundSound(BaseModel):
    id: int
    name: str
    tags: List[str]
    license: str
    username: str
    previews: Optional[FreesoundPreview] = None
    model_config = {"extra": "ignore"}