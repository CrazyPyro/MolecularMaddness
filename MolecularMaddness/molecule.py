import kivy
kivy.require('1.2.0')
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.uix.widget import Widget
#from kivy.utils import boundary

class Molecule(Widget):
	moleculetype = StringProperty("") #ObjectProperty(None)
	xtile = NumericProperty(0)
	ytile = NumericProperty(0)
	tile = ReferenceListProperty(xtile, ytile)

	def on_touch_down(self, touch):
		if not self.collide_point(*touch.pos):
			return False
		touch.ud['molecule_touch'] = True
		return True # Report event as handled.

	def on_touch_move(self, touch):
		if not 'molecule_touch' in touch.ud:
			return False
		if touch.x > self.right:
			touch.ud['moving'] = True
		else:
			self.y += touch.dy
			#self.pos = Vector(*self.velocity) + self.pos
			pass
		#if self.collide_widget(any other compatible molecules):
		return True # Report event as handled.


