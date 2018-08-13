from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from InstagramAPI import InstagramAPI
from functools import partial

def login(username,password):
	api = InstagramAPI(username,password)
	api.login()
	return api

class LoginScreen(GridLayout):
	def __init__(self,**kwargs):
		super(LoginScreen,self).__init__(**kwargs)
		self.cols = 3
		self.add_widget(Label())
		self.add_widget(Label(text="Login",
							  font_size=45))
		self.add_widget(Label())
		self.add_widget(Label(text="Username:",
							  font_size=45))
		self.username = TextInput(height=100,
								  font_size=45,
								  multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label())

		self.add_widget(Label(text="Password:",
							  font_size=45))
		self.password = TextInput(height=100,
								  font_size=45,
								  multiline=False,
								  password=True)
		self.add_widget(self.password)
		self.add_widget(Label())

		self.add_widget(Label())
		self.login = Button(text="Login")
		self.login.bind(on_press=lambda _: login(self.username.text,self.password.text))
		self.add_widget(self.login)
		self.add_widget(Label())

class SimpleKivy(App):
	def build(self):
		return LoginScreen(row_force_default=True, row_default_height=70)

if __name__ == "__main__":
	SimpleKivy().run()