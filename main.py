from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Halo dari GitHub Actions!")

MyApp().run()
