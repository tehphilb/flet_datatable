# main file to handle user input data

from flet import *
from controls import returnControlReference, addToControlReference
# from form_handler import FormHandler

# get the global map dict
control_map = returnControlReference() 

class Btn(UserControl):
    def __init__(self):
        super().__init__()


def returnFromButton():
    return Container(
        alignment=alignment.CENTER,
        content=ElevatedButton(
        
        )
    )
