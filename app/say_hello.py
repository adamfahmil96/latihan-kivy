from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        ## source: https://www.freepik.com/free-vector/flat-design-logos-pack_12979895.htm#query=letter%20a&position=11&from_view=search&track=sph
        self.window.add_widget(Image(source="../assets/images/logo.png"))

        # label widget
        self.greeting = Label(
                            text="What's your name?",
                            font_size=18
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                        multiline=False,
                        padding_y=(20, 20),
                        size_hint=(1, 0.5)
                    )
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                            text="GREET",
                            size_hint=(1, 0.5),
                            bold=True,
                            background_color='#ecb533',
                            background_normal=''
                        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # return
        return self.window
    
    def callback(self, event):
        self.greeting.text = f'Hello, {self.user.text}!'


if __name__ == "__main__":
    SayHello().run()
