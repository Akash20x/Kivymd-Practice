from kivy.lang import Builder
from kivymd.app import MDApp


class ExampleApp(MDApp):
    def build(self):
        kv = Builder.load_file("button.kv")
        return kv

ExampleApp().run()
