from pydantic import BaseModel
from typing import Optional


import pydantic


class SoundPreview(BaseModel):
    preview_hq_mp3: Optional[str] = pydantic.Field(None, alias="preview-hq-mp3")
    preview_hq_ogg: Optional[str] = pydantic.Field(None, alias="preview-hq-ogg")
    preview_lq_mp3: Optional[str] = pydantic.Field(None, alias="preview-lq-mp3")
    preview_lq_ogg: Optional[str] = pydantic.Field(None, alias="preview-lq-ogg")
