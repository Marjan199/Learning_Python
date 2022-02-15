#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


My_Arr = np.array([[1,2],[8,9]])


# In[5]:


My_Arr


# In[6]:


My_Matrix = np.matrix([[1,2],[8,9]])


# In[7]:


My_Matrix


# In[10]:


My_3D_Arr = np.array([[1,2,10],[3,4,11],[7,8,12]])


# In[15]:


Result = My_3D_Arr @ My_3D_Arr
Result


# Multiply arrays 

# In[16]:


Result2 = np.dot(My_3D_Arr , My_3D_Arr)
Result2


# Multiply arrays 

# In[21]:


np.multiply(My_3D_Arr , My_3D_Arr)


# Multiply each value by its corresponding value 

# In[19]:


np.prod(My_3D_Arr) 


# * multiply of all members 

# In[30]:


My_Result3 = np.array([1,2,3])
My_Result3 = My_Result3 + 5
My_Result3 


# * Broadcasting

# In[27]:


c = np.ones((3,3))


# In[28]:


c


# In[29]:


c + My_Result3


# * Broadcasting

# In[31]:


c = np.ones((3,1))
c


# In[3]:


np.zeros((2,3))


# In[35]:


b = np.array([3,4,5])
b


# In[36]:


c + b


# * Broadcasting

# In[40]:


np.sum(My_Result3)


# Sum of all members

# In[43]:


c + b


# In[41]:


np.sum(c + b)


# In[42]:


np.cumsum(c + b)


#  Sum of each element with the sum of the elements before it 

# In[44]:


np.cumsum((c + b) , axis = 0)


# In[45]:


np.cumsum((c + b) , axis = 1)


# In[46]:


np.subtract((c + b) , b)


# In[48]:


np.divide([8 , 4 , 3.24] , 2)


# In[49]:


np.floor_divide([8 , 4 , 3.24] , 2)


# In[50]:


np.math.sqrt(16)


# In[52]:


np.math.nan


# nan = not a number

# In[53]:


np.math.inf


# inf = infinity

# In[54]:


np.random.uniform(1 , 5 , (2,3))


# Random Numbers Between 1 and 5

# In[57]:


np.random.standard_normal((3,1))


# In[58]:


np.arange(1, 10, 3)


# Creat a sequence of numbers from 1 to 10 with step size = 3

# In[59]:


np.linspace(1, 10, 3)


# In[60]:


np.linspace(1, 10, 3)


# Take 3 numbers from 1 to 10 

# In[6]:


a = np.array([[1,2],[3,4]])
a


# In[7]:


np.size(a)


# In[8]:


np.shape(a)


# In[9]:


First_Arr = ([1,2,5,6,1,8,7,4,3,3,2])
Second_Arr = ([9,2,2,2,7,5,3,11,1])


# In[10]:


np.unique(First_Arr)


# In[11]:


np.union1d(First_Arr , Second_Arr)


# In[12]:


np.intersect1d(First_Arr , Second_Arr)


# In[13]:


np.mean(First_Arr )


# In[14]:


np.mean(Second_Arr)


# In[15]:


np.median(First_Arr)


# In[16]:


np.std(First_Arr)


# std = standard deviation

# In[17]:


np.var(First_Arr)


# var = variance

# In[18]:


Polynomials = np.array([1,3,3])
np.polyval(Polynomials , 4)


# x^2 + 3x + 3 with x=4

# In[19]:


np.polyder(Polynomials)


# Derivative 

# In[20]:


np.polyint(Polynomials)


#  Integral = x^3/3 + 1.5x^2 + 3x 

# In[ ]:




