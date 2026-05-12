from pydantic import BaseModel
from typing import List
from src.core.labels import DrumLabel


class AudioDatasetItem(BaseModel):
    source_id: int
    id: int
    filepath: str
    label: DrumLabel
    tags: List[str]
    duration: float | None = None