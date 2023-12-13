from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem


list_helpers = """
Screen:
    ScrollView:
        MDList:
            id: container
"""
class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(list_helpers)
        for i in range(15):
            items = OneLineListItem(text='Item'+str(i))
            screen.ids.container.add_widget(items)


        return screen

DemoApp().run()