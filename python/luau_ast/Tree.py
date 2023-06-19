
from os import path as os_path
from sys import path as sys_path

FILE_DIRECTORY = os_path.dirname(os_path.realpath(__file__))

sys_path.append( os_path.join(FILE_DIRECTORY, "..") )

from luau_ast.Chunk import Chunk, ChunkTypeEnum
from luau_ast.Stack import Stack
from luau_ast.Types import VariableTypes, RobloxVariableTypes

sys_path.pop()

class Tree:

	_source = None

	def _get_source(self) -> str:
		assert self._source, "You must parse a .lua file."
		return self._source

	def _build_from_source( self, source : str ) -> None:
		self._source = source
		print(source)

	def __init__(self):
		pass
