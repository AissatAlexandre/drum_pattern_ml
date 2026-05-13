from enum import Enum


class AudioQuality(str, Enum):
    HQ = "hq"
    LQ = "lq"


class AudioFormat(str, Enum):
    MP3 = "mp3"
    OGG = "ogg"
