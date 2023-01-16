from _typeshed import Incomplete
from typing import Any
from typing_extensions import TypeAlias

from astropy.units.equivalencies import Equivalency
from astropy.utils.exceptions import AstropyWarning

_Equivalences: TypeAlias = list[Equivalency]
_Aliases: TypeAlias = dict[str, UnitBase]

class _UnitRegistry:  # undocumented
    def __init__(self, init=..., equivalencies: _Equivalences = ..., aliases: _Aliases = ...) -> None: ...
    @property
    def registry(self): ...
    @property
    def all_units(self) -> set[UnitBase]: ...
    @property
    def non_prefix_units(self) -> set[UnitBase]: ...
    def set_enabled_units(self, units) -> None: ...
    def add_enabled_units(self, units) -> None: ...
    def get_units_with_physical_type(self, unit): ...
    @property
    def equivalencies(self) -> _Equivalences: ...
    def set_enabled_equivalencies(self, equivalencies: _Equivalences) -> None: ...
    def add_enabled_equivalencies(self, equivalencies: _Equivalences) -> None: ...
    @property
    def aliases(self) -> _Aliases: ...
    def set_enabled_aliases(self, aliases: _Aliases) -> None: ...
    def add_enabled_aliases(self, aliases: _Aliases) -> None: ...

class _UnitContext:  # undocumented
    def __init__(self, init=..., equivalencies: _Equivalences = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: object, value: object, tb: object) -> None: ...

def get_current_unit_registry() -> _UnitRegistry: ...
def set_enabled_units(units) -> _UnitContext: ...
def add_enabled_units(units) -> _UnitContext: ...
def set_enabled_equivalencies(equivalencies: _Equivalences) -> _UnitContext: ...
def add_enabled_equivalencies(equivalencies: _Equivalences) -> _UnitContext: ...
def set_enabled_aliases(aliases: _Aliases) -> _UnitContext: ...
def add_enabled_aliases(aliases: _Aliases) -> _UnitContext: ...

class UnitsError(Exception): ...
class UnitScaleError(UnitsError, ValueError): ...
class UnitConversionError(UnitsError, ValueError): ...
class UnitTypeError(UnitsError, TypeError): ...
class UnitsWarning(AstropyWarning): ...

class UnitBase:
    __array_priority__: int
    def __deepcopy__(self, memo: Any) -> UnitBase: ...
    def __bytes__(self) -> bytes: ...
    @property
    def names(self) -> None: ...
    @property
    def name(self) -> None: ...
    @property
    def aliases(self) -> None | list[str]: ...
    @property
    def scale(self) -> float: ...
    @property
    def bases(self) -> list[UnitBase]: ...
    @property
    def powers(self) -> list[float]: ...
    def to_string(self, format=...): ...
    def __format__(self, format_spec) -> str: ...
    def __pow__(self, p: float) -> CompositeUnit: ...
    def __truediv__(self, m: Any): ...
    def __rtruediv__(self, m: Any): ...
    def __mul__(self, m: Any): ...
    def __rmul__(self, m: Any): ...
    def __rlshift__(self, m: Any): ...
    def __rrshift__(self, m: Any): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __neg__(self) -> UnitBase: ...
    def is_equivalent(self, other, equivalencies: _Equivalences = ...) -> bool: ...
    def to(self, other, value: float = ..., equivalencies: _Equivalences = ...): ...
    def in_units(self, other, value: float = ..., equivalencies: _Equivalences = ...): ...
    def decompose(self, bases: set[UnitBase] = ...) -> None: ...
    def compose(
        self,
        equivalencies: _Equivalences = ...,
        units: Incomplete | None = ...,
        max_depth: int = ...,
        include_prefix_units: bool | None = ...,
    ): ...
    def to_system(self, system): ...
    @property
    def si(self): ...
    @property
    def cgs(self): ...
    @property
    def physical_type(self): ...

    class EquivalentUnitsList(list[UnitBase]):  # noqa: F821
        HEADING_NAMES: Incomplete
        ROW_LEN: int
        NO_EQUIV_UNITS_MSG: str
    def find_equivalent_units(
        self, equivalencies: _Equivalences = ..., units: Incomplete | None = ..., include_prefix_units: bool = ...
    ): ...
    def is_unity(self): ...

class NamedUnit(UnitBase):
    __doc__: Incomplete
    def __init__(
        self, st, doc: Incomplete | None = ..., format: Incomplete | None = ..., namespace: Incomplete | None = ...
    ) -> None: ...
    def get_format_name(self, format): ...
    @property
    def names(self): ...
    @property
    def name(self): ...
    @property
    def aliases(self) -> list[str]: ...
    @property
    def short_names(self): ...
    @property
    def long_names(self): ...

class IrreducibleUnit(NamedUnit):
    def __reduce__(self): ...
    @property
    def represents(self): ...
    def decompose(self, bases=...): ...

class UnrecognizedUnit(IrreducibleUnit):
    __reduce__: Incomplete
    def __bytes__(self) -> bytes: ...
    def to_string(self, format: Incomplete | None = ...): ...
    __pow__: Incomplete
    __truediv__: Incomplete
    __rtruediv__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    __lt__: Incomplete
    __gt__: Incomplete
    __le__: Incomplete
    __ge__: Incomplete
    __neg__: Incomplete
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def is_equivalent(self, other, equivalencies: _Equivalences | None = ...): ...
    def get_format_name(self, format): ...
    def is_unity(self): ...

class _UnitMetaClass(type):
    def __call__(
        self,
        s: str = ...,
        represents: Incomplete | None = ...,
        format: Incomplete | None = ...,
        namespace: Incomplete | None = ...,
        doc: Incomplete | None = ...,
        parse_strict: str = ...,
    ): ...

class Unit(NamedUnit, metaclass=_UnitMetaClass):
    def __init__(
        self,
        st,
        represents: Incomplete | None = ...,
        doc: Incomplete | None = ...,
        format: Incomplete | None = ...,
        namespace: Incomplete | None = ...,
    ) -> None: ...
    @property
    def represents(self): ...
    def decompose(self, bases=...): ...
    def is_unity(self): ...
    def __hash__(self): ...

class PrefixUnit(Unit): ...

class CompositeUnit(UnitBase):
    def __init__(self, scale, bases, powers, decompose: bool = ..., decompose_bases=..., _error_check: bool = ...) -> None: ...
    @property
    def scale(self): ...
    @property
    def bases(self): ...
    @property
    def powers(self): ...
    def __copy__(self): ...
    def decompose(self, bases=...): ...
    def is_unity(self): ...

def def_unit(
    s,
    represents: Incomplete | None = ...,
    doc: Incomplete | None = ...,
    format: Incomplete | None = ...,
    prefixes: bool = ...,
    exclude_prefixes=...,
    namespace: Incomplete | None = ...,
): ...

dimensionless_unscaled: Incomplete = ...
one = dimensionless_unscaled
