import numpy as np 
import matplotlib.pyplot as plt
import math


# In[17]:


x=[[0,1,0,0,1,0,0,1,0],[0,1,0,1,1,0,1,1,1],[1,1,1,0,1,1,1,1,1,],[1,1,1,1,1,1,1,1,1]]
x=np.asmatrix(x)
t=[[0,1],[0,1],[1,0],[1,1]]
t=np.asmatrix(t)
w=[[0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1]]
w=np.asmatrix(w)


# In[18]:


def softmax(x):
    
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


# In[23]:


error = np.array([])
eta = 0.1
for i in range(1000):
    for j in range(4):
        y = x[j]*w
        
        Y_out = softmax(y)
        
        e = t[j]- Y_out
        
        error = np.append(error,e)
        
        del_w = eta*np.transpose(x[j])*e
        
        w = w+ del_w


# In[24]:


print("Updated Weights",w)


# In[25]:


print(error)


# In[26]:


plt.plot(error)
plt.show()


# In[ ]: