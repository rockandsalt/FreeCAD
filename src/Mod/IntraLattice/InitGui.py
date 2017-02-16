# IntraLattice gui init module
# (c) 2001 Juergen Riegel LGPL

class IntraLatticeWorkbench ( Workbench ):
	"IntraLattice workbench object"
	MenuText = "IntraLattice"
	ToolTip = "IntraLattice workbench"
	def Initialize(self):
		# load the module
		import IntraLatticeGui
	def GetClassName(self):
		return "IntraLatticeGui::Workbench"

Gui.addWorkbench(IntraLatticeWorkbench())
