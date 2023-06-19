
class ChunkTypeEnum:
	Unknown = 0
	VariableDefinition = 1
	VariableAssignment = 2
	VariableMathAssignment = 3

class Chunk:
	ID : str = "-1"
	Type = ChunkTypeEnum.Unknown

class ExpressionStatement(Chunk):
	Expression = None
	def __init__(self):
		super().__init__(self)

