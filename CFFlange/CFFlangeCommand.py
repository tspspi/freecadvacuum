import FreeCAD
from FreeCAD import Qt
import FreeCADGui

import Part
from . import CFFlange
from . import CFFlangeViewProvider
import math
import sys

import os

class CommandCFFlange:
	def GetResources(self):
		return {
			'MenuText': Qt.QT_TRANSLATE_NOOP("Part_CFFlange","Create CF flange"),
			'Accel': "",
			'CmdType': "AlterDoc:Alter3DView:AlterSelection",
			'Pixmap': os.path.join(os.path.dirname(os.path.abspath(__file__)), "flange.svg"),
			'ToolTip': Qt.QT_TRANSLATE_NOOP("Part_CFFlange","Creates a conflat flange")
		}

	def Activated(self):
		text = FreeCAD.Qt.translate("QObject", "Create CF flange")
		FreeCAD.ActiveDocument.openTransaction(text)

		flange = FreeCAD.ActiveDocument.addObject("Part::FeaturePython","CFFlange")
		CFFlange.ConflatFlange(flange)

		vp = CFFlangeViewProvider.CFFlangeViewProvider(flange.ViewObject)
		activePart = FreeCADGui.activeView().getActiveObject('part')

		if activePart:
			activePart.addObject(flange)

		FreeCAD.ActiveDocument.recompute()

		vp.startDefaultEditMode(flange.ViewObject)

	def IsActive(self):
		return not FreeCAD.ActiveDocument is None

FreeCADGui.addCommand('Part_CFFlange', CommandCFFlange())
