# main class for the data table UI
from flet import *
from controls import addToControlReference


class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()

    def dataTableInstance(self):
        # set the class instance as a key:value pair in the global dict
        # key => DataTable and the value => self (instance of the class, the object location in memory)
        addToControlReference("AppDataTable", self)

    def build(self):
        self.dataTableInstance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(1, "#ebebeb"),
                    horizontal_lines=border.BorderSide(0.3, "#ebebeb"),
                    vertical_lines=border.BorderSide(0.3, "#ebebeb"),
                    # the columns args will set the number of columns to be displayed
                    columns=[
                        DataColumn(
                            Text("Column One", size=12,
                                 weight=FontWeight.W_500),
                        ), DataColumn(
                            Text("Column Two", size=12,
                                 weight=FontWeight.W_500),
                        ), DataColumn(
                            Text("Column Three", size=12,
                                 weight=FontWeight.W_500),
                        ), DataColumn(
                            Text("Column Four", size=12,
                                 weight=FontWeight.W_500),
                        ),
                    ],
                    # here configure the form button to append the data rows
                    rows=[],
                )
            ]
        )
