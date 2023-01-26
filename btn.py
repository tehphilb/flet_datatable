# main file to handle user input data

from flet import *
from controls import returnControlReference, addToControlReference
# from form_handler import FormHandler

# get the global map dict
control_map = returnControlReference()

# this method will handle the user input data
def getInputData(e):
    pass


def returnFromButton():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: getInputData(e),  # TODO: get input data
            bgcolor="#3b2c53",
            color="#f3f3f4",
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        
                    ),
                    Text("Add to table",
                         weight=FontWeight.W_500,),
                ],
            ),
            style=ButtonStyle(
                shape={"": RoundedRectangleBorder(radius=6),
                       },
                color={
                    "": "#f3f3f4",
                },
            ),
            #height=52,
            #width=235
        )
    )
