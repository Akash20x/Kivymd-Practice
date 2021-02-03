from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.properties import ObjectProperty
from textblob import TextBlob


Builder.load_file('labels.kv')


class MyLayout(Widget):
	def my_callback(self):

		top=self.ids.top.text 
		correction=TextBlob(top)
		result=correction.correct()
		self.ids.top.text=str(result)



class ExampleApp(MDApp):
	def build(self):
		return MyLayout()

		
	def on_start(self):
		for i in range(8):
			self.root.ids.container.add_widget(
				OneLineListItem(text=f"Single-line item {i}")
			)



ExampleApp().run()