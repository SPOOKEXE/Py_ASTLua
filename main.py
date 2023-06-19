from os import path as os_path

from python.luau_ast.AST import AST

FILE_DIRECTORY = os_path.dirname(os_path.realpath(__file__))

if __name__ == '__main__':
	in_filepath = os_path.join( FILE_DIRECTORY, "in.lua" )
	out_filepath = os_path.join( FILE_DIRECTORY, "out.lua" )

	# TODO: check for errors using 'luau-analyze.exe'

	# build the AST tree from the file
	with open(in_filepath, "r") as file:
		tree = AST.parse( file.read() )

	# stringify the ast tree
	dump_str = AST.stringify( tree )

	# write to file
	with open(out_filepath, "w") as file:
		file.write( dump_str )
