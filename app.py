"""Flet datable application"""

from flet import *
from header import AppHeader 

def main(page: Page):
    page.bgcolor = "#f3f3f4"
    page.padding = 20
    page.add(
        # main column where each component will be place
        
        Column(
            expand=True,
            controls=[
                # class instances come here
                AppHeader()
            ]
        )
    )
    page.update()
    pass

if __name__ == "__main__":
    app(target=main)