import FreeCAD, Part, math
from FreeCAD import Vector, Placement, Rotation

class ConflatFlange:
	_cf_dimensions = {
		10 : { 'outsideDiameter' :  25.0, 'tubeMax' :  12.0, 'boltN' :  6, 'boltHoleDia' :  3.3, 'boltThreadM' :  3, 'boltIncl' : 0.50, 'boltCircle' :  17.6, 'boltPositionTolerance' : 0.1, 'sealRecess' :  13.5, 'knifeEdge' :  10.5, 'pipeConnectionDepth' :  3.0, 'setbackInnerRotateable' :    0, 'thickness' :  6.0 },
		16 : { 'outsideDiameter' :  33.8, 'tubeMax' :  19.4, 'boltN' :  6, 'boltHoleDia' :  4.4, 'boltThreadM' :  4, 'boltIncl' : 0.70, 'boltCircle' :  27.0, 'boltPositionTolerance' : 0.1, 'sealRecess' :  21.4, 'knifeEdge' :  18.3, 'pipeConnectionDepth' :  3.3, 'setbackInnerRotateable' :  5.9, 'thickness' :  7.0 },
		25 : { 'outsideDiameter' :  54.0, 'tubeMax' :  25.8, 'boltN' :  4, 'boltHoleDia' :  6.8, 'boltThreadM' :  6, 'boltIncl' : 1.00, 'boltCircle' :  41.3, 'boltPositionTolerance' : 0.2, 'sealRecess' :  33.0, 'knifeEdge' :  27.7, 'pipeConnectionDepth' :  4.3, 'setbackInnerRotateable' :  6.0, 'thickness' : 11.5 },
		40 : { 'outsideDiameter' :  69.9, 'tubeMax' :  44.5, 'boltN' :  6, 'boltHoleDia' :  6.8, 'boltThreadM' :  6, 'boltIncl' : 1.00, 'boltCircle' :  58.7, 'boltPositionTolerance' : 0.2, 'sealRecess' :  48.3, 'knifeEdge' :  41.9, 'pipeConnectionDepth' :  4.3, 'setbackInnerRotateable' :  7.7, 'thickness' : 12.5 },
		50 : { 'outsideDiameter' :  85.7, 'tubeMax' :  51.0, 'boltN' :  8, 'boltHoleDia' :  8.4, 'boltThreadM' :  8, 'boltIncl' : 1.25, 'boltCircle' :  72.4, 'boltPositionTolerance' : 0.2, 'sealRecess' :  61.8, 'knifeEdge' :  55.9, 'pipeConnectionDepth' :  4.9, 'setbackInnerRotateable' :  9.7, 'thickness' : 16.0 },
		63 : { 'outsideDiameter' : 114.3, 'tubeMax' :  70.0, 'boltN' :  8, 'boltHoleDia' :  8.4, 'boltThreadM' :  8, 'boltIncl' : 1.25, 'boltCircle' :  92.2, 'boltPositionTolerance' : 0.2, 'sealRecess' :  82.5, 'knifeEdge' :  77.2, 'pipeConnectionDepth' :  6.4, 'setbackInnerRotateable' : 12.7, 'thickness' : 17.0 },
		75 : { 'outsideDiameter' : 117.4, 'tubeMax' :  76.2, 'boltN' : 10, 'boltHoleDia' :  8.4, 'boltThreadM' :  8, 'boltIncl' : 1.25, 'boltCircle' : 102.3, 'boltPositionTolerance' : 0.2, 'sealRecess' :  91.6, 'knifeEdge' :  85.2, 'pipeConnectionDepth' :  6.5, 'setbackInnerRotateable' : 13.0, 'thickness' : 17.5 },
		100: { 'outsideDiameter' : 152.4, 'tubeMax' : 108.0, 'boltN' : 16, 'boltHoleDia' :  8.4, 'boltThreadM' :  8, 'boltIncl' : 1.25, 'boltCircle' : 130.3, 'boltPositionTolerance' : 0.2, 'sealRecess' : 120.6, 'knifeEdge' : 115.3, 'pipeConnectionDepth' :  7.2, 'setbackInnerRotateable' : 14.3, 'thickness' : 19.5 },
		125: { 'outsideDiameter' : 171.5, 'tubeMax' : 127.0, 'boltN' : 18, 'boltHoleDia' :  8.4, 'boltThreadM' :  8, 'boltIncl' : 1.25, 'boltCircle' : 151.6, 'boltPositionTolerance' : 0.2, 'sealRecess' : 141.8, 'knifeEdge' : 136.3, 'pipeConnectionDepth' :  7.2, 'setbackInnerRotateable' : 14.3, 'thickness' : 21.0 },
		160: { 'outsideDiameter' : 203.2, 'tubeMax' : 159.0, 'boltN' : 20, 'boltHoleDia' :  8.4, 'boltThreadM' :  8, 'boltIncl' : 1.25, 'boltCircle' : 181.0, 'boltPositionTolerance' : 0.2, 'sealRecess' : 171.4, 'knifeEdge' : 166.1, 'pipeConnectionDepth' :  8.0, 'setbackInnerRotateable' : 15.9, 'thickness' : 21.0 },
		200: { 'outsideDiameter' : 254.0, 'tubeMax' : 206.0, 'boltN' : 24, 'boltHoleDia' :  8.3, 'boltThreadM' :  8, 'boltIncl' : 1.25, 'boltCircle' : 231.8, 'boltPositionTolerance' : 0.2, 'sealRecess' : 222.2, 'knifeEdge' : 216.9, 'pipeConnectionDepth' :  8.6, 'setbackInnerRotateable' : 17.2, 'thickness' : 24.0 },
		250: { 'outsideDiameter' : 304.8, 'tubeMax' : 256.0, 'boltN' : 32, 'boltHoleDia' :  8.4, 'boltThreadM' :  8, 'boltIncl' : 1.25, 'boltCircle' : 284.0, 'boltPositionTolerance' : 0.2, 'sealRecess' : 273.1, 'knifeEdge' : 267.5, 'pipeConnectionDepth' :  9.0, 'setbackInnerRotateable' : 18.0, 'thickness' : 24.0 },
		275: { 'outsideDiameter' : 336.6, 'tubeMax' : 273.0, 'boltN' : 30, 'boltHoleDia' : 10.8, 'boltThreadM' : 10, 'boltIncl' : 1.50, 'boltCircle' : 306.3, 'boltPositionTolerance' : 0.2, 'sealRecess' : 294.4, 'knifeEdge' : 288.2, 'pipeConnectionDepth' :  9.9, 'setbackInnerRotateable' : 19.8, 'thickness' : 28.0 },
		300: { 'outsideDiameter' : 368.3, 'tubeMax' : 306.0, 'boltN' : 32, 'boltHoleDia' : 10.8, 'boltThreadM' : 10, 'boltIncl' : 1.50, 'boltCircle' : 338.1, 'boltPositionTolerance' : 0.2, 'sealRecess' : 326.4, 'knifeEdge' : 320.0, 'pipeConnectionDepth' :  9.9, 'setbackInnerRotateable' : 19.8, 'thickness' : 28.0 },
		350: { 'outsideDiameter' : 419.1, 'tubeMax' : 356.0, 'boltN' : 36, 'boltHoleDia' : 10.8, 'boltThreadM' : 10, 'boltIncl' : 1.50, 'boltCircle' : 388.9, 'boltPositionTolerance' : 0.4, 'sealRecess' : 376.7, 'knifeEdge' : 373.0, 'pipeConnectionDepth' : 10.4, 'setbackInnerRotateable' : 20.7, 'thickness' : 28.0 },
		400: { 'outsideDiameter' : 469.9, 'tubeMax' : 406.0, 'boltN' : 40, 'boltHoleDia' : 10.8, 'boltThreadM' : 10, 'boltIncl' : 1.50, 'boltCircle' : 437.9, 'boltPositionTolerance' : 0.4, 'sealRecess' : 424.4, 'knifeEdge' : 419.0, 'pipeConnectionDepth' : 10.4, 'setbackInnerRotateable' : 20.7, 'thickness' : 28.0 }
	}
	_myprops = [
		"cf",
		#"rotateable",
		#"rotateableOutside",
		"pipeDiameter",
		"pipeWallWidth",
		"boltThrough"
	]

	def __init__(self, obj):
		obj.addProperty("App::PropertyEnumeration", "cf", "Conflat flange diameter", "Normed diameter value").cf = [ "10", "16", "25", "40", "50", "63", "75", "100", "125", "160", "200", "250", "275", "300", "350", "400" ]

		#obj.addProperty("App::PropertyBool", "rotateable", "Conflat flange", "Set if the flange should be rotateable").rotateable = False
		#obj.addProperty("App::PropertyBool", "rotateableOutside", "Conflat flange", "Set if we should infer the outside side of the rotateable flange").rotateableOutside = False
		obj.addProperty("App::PropertyFloat", "pipeDiameter", "Pipe", "The pipe diameter").pipeDiameter = -1
		obj.addProperty("App::PropertyFloat", "pipeWallWidth", "Pipe", "The pipe wall width").pipeWallWidth = 2.5
		obj.addProperty("App::PropertyBool", "boltThrough", "Conflat flange", "Should bolt holes be through holes?").boltThrough = True

		obj.Proxy = self

	def onChanged(self, fp, prop):
		if prop in self._myprops:
			self.execute(fp)

	def _rotate_placement(self, origin, direction, angle):
		OZ = Vector(0,0,1)
		map_to_local = Placement(origin, Rotation(OZ, direction))
		map_to_global = map_to_local.inverse()

		global_rotate = Placement(Vector(0,0,0), Rotation(angle,0,0))

		return map_to_local.multiply(global_rotate.multiply(map_to_global))

	def _CylinderCenter(self, r, h, position = None):
		if position is not None:
			return Part.makeCylinder(r, h, Vector(0, 0, -h/2).add(position))
		else:
			return Part.makeCylinder(r, h, Vector(0, 0, -h/2))

	def _ConeCenter(self, r1, r2, h, position = None):
		if position is not None:
			return Part.makeCone(r1, r2, h, Vector(0, 0, -h/2).add(position))
		else:
			return Part.makeCone(r1, r2, h, Vector(0, 0, -h/2))

	def _BoxCenter(self, x, y, z, position = None):
		if position is not None:
			return Part.makeBox(x,y,z, Vector(-x/2, -y/2, -z/2).add(position))
		else:
			return Part.makeBox(x,y,z, Vector(-x/2, -y/2, -z/2))

	def execute(self, fp):
		if ((fp.pipeWallWidth*2) >= fp.pipeDiameter) and (fp.pipeDiameter > 0):
			raise ValueError("Pipe wall width is too large for specified pipe diameter")

		# First select parameters ....
		pars = self._cf_dimensions[int(fp.cf)]

		# Base blank
		flange = self._CylinderCenter(pars['outsideDiameter'] / 2.0, pars['thickness'], Vector(0,0,pars['pipeConnectionDepth'] - pars['thickness'] / 2))

		# Hole for pipe
		if fp.pipeDiameter > 0:
			pipeInset = pars['thickness'] - pars['pipeConnectionDepth']

			flange = flange.cut(
				self._CylinderCenter((fp.pipeDiameter - 2 * fp.pipeWallWidth) / 2.0, pars['thickness'], Vector(0,0,pars['pipeConnectionDepth'] - pars['thickness']/2))
			)
			flange = flange.cut(
				self._CylinderCenter(fp.pipeDiameter / 2.0, pipeInset, Vector(0,0,-pipeInset/2))
			)

		# Seal recess and area where knife edge will be cut
		flange = flange.cut(
			self._CylinderCenter(pars['knifeEdge']/2, 1.2, Vector(0,0,-0.6 + pars['pipeConnectionDepth']))
		)
		flange = flange.cut(
			self._CylinderCenter(pars['sealRecess']/2, 0.89, Vector(0,0,-0.89/2.0 + pars['pipeConnectionDepth']))
		)

		# Knife edge
		kfwidth = (pars['sealRecess'] - pars['knifeEdge']) / 2.0
		kfheight = math.tan(20 * math.pi / 180) * kfwidth
		knife = self._CylinderCenter(pars['sealRecess'] / 2, kfheight, Vector(0,0,-0.98 - kfheight / 2.0 + pars['pipeConnectionDepth']))
		knife = knife.cut(self._ConeCenter(pars['sealRecess'] / 2, pars['knifeEdge'] / 2, kfheight, Vector(0,0,-0.98 - kfheight / 2.0 + pars['pipeConnectionDepth'])))
		flange = flange.cut(knife)

		# Screw holes
		for iHole in range(pars['boltN']):
			currentAngle = (360.0 / pars['boltN']) * iHole
			if fp.boltThrough:
				newHole = self._CylinderCenter(pars['boltHoleDia']/2.0, pars['thickness'], Vector(pars['boltCircle']/2.0, 0, pars['pipeConnectionDepth'] - pars['thickness']/2.0))
				r = self._rotate_placement(Vector(0,0,0), Vector(0,0,1), currentAngle)
				newHole.Placement = r.multiply(newHole.Placement)
				flange = flange.cut(newHole)
			else:
				newHole = self._CylinderCenter(pars['boltHoleDia']/2.0, pars['thickness']/2.0, Vector(pars['boltCircle']/2.0, 0, pars['pipeConnectionDepth'] - 1.0*pars['thickness']/4.0))
				r = self._rotate_placement(Vector(0,0,0), Vector(0,0,1), currentAngle)
				newHole.Placement = r.multiply(newHole.Placement)
				flange = flange.cut(newHole)

		# Leak checking grooves
		grove01 = self._BoxCenter((pars['outsideDiameter'] - pars['sealRecess']) / 2.0 + 3, 1.5, 1.5, Vector(pars['outsideDiameter'] / 2 - (pars['outsideDiameter'] - pars['sealRecess'])/4, 0, pars['pipeConnectionDepth']))
		groov01r = self._rotate_placement(Vector(0,0,0), Vector(0,0,1), 180 / pars['boltN'])
		grove01.Placement = groov01r.multiply(grove01.Placement)
		grove02 = self._BoxCenter((pars['outsideDiameter'] - pars['sealRecess']) / 2.0 + 3, 1.5, 1.5, Vector(pars['outsideDiameter'] / 2 - (pars['outsideDiameter'] - pars['sealRecess'])/4, 0, pars['pipeConnectionDepth']))
		groov02r = self._rotate_placement(Vector(0,0,0), Vector(0,0,1), 180 / pars['boltN'] + 180)
		grove02.Placement = groov02r.multiply(grove02.Placement)
		flange = flange.cut(grove01)
		flange = flange.cut(grove02)

		fp.Shape = flange

	@staticmethod
	def makeFlange(name = "CFFlange"):
		obj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", name)
		ConflatFlange(obj)
		if FreeCAD.GuiUp:
			from .CFFlangeViewProvider import CFFlangeViewProvider
			CFFlangeViewProvider(obj.ViewObject)
		else:
			obj.ViewObject.Proxy=0

		FreeCAD.ActiveDocument.recompute()
