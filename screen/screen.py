from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.picker import MDThemePicker

class MenuScreen(Screen):
	
    def show_themepicker(self):
        picker=MDThemePicker()
        picker.open()


class ProfileScreen(Screen):
	pass


class UploadScreen(Screen):
	pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))

class ExampleApp(MDApp):
	def build(self):
	   self.theme_cls.primary_palette = "Red"
	   self.theme_cls.primary_hue = "900"
	   self.theme_cls.theme_style = "Light"
	   kv = Builder.load_file("screen.kv")
	   return kv

ExampleApp().run()
