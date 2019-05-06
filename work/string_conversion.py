# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:48:27 2019

@author: mgreen13
"""
from num2words import num2words



def str_append(s, n):
    output = ''
    i = 0
    while i < n:
        output += s
        i = i + 1
    return output
numWords = []
for i in range(2,41):
    numWords.append('\"&'+ str(num2words(i)).replace("-", "_")+'=\"')
    numWords.append(str(num2words(i)).replace("-", "_"))
for i in range(50,150):
    numWords.append('\"&' +str(num2words(i)).replace(" ", "_").replace("-","_")+'=\"')
    numWords.append(str(num2words(i)).replace(" ", "_").replace("-","_"))

end = "'&action=insert';"

url = "script_url + '?callback=ctrlq&one=' + one + "
inner = ""
for i in numWords:
    inner = inner + str(i) + "+"

url = url + inner + end

# 2nd string formation 
# all variables in java script funcion insert values
numWords2= []
for i in range(1,151):
    if i <41 or i >50:
        numWords2.append(num2words(i).replace(" ", "_").replace("-","_"))

varNames = []
for i in numWords2:
    varNames.append("var {} = $(\".{}\").val();".format(i,i))

varName = ""
for i in varNames:
    varName = varName + i + " "
    
#final string building section

objs = ""
for i in range(1,151):
    if i < 41 or i > 49:
        num = num2words(i).replace(" ", "_").replace("-","_")
        objs = objs + "var {}  = request.parameter.{};".format(num,num)

numWordStrings = []
for i in range(1,151):
    if i < 41 or i > 49:
        numWordStrings.append(num2words(i).replace(" ", "_").replace("-","_"))
        
nums = {}
sql_col_names = []
for idx,i in enumerate(numWordStrings):
    if idx +1 > 40:
        idx = idx + 9
    nums[idx+1] = '{}'.format("INT " + i)
    sql_col_names.append(i + " INT")

sys.intern(sql_col_names[2])

sql_col_names

for i in sql_col_names:
        print(i + ',')


