from __future__ import annotations

import sys
import typing
import typing_extensions
from typing import Generic, TypeVar, cast

from browserbase._utils import is_type_alias_type, extract_type_var_from_base

_T = TypeVar("_T")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
ExtensionsAlias = typing_extensions.TypeAliasType("ExtensionsAlias", str)

if sys.version_info >= (3, 12):
    StdlibAlias = typing.TypeAliasType("StdlibAlias", str)


class BaseGeneric(Generic[_T]): ...


class SubclassGeneric(BaseGeneric[_T]): ...


class BaseGenericMultipleTypeArgs(Generic[_T, _T2, _T3]): ...


class SubclassGenericMultipleTypeArgs(BaseGenericMultipleTypeArgs[_T, _T2, _T3]): ...


class SubclassDifferentOrderGenericMultipleTypeArgs(BaseGenericMultipleTypeArgs[_T2, _T, _T3]): ...


def test_is_type_alias_type_from_typing_extensions() -> None:
    assert is_type_alias_type(ExtensionsAlias)
    assert not is_type_alias_type(str)


if sys.version_info >= (3, 12):

    def test_is_type_alias_type_from_typing() -> None:
        assert is_type_alias_type(StdlibAlias)


def test_extract_type_var() -> None:
    assert (
        extract_type_var_from_base(
            BaseGeneric[int],
            index=0,
            generic_bases=cast("tuple[type, ...]", (BaseGeneric,)),
        )
        == int
    )


def test_extract_type_var_generic_subclass() -> None:
    assert (
        extract_type_var_from_base(
            SubclassGeneric[int],
            index=0,
            generic_bases=cast("tuple[type, ...]", (BaseGeneric,)),
        )
        == int
    )


def test_extract_type_var_multiple() -> None:
    typ = BaseGenericMultipleTypeArgs[int, str, None]

    generic_bases = cast("tuple[type, ...]", (BaseGenericMultipleTypeArgs,))
    assert extract_type_var_from_base(typ, index=0, generic_bases=generic_bases) == int
    assert extract_type_var_from_base(typ, index=1, generic_bases=generic_bases) == str
    assert extract_type_var_from_base(typ, index=2, generic_bases=generic_bases) == type(None)


def test_extract_type_var_generic_subclass_multiple() -> None:
    typ = SubclassGenericMultipleTypeArgs[int, str, None]

    generic_bases = cast("tuple[type, ...]", (BaseGenericMultipleTypeArgs,))
    assert extract_type_var_from_base(typ, index=0, generic_bases=generic_bases) == int
    assert extract_type_var_from_base(typ, index=1, generic_bases=generic_bases) == str
    assert extract_type_var_from_base(typ, index=2, generic_bases=generic_bases) == type(None)


def test_extract_type_var_generic_subclass_different_ordering_multiple() -> None:
    typ = SubclassDifferentOrderGenericMultipleTypeArgs[int, str, None]

    generic_bases = cast("tuple[type, ...]", (BaseGenericMultipleTypeArgs,))
    assert extract_type_var_from_base(typ, index=0, generic_bases=generic_bases) == int
    assert extract_type_var_from_base(typ, index=1, generic_bases=generic_bases) == str
    assert extract_type_var_from_base(typ, index=2, generic_bases=generic_bases) == type(None)
