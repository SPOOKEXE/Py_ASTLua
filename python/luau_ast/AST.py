
#from re import escape as re_escape

from os import path as os_path
from sys import path as sys_path

FILE_DIRECTORY = os_path.dirname(os_path.realpath(__file__))

sys_path.append( os_path.join(FILE_DIRECTORY, "..") )

from luau_ast.Tree import Tree

sys_path.pop()

COMMENT_START_ENDERS = {
	"--[==[" : "]==]",
	"--[[" : "]]",
	"--" : "\n",
}

class AST:
	@staticmethod
	def _cleanup_source( source : str ) -> str:
		def find_start_finish( nsource, index ) -> tuple[int, int]:
			for starter, finisher in COMMENT_START_ENDERS.items():
				comment_start = nsource.find(starter, index)
				if comment_start != -1:
					print(starter, finisher)
					return comment_start, finisher
			return -1, -1

		index = 0
		while index < len(source):
			comment_start, comment_finish = find_start_finish( source, index )
			if comment_start == -1:
				break
			line_finish = source.find(comment_finish, comment_start)
			print( comment_start, line_finish )
			if line_finish == -1:
				line_finish = len(source)
			else:
				line_finish = line_finish + len(comment_finish)
			print( source[comment_start : line_finish] )
			source = source[ : comment_start] + source[ line_finish : len(source) ]
			index = comment_start + 1
		return source

	@staticmethod
	def parse( source : str ) -> Tree:
		_source = AST._cleanup_source( source )
		tree = Tree()
		tree._build_from_source(_source)
		return tree

	@staticmethod
	def stringify( tree : Tree ) -> str:
		return tree._get_source()
