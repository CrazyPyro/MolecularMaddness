import kivy
kivy.require('1.2.0') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.button import Button

class MolecularMaddnessGame(App):
	def build(self):
		return Button(text='Hello World')

def main():
	"""your app starts here"""
	MolecularMaddnessGame().run()
