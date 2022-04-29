from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

entry = ""

class SM(ScreenManager):

    def __init__(self, **kwargs):
        super(SM, self).__init__(**kwargs)

class Screen1(Screen):

    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)

    def callback(self, instance):

        entry = self.manager.ids['screen1'].ids.my_input.text
        greeting = self.manager.ids['screen1'].ids.my_label

        if entry.isnumeric() and int(entry) >= 10000:
            greeting.text = "Calculating: $" + entry
            greeting.color = '90EE90'
            self.manager.current = 'screen2'

        else:
            greeting.text = "Invalid"
            greeting.color = "#FF0000"

class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)

    def callback(self, instance):

        entry = self.manager.ids['screen2'].ids.my_input.text
        greeting = self.manager.ids['screen2'].ids.my_label

        # If Input is Valid
        if entry.isnumeric() and 1 <= int(entry) <= 5:
            greeting.text = "Calculating"
            greeting.color = '#FF0000'
        else:
            greeting.text = "Invalid"
            greeting.color = "#FF0000"

        # If input is 1
        if int(entry) == 1:
            self.manager.current = 'r1screen'

class r1Screen(Screen):
    def __init__(self, **kwargs):
        super(r1Screen, self).__init__(**kwargs)


class MZ_Invest(App):
    def build(self):
        sm = SM()
        return sm

if __name__ == "__main__":
    MZ_Invest().run()
