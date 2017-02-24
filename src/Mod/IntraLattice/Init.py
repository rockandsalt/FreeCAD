# FreeCAD init script of the IntraLattice module
# (c) 2001 Juergen Riegel LGPL

FreeCAD.addImportType("STL Mesh (*.stl *.ast)", "Mesh")
FreeCAD.addImportType("IGES File(*.iges)","IGES")
FreeCAD.addImportType("STEP File (*.stp)", "Step")


FreeCAD.addExportType("STL Mesh (*.stl *.ast)", "Mesh")