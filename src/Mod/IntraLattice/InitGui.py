



 class DrawingWorkbench (Workbench):
    "Intralattice workbench object"
    def __init__(self):
        self.__class__.Icon = FreeCAD.getResourceDir() + "Mod/IntraLattice/Resources/icons/IntraLatticeWorkbench.svg"
        self.__class__.MenuText = "IntraLattice"
        self.__class__.ToolTip = "IntraLattice workbench"


    def Initialize(self):
        # load the module
        import DrawingGui
    def GetClassName(self):
        return "DrawingGui::Workbench"
        
Gui.addWorkbench(DrawingWorkbench())