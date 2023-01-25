# this is the header of the application

from flet import *
from controls import addToControlReference, returnControlReference

# assigns the returned dict as variable
controlMap = returnControlReference()

# main class
class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def appHeaderInstance(self):
        # set the class instance as a key:value pair in the global dict
        # key => "AppHeader" and the value => self (instance of the class, the object location in memory)
        addToControlReference("AppHeader", self)

### Header inner components
    def appHeaderBrand(self):
        # here the brand can be set
        return Container(
            content=Text("Brand", size=15)
        )

    def appHeaderSearch(self):
        # here a search bar is created
        return Container(
            width=320,
            bgcolor="white10",
            border_radius=6,
            opacity = 0,
            animate_opacity=320,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=18, opacity=0.85),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=14, #TDOD: add text_style = FontWeight.W_100
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=0.7,
                        color="white",
                        hint_text="Search",
                        # on_change=lambda e: self.filterDataTable(e),
                    ),
                ],
            ),
        )

    def appHeaderAvatar(self):
        # here a user avatar can be added
        return Container(
            content=IconButton(icons.PERSON)
        )

    def showSearchBar(self, e): # TDOD: add logig that the saerch bar does not disappear as long the seach has not submitted
        # manage when the user hovers over the header that the search bar is shown
        if e.data == 'true':
            self.controls[0].content.controls[1].opacity = 1 # accesing the appHeaderSearch opacity
            self.controls[0].content.controls[1].update()
        else:
            self.controls[0].content.controls[1].content.controls[1].value = "" # set emty string as soon the search bar disappear
            self.controls[0].content.controls[1].opacity = 0
            self.controls[0].content.controls[1].update()

    def build(self):
        self.appHeaderInstance()

        return Container(
            expand=True,
            on_hover=lambda e: self.showSearchBar(e),
            height=60,
            bgcolor="#3f2a56",
            border_radius=border_radius.only(topLeft=15, topRight=15,),
            padding=padding.only(left=15, right=15,),
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.appHeaderBrand(),
                    self.appHeaderSearch(),
                    self.appHeaderAvatar(),
                ],
            ),
        )