# -*- coding: utf-8 -*-
"""project 113

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1chX6_Z9e-7CnKog0gZxmwWsnHBQ-XPNn
"""

from google.colab import files 
files.upload()

import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("project_savings_data.csv")
fig = px.scatter(df, y="quant_saved", color = "rem_any")
fig.show()

