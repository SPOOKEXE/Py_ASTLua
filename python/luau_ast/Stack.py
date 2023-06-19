
class Stack:
	Parent = None
	StackHistory = None
	LocalVars = { }
	StackVars = { }

	def get_vars(self) -> dict:
		return self.StackVars.copy().update( self.LocalVars.copy() )

	def set_loc_var(self, varName : str, varType : str, iterStep=0 ) -> None:
		if self.StackHistory != None:
			self.StackHistory.append( [ iterStep, self.LocalVars.copy() ] )
		self.LocalVars.update({ varName : varType })

	def pop_loc_var(self, varName : str, iterStep=0 ) -> str:
		if self.StackHistory != None:
			self.StackHistory.append( [ iterStep, self.LocalVars.copy() ] )
		return self.LocalVars.pop(varName)

	def set_global_var(self, varName : str, varType : str, iterStep=0 ) -> None:
		if self.StackHistory != None:
			self.StackHistory.append( [ iterStep, self.StackVars.copy() ] )
		return self.StackVars.update({ varName : varType })

	def pop_global_var(self, varName : str, iterStep=0 ) -> None:
		if self.StackHistory != None:
			self.StackHistory.append( [ iterStep, self.StackVars.copy() ] )
		return self.StackVars.pop(varName)

	def __init__(self, Parent=None, StackHistory=None):
		self.StackHistory = StackHistory
		if Parent != None:
			self.StackVars = Parent.get_vars()
