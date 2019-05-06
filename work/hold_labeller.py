# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:18:23 2019

@author: mgreen13
"""

import pandas as pd
import json

a = pd.read_table("hold_mapping.txt",sep='\t',header = None )
a1 = list(a[0])
a1.extend(list(a[2]))
a1.extend(list(a[4]))
a1.extend(list(a[6]))
a1_clean = a1[0:140]

a1_clean_int = []
for i in a1_clean:
    a1_clean_int.append(int(i))
b1 = list(a[1])
b1.extend(list(a[3]))
b1.extend(list(a[5]))
b1.extend(list(a[7]))

b1_clean = []

for val in b1:
    if val != "nan":
        b1_clean.append(val.split("-")[1])
hold_map = dict(zip(a1_clean_int, b1_clean))

with open('hold_labels.json', 'w') as fout:
    fout.write(json.dumps(hold_map))
