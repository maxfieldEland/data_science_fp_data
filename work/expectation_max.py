import numpy as np
import pandas as pd
from collections import Counter
import pymc3 as pm
import matplotlib.pyplot as plt
import json
holds_raw = pd.read_excel("hold_submission_form.xlsx")

# ----------------------------------------------- PREPARE DATA FOR EXPECTATION MAXIMIZATION --------------------


# hold labels is a dict of numbers that correspond to holds and their values that are a list of probable hold classes. 
hold_labels = {}
# from hold labels, for each hold there will be a dictionary that represents the distribution of potential classes for that respective hold

numWords = []
for i in range(1,41):
    numWords.append(i)
for i in range(50,150):
    numWords.append(i)

#get label for associated hold id via index
for idx,i in enumerate(numWords):
    labels = list(holds_raw.iloc[:,idx])
    true_labels = []
    for ele in labels:
        if type(ele) == int:
            true_labels.append(ele)
    # label : number of votes for label for hold
    hold_labels[i] = dict(Counter(true_labels))
    

# ---------------------------------------------------- EXPECTATION MAXIMIZATION --------------------------------------------------

# majority vote estimate
majority_labs = {}
for i in numWords:
    try:
        majority = max(hold_labels[i],key = hold_labels[i].get)
        majority_labs[i] = majority
    except:
        ValueError

#- EM result
data = np.array(holds_raw)

I = data.shape[1]
J = data.shape[0]
K = 5
N = I*J


z_init = np.zeros(I, dtype = np.int64)
alpha = np.ones( K )
beta = np.ones( (K,K) ) + np.diag( np.ones(K) )

model = pm.Model()
with model:
    pi = pm.Dirichlet( 'pi', a=alpha, shape=K )
    theta = pm.Dirichlet( 'theta', a=beta, shape=(J,K,K) )
    z = pm.Categorical( 'z', p=pi, shape=I, testval=z_init )


with model:
    step1 = pm.Metropolis( vars=[pi,theta] )
    step2 = pm.CategoricalGibbsMetropolis( vars=[z] )
    trace = pm.sample( 5000, step=[step1, step2], progressbar=True )

pm.traceplot( trace, varnames=['pi'] )
z = trace['z'][-1000:,:]

z_hat = np.zeros( I )
for i in range( I ):
    z_hat[ i ] = np.bincount( z[:,i] ).argmax()
    
# ----------------------------------------------- Analysis of hold type ----------------------------------------
plt.hist(z_hat)
plt.hist(majority_labs)


estimated_labels = majority_labs
with open('estimated_holds.json','w') as fp:
    json.dump(estimated_labels,fp)

