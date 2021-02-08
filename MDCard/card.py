from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from nltk.corpus import wordnet
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition,CardTransition

Builder.load_file('card.kv')
Window.size = (300, 500)


class MyLayout(Screen):
	def my_callback(self):
		top=self.ids.top.text 
		syns = wordnet.synsets(top)
		syns1=syns[0].examples()
		result = ' '.join([str(elem) for elem in syns1]) 
		self.ids.top.text=result


class xampleApp(MDApp):
    def build(self):
    	return MyLayout()


xampleApp().run()
