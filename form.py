# this is the form class for the app
# it holds the input for the app and so on

from flet import *
from controls import addToControlReference


class AppForm(UserControl):
    def __init__(self):
        super().__init__()

    def appFormInstance(self):
        # set the class instance as a key:value pair in the global dict
        # key => "AppForm" and the value => self (instance of the class, the object location in memory)
        addToControlReference("AppForm", self)

# form inner components
    def appFormInputField(self, name: str, expand: int):
        # here the input fields are created
        return Container(
            expand=expand,
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(value=name, size=10, color="#2a2c36",
                         weight=FontWeight.W_400),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=14,  # TDOD: add text_style = FontWeight.W_100
                        content_padding=0,
                        cursor_color="#2a2c36",
                        cursor_width=0.9,
                        cursor_height=18,
                        color="#2a2c36",
                        # on_change=lambda e: self.filterDataTable(e),
                    )
                ]
            )
        )

    def build(self):
        self.appFormInstance()
        return Container(
            expand=True,
            height=190,
            bgcolor="white10",
            border=border.all(1, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[self.appFormInputField("Field *", True),],

                    ),
                    Row(
                        controls=[self.appFormInputField("Field one", 3),
                                  self.appFormInputField("Field two", 1),
                                  self.appFormInputField("Field three", 1),],
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[], 
                    )
                ],
            )

        )
