# main file to handle user input data

from flet import *
from controls import returnControlReference, addToControlReference
from form_helper import FormHelper

# get the global map dict
control_map = returnControlReference()

# these methods will handle the user input data


def updateText(e):
    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()

def getInputData(e):
    for key, value in control_map.items():
        if key == "AppForm":
            data = DataRow(cells=[])
            for userInput in value.controls[0].content.content.controls[0].controls[:]:
                data.cells.append(DataCell(FormHelper(userInput.value),
                                  on_double_tap=lambda e: updateText(e)))
            for userInput in value.controls[0].content.content.controls[1].controls[:]:
                data.cells.append(DataCell(FormHelper(userInput.value),
                                  on_double_tap=lambda e: updateText(e)))

        if key == "AppDataTable":
            value.controls[0].controls[0].rows.append(data)
        #     # value.controls[0].controls[0].append(data)  # append the data to the table
            value.controls[0].controls[0].update()  # update the table


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
            # height=52,
            # width=235
        )
    )
