import requests
from typing import Optional, List

from src.data_models.sound import Sound, SoundList


class FreesoundClient:
    def __init__(self, api_key: str, client_id: str):
        self.api_key = api_key
        self.client_id = client_id

    @property
    def base_url(self) -> str:
        return "https://freesound.org/apiv2/search/text/"

    @property
    def headers(self) -> dict:
        return {"Authorization": f"Token {self.api_key}"}

    def search_query_parameters(self, query: str, page: int, page_size: int) -> dict:
        return {
            "query": query,
            "page": page,
            "page_size": page_size,
        }

    def _fetch_page(self, url: str, params: Optional[dict] = None) -> SoundList:
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()

        return SoundList.model_validate(response.json())

    def search(
        self, query: str, page: int = 1, page_size: int = 10, max_pages: int = 1
    ) -> List[Sound]:

        results: List[Sound] = []

        url = self.base_url
        params = self.search_query_parameters(query, page, page_size)

        for _ in range(max_pages):
            page_data = self._fetch_page(url, params)

            # JSON -> SoundList -> List[Sound]
            results.extend(page_data.results)

            url = page_data.next
            params = None  # important : next URL already contains params

            if not url:
                break

        return results
