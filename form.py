# this is the form class for the app
# it holds the datatable and so on

from flet import *
from controls import addToControlReference

class AppForm(UserControl):
    def __init__(self):
        super().__init__()

    def appFormInstance(self):
    # set the class instance as a key:value pair in the global dict
    # key => "AppForm" and the value => self (instance of the class, the object location in memory)
        addToControlReference("AppForm", self)

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

                ],
            )

        )