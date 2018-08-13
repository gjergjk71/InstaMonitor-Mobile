from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
	def __init__(self,**kwargs):
		super(GridLayout,self).__init__(**kwargs)

class SimpleKivy(App):
	def build(self):
		return LoginScreen()

if __name__ == "__main__":
	SimpleKivy().run()