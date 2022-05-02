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
from bs4 import BeautifulSoup
import requests


class SM(ScreenManager):

    def __init__(self, **kwargs):
        super(SM, self).__init__(**kwargs)

class Screen1(Screen):
    investment = 0
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)

    def exit(self, instance):
        quit()

    def callback(self, instance):

        entry = self.manager.ids['screen1'].ids.my_input.text
        greeting = self.manager.ids['screen1'].ids.my_label
        self.investment = entry


        if entry.isnumeric():
            if int(entry) >= 10000:
                if int(entry) < 1000000000:
                    greeting.text = "Calculating: $" + entry
                    greeting.color = '90EE90'
                    self.manager.current = 'screen2'
                else:
                    greeting.text = "Please keep the amount under a billion"
                    greeting.color = '90EE90'
            else:
                greeting.text = "Please keep the amount above $10,000"
                greeting.color = '90EE90'
        else:
            greeting.text = "Please enter a numerical-only value"
            greeting.color = "#FF0000"

class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)

    def back(self, instance):
        self.manager.current = 'screen1'

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
        if int(entry) == 2:
            self.manager.current = 'r2screen'
        if int(entry) == 3:
            self.manager.current = 'r3screen'
        if int(entry) == 4:
            self.manager.current = 'r4screen'
        if int(entry) == 5:
            self.manager.current = 'r5screen'

class r1Screen(Screen):
    def __init__(self, **kwargs):
        super(r1Screen, self).__init__(**kwargs)

    def callback(self, instance):
        greeting = self.manager.ids['r1screen'].ids.invest
        greeting.text = "Invest " + str(float(Screen1.investment)/12) + " monthly in VFV.TO for a year"

    url = 'https://www.google.com/search?q=vfv.to&ei=hiBvYvKeE87OtQb-_anIDQ&ved=0ahUKEwjy-aXQwr_3AhVOZ80KHf5-CtkQ4dUDCA4&uact=5&oq=vfv.to&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQ-gEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BQgAEJECOgoILhDHARDRAxBDOhEILhCABBCxAxCDARDHARCvAToRCC4QgAQQsQMQgwEQxwEQ0QM6EQguEIAEELEDEIMBEMcBEKMCOggILhCABBCxAzoICAAQsQMQgwE6DgguEIAEELEDEMcBENEDOgcIABCxAxBDOgQIABBDOg0ILhCxAxDHARCjAhBDOggIABCABBCxAzoKCAAQsQMQgwEQQ0oECEEYAEoECEYYAFCkCljSEmCKF2gBcAB4AIABf4gBxASSAQM0LjKYAQCgAQHIAQjAAQE&sclient=gws-wiz'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    price = doc.find() #???



class r2Screen(Screen):
    def __init__(self, **kwargs):
        super(r2Screen, self).__init__(**kwargs)

class r3Screen(Screen):
    def __init__(self, **kwargs):
        super(r3Screen, self).__init__(**kwargs)

class r4Screen(Screen):
    def __init__(self, **kwargs):
        super(r4Screen, self).__init__(**kwargs)

class r5Screen(Screen):
    def __init__(self, **kwargs):
        super(r5Screen, self).__init__(**kwargs)

class MZ_Invest(App):
    def build(self):
        sm = SM()
        return sm

if __name__ == "__main__":
    MZ_Invest().run()
