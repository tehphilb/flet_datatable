# main class for the data table UI
from flet import *
from controls import addToControlReference

class DataTable(UserControl):
    def __init__(self):
        super().__init__()

    def dataTableInstance(self):
        # set the class instance as a key:value pair in the global dict
        # key => DataTable and the value => self (instance of the class, the object location in memory)
        addToControlReference("DataTable", self)

    def build(self):
        self.dataTableInstance()
        return Row(
            
        )
