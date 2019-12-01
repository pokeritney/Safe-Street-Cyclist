# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
data = pd.read_csv("by_hour.csv")
data = data[["Hour", "Lane"]]

rollup = pd.crosstab(index=data['Lane'], columns=data['Hour'])
by_hour = rollup.transpose()

hour = []
for i, row in by_hour.iterrows():
    hour.append({"hour":str(i), "no":row["No"], "yes":row["Yes"]})
