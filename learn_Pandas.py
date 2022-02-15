#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


mySeries = pd.Series([1,2,3,4,5,6],index = ['Row1','Row2','Row3','Row4','Row5','Row6'])
mySeries


# In[4]:


mySeries.values


# In[5]:


mySeries.index


# In[6]:


mySeries.Row4


# In[7]:


mySeries['Row4']


# In[8]:


mySeries[mySeries>2]


# In[9]:


mySeries.rename({'Row1':'a','Row2':'b','Row3':'c','Row4':'d','Row5':'e','Row6':'f'})


# In[10]:


New_Arr = np.array([[3,6,9],[2,4,8],[4,8,12],[7,14,49]])
New_DataFrame = pd.DataFrame(New_Arr , index = ['Row1','Row2','Row3','Row4']
                                     , columns =['col1','col2','col3'] )
New_DataFrame


# In[11]:


New_Dictionary = {'col1':[3,2,4,7] , 'col2':[6,4,8,14] , 'col3':[9,8,12,49] }
New_Dictionary


# In[12]:


New_DataFrame2 = pd.DataFrame(New_Dictionary , index = ['Row1','Row2','Row3','Row4']
                                     , columns =['col1','col2','col3'] )
New_DataFrame2


# In[13]:


New_DataFrame.index


# In[14]:


New_DataFrame.columns


# In[15]:


New_DataFrame.values


# In[16]:


New_DataFrame.iloc[1][2]


# In[17]:


New_DataFrame.loc['Row2']['col2']


# In[18]:


New_DataFrame['col4']=[9,10,11,12]
New_DataFrame


# In[19]:


New_DataFrame.loc[['Row2','Row3'],'col1'] = 0
New_DataFrame


# In[20]:


New_DataFrame.reset_index(drop=True , inplace=True)
New_DataFrame


# In[21]:


New_DataFrame.drop('col4', axis = 1)


# In[22]:


New_DataFrame


# In[23]:


New_DataFrame.drop('col4', axis = 1, inplace=True)


# In[24]:


New_DataFrame


# In[25]:


New_DataFrame.rename(columns={'col2': 'my_new_col4'} , inplace=True)
New_DataFrame


# In[26]:


New_DataFrame.replace(49 , 999)


# In[27]:


New_DataFrame.col1 = ['{:.2f}'.format(x) for x in New_DataFrame.iloc[:,0]]


# In[28]:


New_DataFrame


# In[29]:


New_DataFrame['col3'] = New_DataFrame['col3'].apply(lambda x :'{:.2f}'.format(x))


# In[30]:


New_DataFrame


# In[31]:


New_DataFrame.sort_index(axis = 1, ascending= False , inplace = True)
New_DataFrame


# In[32]:


New_DataFrame.sort_index(axis = 0, ascending= False)


# In[33]:


New_DataFrame


# In[34]:


New_DataFrame.sort_values(by = 'col1', ascending= False , inplace = True)
New_DataFrame


# In[35]:


New_DataFrame.sort_values(by = 'my_new_col4', ascending= True , inplace = True)
New_DataFrame


# In[36]:


New_DataFrame.head(2)


# In[37]:


New_DataFrame.tail(2)


# In[39]:


Data = pd.read_csv('SampleCSVFile_53000kb.csv', encoding= 'unicode_escape')


# In[40]:


Data


# In[ ]:




