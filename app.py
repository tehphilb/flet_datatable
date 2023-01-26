"""Flet datable application"""

from flet import *
from header import AppHeader # appHeader
from form import AppForm # app input form

def main(page: Page):
    page.bgcolor = "#f3f3f4"
    page.padding = 20
    page.add(
        # main column where each component will be place
        
        Column(
            expand=True,
            controls=[
                # class instances come here
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppForm(),
                Column(
                    scroll='hidden',
                ),
            ]
        )
    )
    page.update()
    pass

if __name__ == "__main__":
    app(target=main)


"https://www.youtube.com/watch?v=39AH8tnTf4E    42:27"