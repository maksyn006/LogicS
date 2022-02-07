from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
class Container(FloatLayout):
    pass
class MyApp(App):
    def __init__(self):
        super().__init__()
    def build(self):
        return Container()
if __name__ == '__main__':
    MyApp().run()
