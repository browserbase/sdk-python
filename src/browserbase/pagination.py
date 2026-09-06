# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncDownloadsPage", "AsyncDownloadsPage"]

_T = TypeVar("_T")


class SyncDownloadsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    downloads: List[_T]
    total: Optional[int] = None
    limit: Optional[int] = None
    offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        downloads = self.downloads
        if not downloads:
            return []
        return downloads

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total = self.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncDownloadsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    downloads: List[_T]
    total: Optional[int] = None
    limit: Optional[int] = None
    offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        downloads = self.downloads
        if not downloads:
            return []
        return downloads

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total = self.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"offset": current_count})

        return None
