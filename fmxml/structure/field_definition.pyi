#
# coding: utf-8
#
# Stubs for fmxml.structure.field_definition
#
from typing import Set, Optional, Any

from . import layout as layout_module
from . import portal as portal_module
from . import valuelist as valuelist_module
from ..parsers import data_grammar as data_grammar_module

RESULT_TEXT: str = ...
RESULT_NUMBER: str = ...
RESULT_DATE: str = ...
RESULT_TIME: str = ...
RESULT_TIMESTAMP: str = ...
RESULT_CONTAINER: str = ...
RESULT_UNKNOWN: str = ...

KNOWN_TYPES: Set[str] = ...
KNOWN_RESULTS: Set[str] = ...


class FieldDefinition:
    _layout: layout_module.Layout
    _field_name: str
    _portal: str
    _auto_entered: bool
    _global: bool
    _not_empty: bool
    _numeric_only: bool
    _four_digit_year: bool
    _time_of_day: bool
    _max_repetitions: int
    _valuelist_name: Optional[str]
    _max_characters: int
    _type: str
    _result: str

    def __init__(self,
                 layout: layout_module.Layout,
                 raw_field_definition: data_grammar_module.RawFieldDefinition,
                 portal: Optional[portal_module.Portal] = None) \
            -> None:
        ...

    @property
    def field_name(self) -> str:
        ...

    @property
    def layout(self) -> layout_module.Layout:
        ...

    def munge_value(self, value: Optional[str]) -> Any:
        ...

    def set_valuelist_name_(self, valuelist_name: str) -> None:
        ...

    def get_valuelist(self) -> valuelist_module.Valuelist:
        ...
