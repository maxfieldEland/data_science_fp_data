# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:07:50 2019

@author: mgreen13
"""

# - ------------------------------- Import useful packages ----------------
import json
import numpy as np
import re
import seaborn as sns
sns.set_style("white")
import pandas as pd
import statistics

# -------------------------------------------------- Custom functions --------------------------------


def extract_num(str_input):
    numbers = re.findall('\d+',str_input) 
    return(int(numbers[0]))

# ----------------------------------------- Load in data from folders of files -----------------------------------

# Build file path strings, there are 42 files. 
file_names = []
for i in range(1,42):
    file = "routes{}.json".format(i)
    folder = "routes_json/"
    file_path = folder + file
    file_names.append(file_path)
    
# load data in from files
data = []
for file in file_names:
    # there is a single exception in naming convention that must be skipped
    try:
        with open(file, encoding = 'utf-8') as f:
            for line in f:
                file_outer = json.loads(line)
        data_file = file_outer['Data']
        data.extend(data_file)
    except: 
        FileNotFoundError

# load in estimated hold classes
with open('estimated_holds.json','r') as fp:
    hold_class = json.load(fp)

# load in hold name transition dictionary
with open('hold_labels.json','r') as fp:
    hold_dict = json.load(fp)
    


# ------------------------------------ Build route_corpus from full data set ------------------------------
route_corpus = []
idx = 0
# pull each route out of initial full data structure and collect only meaningfull fields
for route in data:
    idx = idx + 1
    route_data = {'id' : idx,
                  'grade':route['Grade'],
                  'holds': [],
                  'loc': '{},{}'.format(route['Setter']['City'],route['Setter']['Country']),
                  'date':route['DateTimeString'],
                  'transf_holds': {"x":[],"y":[]},
                  'quality': route['UserRating'],
                  'num_repeats' : route['Repeats'],
                  'length' : len(route['Moves'])}
    
    moves = route['Moves']
    for i in moves:
        route_data['holds'].append(i['Description'])
    route_corpus.append(route_data)

# prune problem routes ?? errors in web data 
# first problem is route with id = 12152, reporting a hold on tile A6 which is not used in this verions of the moonboard
del route_corpus[12152]


#----------------------------------------- Load in hold usable surface depths ---------------------------
hold_depth = pd.read_table("holds2.txt",sep='\t',header = None)
labels = list(hold_depth[0])
for idx,label in enumerate(labels):
    labels[idx] = label.strip()
depths = list(hold_depth[1])
hold_depth_dict = {}
for i in list(range(len(labels))):
    hold_depth_dict[labels[i]] = depths[i]
    
# add extranous depth 
hold_depth_dict['D17'] = 2.39
#---------------------------------------------------- get distribution of grades ----------------------------------------
grades = []
for i in route_corpus:
    grades.append(i['grade'])

# ----------------------------------- transform letter to number coordinate systems -------------------------------------
letter2num = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K"}
letter2num= {y:x for x,y in letter2num.items()}

# loop over each route
for idx,i in enumerate(route_corpus):
    # loop over each hold on the route
    for idx2,hold in enumerate(i['holds']):
        # add transformed x and y components to transf_holds dict
        # x component 
        route_corpus[idx]['transf_holds']['x'].append(letter2num[hold[0]])
        y = extract_num(hold)
        route_corpus[idx]['transf_holds']['y'].append(int(y))
    if len(i['transf_holds']['x']) != len(i['transf_holds']['x']):
        print("ERROR IN ROUTE NUMBER {}".format(idx))

# -----------------------------------calculate the distances between every move on every climb -----------------------

dists = []
for route in route_corpus:
    route['distances'] = []
    for idx,x in enumerate(route['transf_holds']['x']):
        # get distance between current and next hold on route
        x1 = x
        y1 = route['transf_holds']['y'][idx]
        
        try:
            x2 = route['transf_holds']['x'][idx+1]
            y2 = route['transf_holds']['y'][idx+1]
        except:
            IndexError
        # calculate distance between holds by finding hypotenuse of trianlge between holds.
        distance = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        if distance != 0:
            inches_cm = 7.87
            dists.append(distance*inches_cm)
            route['distances'].append(distance*inches_cm)
# ---------------------------------------- configure hold classes and edge depths into route corpus data structure ---------------------
# build coordinate to type dictionary using letter2num dictionarys 
hold_dict_flip = {y:x for x,y in hold_dict.items()}
holds_dist = []

for route in route_corpus:
    route["hold_classes"] = np.zeros(len(route['holds']))
    route["edge_depths"] = np.zeros(len(route['holds']))
    for idx,hold in enumerate(route['holds']):
        formated_loc = ' {} '.format(hold)
        flipped_idx = hold_dict_flip[formated_loc]

        # add edge depth to associated hold
        route['edge_depths'][idx] = hold_depth_dict[hold]
        # add hold class label to associated hold
        hold_type = hold_class[str(flipped_idx)]
        route['hold_classes'][idx] = hold_type
    holds = route['hold_classes']
    holds_true = []
    for i in holds:
        if i != 0.0:
            holds_true.append(i)
    try:
        route['mode_hold'] = statistics.mode(holds_true)
    except statistics.StatisticsError:
        try:
            route['mode_hold'] = statistics.median(holds_true)
        except:
            statistics.StatisticsError
    holds_dist.extend(holds_true)
    route['edge_depths'] = list(route['edge_depths'])
    route['hold_classes'] = list(route['hold_classes'])
    route['mode_hold'] = int(route['mode_hold'])

#  END OF DATA CLEANING -----------------------------
# WRITE DATA TO JSON
with open('route_corpus.json','w',encoding = 'utf-8') as fp:
    json.dump(route_corpus,fp)
    


