from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

# from kivymd.theming import ThemeManager

from assistant_1 import Assistant

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (720, 720)
# Window.size = (480, 853)


class Container(GridLayout):
    def send_message(self):
        a = Assistant()
        message = self.text_input.text
        answer = a.answer_message(message)

        self.upload_user(self.text_input.text)

        self.upload_assist(answer)

        self.text_input.text = ''

        a.say(answer)

    def listen_message(self):
        a = Assistant()
        self.upload_assist(a.processing())
        text, voice = a.voice_down_and_to_text('output')
        if "я не смогла распознать вашу команду" in text:
            self.upload_assist(text)
        else:
            self.upload_user(text)
        answer = a.answer_talk(text)
        if answer is None:
            self.upload_assist('Error')
        elif len(answer) == 5:
            text1, text_u1, text2, text_u2, text3 = answer
            self.upload_assist(text1)
            self.upload_user(text_u1)
            self.upload_assist(text2)
            self.upload_user(text_u2)
            self.upload_assist(text3)
        elif len([answer]) == 1:
            name = a.analize_user(voice)
            self.upload_assist(f"{name}, {answer}")
            a.say(f"{name}, {answer}")

    def upload_assist(self, answer):
        if answer is None:
            answer = '0'
        self.l10a.text = self.l9a.text
        self.l9a.text = self.l8a.text
        self.l8a.text = self.l7a.text
        self.l7a.text = self.l6a.text
        self.l6a.text = self.l5a.text
        self.l5a.text = self.l4a.text
        self.l4a.text = self.l3a.text
        self.l3a.text = self.l2a.text
        self.l2a.text = self.l1a.text
        self.l1a.text = answer

        self.l10.text = self.l9.text
        self.l9.text = self.l8.text
        self.l8.text = self.l7.text
        self.l7.text = self.l6.text
        self.l6.text = self.l5.text
        self.l5.text = self.l4.text
        self.l4.text = self.l3.text
        self.l3.text = self.l2.text
        self.l2.text = self.l1.text
        self.l1.text = ''

    def upload_user(self, text):
        if text is None:
            text = '0'
        self.l10.text = self.l9.text
        self.l9.text = self.l8.text
        self.l8.text = self.l7.text
        self.l7.text = self.l6.text
        self.l6.text = self.l5.text
        self.l5.text = self.l4.text
        self.l4.text = self.l3.text
        self.l3.text = self.l2.text
        self.l2.text = self.l1.text
        self.l1.text = text

        self.l10a.text = self.l9a.text
        self.l9a.text = self.l8a.text
        self.l8a.text = self.l7a.text
        self.l7a.text = self.l6a.text
        self.l6a.text = self.l5a.text
        self.l5a.text = self.l4a.text
        self.l4a.text = self.l3a.text
        self.l3a.text = self.l2a.text
        self.l2a.text = self.l1a.text
        self.l1a.text = ''


class MyApp(App):
    # theme = ThemeManager()
    # title = 'Assistant'

    #: import MDLabel kivymd.label.MDLabel
    #: import MDTextField kivymd.textfields.MDTextField
    #: import MDRaisedButton kivymd.button.MDRaisedButton

    def build(self):
        # self.theme.theme_style = 'Light'
        return Container()


if __name__ == "__main__":
    MyApp().run()
