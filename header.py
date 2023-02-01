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

# Header inner components
    def appHeaderBrand(self):
        # here the brand can be set
        return Container(
            content=Text("Brand", size=20, color="white")
        )

    def appHeaderSearch(self):
        # here a search bar is created
        return Container(
            padding=0,
            width=320,
            bgcolor="white10",
            border_radius=8,
            opacity=0.85,
            height=50,
            # animate_opacity=320,
            # padding=padding.symmetric(vertical=2),
            content=ListTile(
                title=TextField(
                    border_color="transparent",
                    # text_size=14,
                    text_style=TextStyle(
                        color="white", weight=FontWeight.W_300),
                    # content_padding=0,
                    cursor_color="white",
                    # cursor_width=0.7,
                    color="white",
                    hint_text="Search",
                    hint_style=TextStyle(color="white"),
                    # on_change=lambda e: self.filterDataTable(e),
                ),
                trailing=Icon(
                    name="SEARCH_ROUNDED",
                    color="white",
                    # icon_size=20,),
                )
            ),
        )

    def appHeaderAvatar(self):
        # here a user avatar can be added
        return Container(
            content=IconButton(icons.PERSON, icon_color="white",
                               icon_size=30, opacity=0.85,)
        )

    # TDOD: add logig that the saerch bar does not disappear as long the seach has not submitted
    # def showSearchBar(self, e):
    #     # manage when the user hovers over the header that the search bar is shown
    #     if e.data == 'true':
    #         # accesing the appHeaderSearch opacity
    #         self.controls[0].content.controls[1].opacity = 1
    #         self.controls[0].content.controls[1].update()
    #     else:
    #         # set emty string as soon the search bar disappear
    #         self.controls[0].content.controls[1].content.controls[1].value = ""
    #         self.controls[0].content.controls[1].opacity = 0
    #         self.controls[0].content.controls[1].update()

    def filterData

    def build(self):
        self.appHeaderInstance()

        return Container(
            expand=True,
            # on_hover=lambda e: self.showSearchBar(e),
            # height=60,
            bgcolor="#3f2a56",
            border_radius=border_radius.only(topLeft=16, topRight=16,),
            padding=padding.symmetric(horizontal=24, vertical=12),
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.appHeaderBrand(),
                    self.appHeaderSearch(),
                    self.appHeaderAvatar(),
                ],
            ),
        )
