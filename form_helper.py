from flet import *

# this class generates a new instance of textfield and insert it into the data table


class FormHelper(UserControl):
    def __init__(self, userInput):
        self.userInput = userInput
        super().__init__()

    def saveValue(self, e):
        e.control.read_only = True
        e.control.update()

    def build(self):
        return TextField(
            value=self.userInput,  # form field values pass here
            border_color="transparent",
            # size=12,
            # weight=FontWeight.W_500,
            # height="20",
            # text_style=12,
            # content_padding=0,
            # cursor_color="black",
            cursor_width=0.9,
            # color="black",
            read_only=True,  # this will make the field read only
            on_blur=lambda e: self.saveValue(e),
        )
