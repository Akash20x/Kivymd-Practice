from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty



class SwipeToDeleteItem(MDCardSwipe):
	text = StringProperty()


class ampleApp(MDApp):
    def build(self):
        kv = Builder.load_file("card2.kv")
        return kv

    def on_swipe_complete(self, instance):
        self.root.ids.md_list.remove_widget(instance)

    def on_start(self):
    	for i in range(20):
            self.root.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"One-line item {i}")
            )
ampleApp().run()
