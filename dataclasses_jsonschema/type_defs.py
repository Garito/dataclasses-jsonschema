from enum import Enum
from typing import Union, Dict, Any, List, Type

try:
    # Supported in future python versions
    from typing import TypedDict  # type: ignore
except ImportError:
    from mypy_extensions import TypedDict


JsonEncodable = Union[int, float, str, bool]
JsonDict = Dict[str, Any]


class JsonSchemaMeta(TypedDict):
    """JSON schema field definitions. Example usage:

    >>> foo = field(metadata=JsonSchemaMeta(description="A foo that foos"))
    """
    description: str
    title: str
    examples: List
    read_only: bool
    write_only: bool
    # Additional extension properties that will be output prefixed with 'x-' when generating OpenAPI / Swagger schemas
    extensions: Dict[str, Any]


class SchemaType(Enum):
    DRAFT_06 = "Draft6"
    DRAFT_04 = "Draft4"
    SWAGGER_V2 = "2.0"
    SWAGGER_V3 = "3.0"
    # Alias of SWAGGER_V2
    V2 = "2.0"
    # Alias of SWAGGER_V3
    V3 = "3.0"
    OPENAPI_3 = "3.0"


# Retained for backwards compatibility
SwaggerSpecVersion = SchemaType


class _NULL_TYPE:
    """Sentinel value to represent null json values for nullable fields, to distinguish them from `None`
    for omitted fields.
    """
    pass


NULL = _NULL_TYPE()


class _Nullable:
    """Nullable type annotation. Used to declare fields which can have a null value.
    This is distinct from `None`, which refers to the absence of a value.
    """

    def __getitem__(self, item: Type):
        return Union[item, _NULL_TYPE]


Nullable = _Nullable()
