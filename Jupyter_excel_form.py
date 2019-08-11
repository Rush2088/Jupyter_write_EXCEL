import pandas as pd
# from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from ipywidgets import HBox, VBox
from IPython.display import display



#################### UI##################################

Operator = widgets.Text(
placeholder='Name',
value= 'Name',
description='Operator :',
disabled=False )

Number = widgets.Text(
placeholder='111',
value= '111',
description='Number :',
disabled=False )   

ui = VBox([Operator,Number])
button = widgets.Button(description="Update Records")
display(ui,button)
button.on_click(submit_fields)


        

#################### MAIN FUNCTION ##########################

def submit_fields(b):
    path = 'output.xlsx'
    df1 = pd.read_excel(path)
    SeriesA = df1['Operator']   # interactive form fields
    SeriesB = df1['Number']     # interactive form fields
    A = pd.Series(Operator.value)
    B = pd.Series(Number.value)
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    df2 = pd.DataFrame({"Operator":SeriesA, "Number":SeriesB})
    df2.to_excel(path, index=False)
   
