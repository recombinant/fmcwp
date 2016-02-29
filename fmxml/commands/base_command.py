# -*- mode: python tab-width: 4 coding: utf-8 -*-
from .command_container import CommandContainer, Command
from ..parsers.data_grammar import DataGrammarParser
from ..structure.command_result import CommandResult


class BaseCommand:
    """
    Base for command classes.

    This class must be on the right of any mixins so that it is at the end of
    the mro."""
    __slots__ = ('__fms', '__layout_name', )

    def __init__(self, fms, layout_name):
        assert fms
        assert layout_name
        assert isinstance(layout_name, str)
        self.__fms = fms
        self.__layout_name = layout_name

    def get_command_params(self):
        db = self.__fms.get_property('db')
        assert db
        command_params = CommandContainer(
            Command('-db', db),
            Command('-lay', self.__layout_name),
        )
        return command_params

    def execute(self):
        xml_bytes = self.__fms._execute(self.get_query())
        assert xml_bytes

        parsed_data = DataGrammarParser().parse(xml_bytes)
        # populate result
        return CommandResult(self.__fms, parsed_data)