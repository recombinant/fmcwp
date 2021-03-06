#
# coding: utf-8
#
# Stubs for fmxml.structure.record
#
from typing import List, Any, Optional, Dict

from . import field_container as field_container_module
from . import layout as layout_module
from . import portal as portal_module
from .. import fms as fms_module


class Record:
    _fms: fms_module.FileMakerServer
    _layout: layout_module.Layout
    _record_id: int
    _modification_id: int
    _field_container: field_container_module.FieldContainer
    _portal_records: Dict[str, List[portal_module.Portal]]
    _parent_record: Optional[Record]
    _portal_name: str

    def __init__(self,
                 layout: layout_module.Layout,
                 field_container: Optional[field_container_module.FieldContainer] = None) \
            -> None:
        ...

    @property
    def layout(self) -> layout_module.Layout:
        ...

    @property
    def field_names(self) -> List[str]:
        ...

    def _get_modification_id(self) -> Optional[None]:
        ...

    def _set_modification_id(self, modification_id: int) -> None:
        ...

    modification_id: int = ...

    def _get_record_id(self) -> int:
        ...

    def _set_record_id(self, record_id: int) -> None:
        ...

    record_id: int = ...

    @property
    def portal_table_names(self) -> List[str]:
        ...

    def add_portal_record_(self,
                           table_name: str,
                           portal_record: Record) \
            -> None:
        ...

    @property
    def parent(self) -> Optional[Record]:
        ...

    def get_field_value(self, field_name: str, repetition_number: int = 0) -> Any:
        ...

    def get_field_values(self, field_name: str) -> List[Any]:
        ...

    def delete(self) -> None:
        ...

    def duplicate(self) -> Record:
        ...
