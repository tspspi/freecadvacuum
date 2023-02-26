import os
import FreeCAD
import FreeCADGui

from PySide import QtGui

class CFFlangeViewProvider:
	def __init__(self, obj):
		obj.addExtension("PartGui::ViewProviderAttachExtensionPython")
		obj.setIgnoreOverlayIcon(True, "PartGui::ViewProviderAttachExtensionPython")
		obj.Proxy = self

	def attach(self, obj):
		return

	def setupContextMenu(self, viewObject, menu):
		action = menu.addAction(FreeCAD.Qt.translate("QObject", "Edit %1").replace("%1", viewObject.Object.Label))
		action.triggered.connect(lambda: self.startDefaultEditMode(viewObject))
		return False

	def startDefaultEditMode(self, viewObject):
		document = viewObject.Document.Document
		if not document.HasPendingTransaction:
			text = FreeCAD.Qt.translate("QObject", "Edit %1").replace("%1", viewObject.Object.Label)
			document.openTransaction(text)
		viewObject.Document.setEdit(viewObject.Object, 0)

	def setEdit(self, viewObject, mode):
		if mode == 0:
			FreeCADGui.Control.showDialog(TaskCFFlangeUI(viewObject))
			return True

	def unsetEdit(self, viewObject, mode):
		if mode == 0:
			FreeCADGui.Control.closeDialog()
			return True

	def getIcon(self):
		# return ":/icons/parametric/Part_Tube_Parametric.svg"
		return None

	def __getstate__(self):
		return None

	def __setstate__(self,state):
		return None

class TaskCFFlangeUI:
	def __init__(self, viewObject):
		self.viewObject = viewObject
		ui_file = os.path.join(os.path.dirname(__file__), "TaskCFFlange.ui")
		ui = FreeCADGui.UiLoader()
		self.form = ui.load(ui_file)

		object = self.viewObject.Object
		self.form.cf.setProperty("rawValue", object.cf)
		#self.form.rotateable.setProperty("rawValue", object.rotateable.Value)
		#self.form.rotateableOutside.setProperty("rawValue", object.rotateableOutside.Value)
		self.form.pipeDiameter.setProperty("rawValue", object.pipeDiameter)
		self.form.pipeWallWidth.setProperty("rawValue", object.pipeWallWidth)
		#self.form.boltThrough.setProperty("rawValue", object.boltThrough)

		self.form.cf.valueChanged.connect(lambda x : self.onChangeCF(x))
		#self.form.rotateable.valueChanged.connect(lambda x : self.onChangeRotateable(x))
		#self.form.rotateableOutside.valueChanged.connect(lambda x : self.onChangeRotateableOutside(x))
		self.form.pipeDiameter.valueChanged.connect(lambda x : self.onChangePipeDiameter(x))
		self.form.pipeWallWidth.valueChanged.connect(lambda x : self.onChangePipeWallWidth(x))
		#self.form.boltThrough.valueChanged.connect(lambda x : self.onChangeBoltThrough(x))

		FreeCADGui.ExpressionBinding(self.form.cf).bind(object,"cf")
		#FreeCADGui.ExpressionBinding(self.form.rotateable).bind(object,"rotateable")
		#FreeCADGui.ExpressionBinding(self.form.rotateableOutside).bind(object,"rotateableOutside")
		FreeCADGui.ExpressionBinding(self.form.pipeDiameter).bind(object,"pipeDiameter")
		FreeCADGui.ExpressionBinding(self.form.pipeWallWidth).bind(object,"pipeWallWidth")
		#FreeCADGui.ExpressionBinding(self.form.boltThrough).bind(object,"boltThrough")

	def onChangeCF(self, newcf):
		obj = self.viewObject.Object
		obj.cf = newcf
		obj.recompute()

	#def onChangeRotateable(self, newrotateable):
	#	obj = self.viewObject.Object
	#	obj.rotateable = newrotateable
	#	obj.recompute()

	#def onChangeRotateableOutside(self, newrotateableOutside):
	#	obj = self.viewObject.Object
	#	obj.rotateableOutside = newrotateableOutside
	#	obj.recompute()

	def onChangePipeDiameter(self, newpipediameter):
		obj = self.viewObject.Object
		obj.pipeDiameter = newnewpipediameter
		obj.recompute()

	def onChangePipeWallWidth(self, newpipewallwidth):
		obj = self.viewObject.Object
		obj.pipeWallWidth = newpipewallwidth
		obj.recompute()

	def onChangeBoltThrough(self, newboltthrough):
		obj = self.viewObject.Object
		obj.boltThrough = newboltthrough
		obj.recompute()

	def accept(self):
		object = self.viewObject.Object
		if not object.isValid():
			QtGui.QMessageBox.warning(None, "Error", object.getStatusString())
			return False
		document = self.viewObject.Document.Document
		document.commitTransaction()
		document.recompute()
		self.viewObject.Document.resetEdit()
		return True

	def reject(self):
		guidocument = self.viewObject.Document
		document = guidocument.Document
		document.abortTransaction()
		document.recompute()
		guidocument.resetEdit()
		return True
