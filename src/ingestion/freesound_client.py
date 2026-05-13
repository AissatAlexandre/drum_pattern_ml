from dataclasses import dataclass


@dataclass
class FreesoundClient:
    api_key: str
    client_id: str

    def search(self, query: str, page: str, page_size: str):
        pass
