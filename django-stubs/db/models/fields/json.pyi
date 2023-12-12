import json
from collections.abc import Callable
from typing import Any, ClassVar, TypeVar

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import lookups
from django.db.models.fields import TextField
from django.db.models.lookups import PostgresOperatorLookup, Transform
from django.db.models.sql.compiler import SQLCompiler
from django.utils.functional import _StrOrPromise
from typing_extensions import Self

from . import Field
from .mixins import CheckFieldDefaultMixin

# __set__ value type
_ST = TypeVar("_ST", contravariant=True, default=Any)
# __get__ return type
_GT = TypeVar("_GT", covariant=True, default=Any)

class JSONField(CheckFieldDefaultMixin, Field[_ST, _GT]):
    encoder: type[json.JSONEncoder] | None
    decoder: type[json.JSONDecoder] | None
    def __init__(
        self,
        verbose_name: _StrOrPromise | None = ...,
        name: str | None = ...,
        encoder: type[json.JSONEncoder] | None = ...,
        decoder: type[json.JSONDecoder] | None = ...,
        **kwargs: Any,
    ) -> None: ...

class DataContains(PostgresOperatorLookup): ...
class ContainedBy(PostgresOperatorLookup): ...

class HasKeyLookup(PostgresOperatorLookup):
    logical_operator: str | None
    def compile_json_path_final_key(self, key_transform: Any) -> str: ...

class HasKey(HasKeyLookup):
    postgres_operator: str

class HasKeys(HasKeyLookup):
    postgres_operator: str
    logical_operator: str

class HasAnyKeys(HasKeys):
    postgres_operator: str
    logical_operator: str

class HasKeyOrArrayIndex(HasKey): ...
class JSONExact(lookups.Exact): ...
class CaseInsensitiveMixin: ...
class JSONIContains(CaseInsensitiveMixin, lookups.IContains): ...

class KeyTransform(Transform):
    key_name: str
    postgres_operator: str
    postgres_nested_operator: str
    def __init__(self, key_name: Any, *args: Any, **kwargs: Any) -> None: ...
    def preprocess_lhs(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper) -> Any: ...

class KeyTextTransform(KeyTransform):
    postgres_operator: str
    postgres_nested_operator: str
    output_field: ClassVar[TextField]
    @classmethod
    def from_lookup(cls, lookup: str) -> Self: ...

KT: Callable[[str], KeyTextTransform]

class KeyTransformTextLookupMixin:
    def __init__(self, key_transform: Any, *args: Any, **kwargs: Any) -> None: ...

class KeyTransformIsNull(lookups.IsNull): ...
class KeyTransformIn(lookups.In): ...
class KeyTransformExact(JSONExact): ...
class KeyTransformIExact(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IExact): ...
class KeyTransformIContains(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IContains): ...
class KeyTransformStartsWith(KeyTransformTextLookupMixin, lookups.StartsWith): ...
class KeyTransformIStartsWith(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IStartsWith): ...
class KeyTransformEndsWith(KeyTransformTextLookupMixin, lookups.EndsWith): ...
class KeyTransformIEndsWith(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IEndsWith): ...
class KeyTransformRegex(KeyTransformTextLookupMixin, lookups.Regex): ...
class KeyTransformIRegex(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IRegex): ...
class KeyTransformNumericLookupMixin: ...
class KeyTransformLt(KeyTransformNumericLookupMixin, lookups.LessThan): ...
class KeyTransformLte(KeyTransformNumericLookupMixin, lookups.LessThanOrEqual): ...
class KeyTransformGt(KeyTransformNumericLookupMixin, lookups.GreaterThan): ...
class KeyTransformGte(KeyTransformNumericLookupMixin, lookups.GreaterThanOrEqual): ...

class KeyTransformFactory:
    key_name: Any
    def __init__(self, key_name: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> KeyTransform: ...
