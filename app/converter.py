from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar


class ConverterApp(MDApp):
    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()

        # top toolbar
        self.toolbar = MDTopAppBar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.flip()]
        ]
        screen.add_widget(self.toolbar)

        # logo
        screen.add_widget(Image(
            source="../assets/images/logo.png",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint=(0.5, 0.25)
        ))

        # collect user input
        self.input = MDTextField(
            text="enter the binary number",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            font_size=22
        )
        screen.add_widget(self.input)

        # secondary and primary widget
        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"
        )
        self.converted = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # CONVERT button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.convert
        ))

        return screen

    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.text = "enter a decimal number"
            self.converted.text = ""
            self.label.text = ""
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.text = "enter a binary number"
            self.converted.text = ""
            self.label.text = ""

    def convert(self, args):
        if self.state == 0:
            val = int(self.input.text, 2)
            self.converted.text = str(val)
            self.label.text = "in decimal is: "
        else:
            val = bin(int(self.input.text))[2:]
            self.converted.text = str(val)
            self.label.text = "in binary is: "

if __name__ == '__main__':
    ConverterApp().run()
