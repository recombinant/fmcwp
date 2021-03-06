#
# coding: utf-8
#
# fmxml.commands.dup_command
#
from .base_command import BaseCommand
from .mixins import RecordIdMixin


class DupCommand(RecordIdMixin, BaseCommand):
    """
    –dup (Duplicate record) query command
    """

    def __init__(self, fms, layout_name, record_id=None):
        super().__init__(fms, layout_name)
        self.record_id = record_id  # property in RecordIdMixin

    def get_query(self):
        assert self.record_id is not None

        command_params = super().get_command_params()
        command_params['-dup'] = None
        return command_params.as_query()
