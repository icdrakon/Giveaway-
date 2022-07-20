#!/usr/bin/env python
# coding: utf-8

# In[1]:


# random Number generator for giveaway
from random import seed
from random import randint
# seed 
seed(1)
# Numbers generate in a range
for _ in range(11):
	value = randint(0, 54)
	print(value)


# In[ ]:




