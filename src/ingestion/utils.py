from src.data_models.sound import SoundList
from src.ingestion.downloader import Downloader


def download_sound_previews(sound_list: SoundList):
    downloader = Downloader()
    for page in range(1, sound_list.count + 1):
        if sound.previews:
            for preview_url in sound.previews.__dict__.values():
                downloader.download(preview_url)
