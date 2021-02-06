from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (300, 500)

class ExampleApp(MDApp):
    def build(self):
        kv = Builder.load_file("toolbar.kv")
        return kv

    def navigation_draw(self):
    	print("Navigation")

    foo="yay"


ExampleApp().run()
