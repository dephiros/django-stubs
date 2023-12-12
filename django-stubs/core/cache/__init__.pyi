from typing import Any, TypeVar

from django.utils.connection import BaseConnectionHandler

from .backends.base import BaseCache as BaseCache
from .backends.base import CacheKeyWarning as CacheKeyWarning
from .backends.base import InvalidCacheBackendError as InvalidCacheBackendError
from .backends.base import InvalidCacheKey as InvalidCacheKey

DEFAULT_CACHE_ALIAS: str

_T = TypeVar("_T")

class CacheHandler(BaseConnectionHandler[_T]):
    settings_name: str
    exception_class: type[Exception]
    def create_connection(self, alias: str) -> BaseCache: ...
    def all(self, initialized_only: bool = ...) -> list[BaseCache]: ...

def close_caches(**kwargs: Any) -> None: ...

cache: BaseCache
caches: CacheHandler[Any]
