# Vacuum parts library for FreeCAD

This is a (__work in progress__) vacuum parts library for FreeCAD. It adds
a new toolbar to FreeCAD that allows one to generate various standard shapes.

__Work in progress__: Really new experimental stuff, my first FreeCAD extension.

Currently it includes support for:

* Conflat flanges (16-400)
   * Note that this is currently not automatically loaded even when included
	   in the ```Mod``` directory and has to be imported using ```import CFFlange```
		 manually. Then the toolbar also has to be generated manually at this point
		 in time.
	 * Currently the UI file lacks stuff and logic - the property dialog works
	   on the other hand ...
   * This is based on my [JSCAD implementation](https://github.com/tspspi/jscadModels/blob/master/library/mechanics/cfflange.jscad)
	 * Currently no attachment points, etc. - work in progress

![Conflat flanges](https://raw.githubusercontent.com/tspspi/freecadvacuum/master/doc/screenshot01.png)
![Conflat flanges](https://raw.githubusercontent.com/tspspi/freecadvacuum/master/doc/screenshot02.png)
![Conflat flanges](https://raw.githubusercontent.com/tspspi/freecadvacuum/master/doc/screenshot03.png)
