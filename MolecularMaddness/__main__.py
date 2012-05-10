import kivy
kivy.require('1.2.0')
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Point, GraphicException
from random import random
from math import sqrt


def calculate_points(x1, y1, x2, y2, steps=5):
	dx = x2 - x1
	dy = y2 - y1
	dist = sqrt(dx * dx + dy * dy)
	if dist < steps:
		return None
	o = []
	m = dist / steps
	for i in xrange(1, int(m)):
		mi = i / m
		lastx = x1 + dx * mi
		lasty = y1 + dy * mi
		o.extend([lastx, lasty])
	return o

class MainWindow(FloatLayout):

	def update(self, *args):
		"""Called in between frames to update game state."""
		return True

	def button_pressed(self):
		return

	def on_touch_down(self, touch):
		"""On touch/click"""
		win = self.get_parent_window()
		ud = touch.ud # touch.ud is a user-defined data object, persistent for the duration of this touch.
		ud['group'] = g = str(touch.uid)
		with self.canvas:
			ud['color'] = Color(random(), 1, 1, mode='hsv', group=g)
			ud['lines'] = (
				Rectangle(pos=(touch.x, 0), size=(1, win.height), group=g),
				Rectangle(pos=(0, touch.y), size=(win.width, 1), group=g),
				Point(points=(touch.x, touch.y), source='particle.png',
					  pointsize=5, group=g))

		ud['label'] = Label(size_hint=(None, None))
		self.update_touch_label(ud['label'], touch)
		self.add_widget(ud['label'])
		touch.grab(self)
		return True # Report event as handled.

	def on_touch_move(self, touch):
		"""Touch-swiping or mouse-dragging"""
		if touch.grab_current is not self:
			return
		ud = touch.ud
		ud['lines'][0].pos = touch.x, 0
		ud['lines'][1].pos = 0, touch.y

		points = ud['lines'][2].points
		oldx, oldy = points[-2], points[-1]
		points = calculate_points(oldx, oldy, touch.x, touch.y)
		if points:
			try:
				lp = ud['lines'][2].add_point
				for idx in xrange(0, len(points), 2):
					lp(points[idx], points[idx+1])
			except GraphicException:
				pass

		ud['label'].pos = touch.pos
		self.update_touch_label(ud['label'], touch)
		#return True?

	def on_touch_up(self, touch):
		"""Mouse button up, or stop touch swiping"""
		if touch.grab_current is not self:
			return
		touch.ungrab(self)
		ud = touch.ud
		self.canvas.remove_group(ud['group'])
		self.remove_widget(ud['label'])
		#return True?

	def update_touch_label(self, label, touch):
		label.text = 'ID: %s\nPos: (%d, %d)\nClass: %s' % (
			touch.id, touch.x, touch.y, touch.__class__.__name__)
		label.texture_update()
		label.pos = touch.pos
		label.size = label.texture_size[0] + 20, label.texture_size[1] + 20


class MolecularMaddnessGame(App):
	title = 'Molecular Maddness'
	icon = 'icon.png'

	def on_pause(self):
		"""Called on phones when user switches away from this app."""
		return True # Do nothing?

	def build(self):
		root = ObjectProperty(None) # in .kv file
		# create the root widget and give it a reference of the application instance (so it can access t$
		#self.mainwidget = MainWindow(app=self)
        	#self.root = self.mainwidget

		#Logger.debug('MolecularMaddnessGame: build')
		#return kivy.uix.button.Button(text='Hello World')
		game = MainWindow()
		Clock.schedule_interval(game.update, 1.0/30.0)
		return game

	#def build_settings(self, settings):
	#	settings.add_json_panel('Test application',
	#		self.config, data="""... put the json data here ...""")

def main():
	"""app starts here"""
	#Config.set('kivy', 'log_enable', 1)
	#Config.set('kivy', 'log_level', 'debug')
	#Config.write()
	#Logger.debug('MolecularMaddnessGame: main')
	MolecularMaddnessGame().run()
