#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import numpy as np
ex_ther=pd.read_csv("/Users/saranshmehta/Desktop/hack/THERAPIST REGISTRATION (Responses) - Form Responses 1.csv")
ex_ther


# In[49]:


ex_pat=pd.read_csv("/Users/saranshmehta/Desktop/hack/Help Us Get To Know You (Responses) - Form Responses 1.csv")
ex_pat


# In[93]:


for i in range(0,3):    
    '''spec_ther[i] = ex_ther["SPECIALISATION"][i]
    fee_ther[i]=ex_ther["FEES PER SESSION"][i]
    age_ther[i]=ex_ther["PREFERRED AGE GROUP"][i]
''' 
    t_points={}
    scores=[]
    for j in range(0,4):
        
        score=0
        if ex_pat["WHAT KIND OF THERAPY ARE YOU LOOKING FOR"][i] in ex_ther["SPECIALISATION"][j]:
            score=score+3
        if (ex_pat["WHAT KIND OF FEE PER SESSION ARE YOU COMFORTABLE WITH"][i])==(ex_ther["FEES PER SESSION "][j]):
            score=score+2
        if (ex_pat["CAN WE KNOW WHAT AGE CATEGORY YOU BELONG TO"][i])==( ex_ther["PREFERRED AGE GROUP "][j]):
            score =score+1
        t_points[ex_ther["NAME"][j]]=score
    
print(t_points)


# In[98]:


max = 0
best_t=0
for i in t_points:
    if t_points[i]>max:
        max = t_points[i]
print(max)
if max==0:
    print("contact the national helpline number for immediate assitance : call or text 988")


# In[ ]:





# 
