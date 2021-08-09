import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

kivy.require('1.9.0')


class DarishkaAMSRandom(App):

    def build(self):
        # return Label(text="hello")
        return BoxLayout()


if __name__ == "__main__":
    DarishkaAMSRandom().run()

# DarishkaAMSRandom = DarishkaAMSRandom()
# DarishkaAMSRandom.run()

