#!/usr/bin/env python
# coding: utf-8

# In[1]:


grid = [
    [4,0,9,0,0,5,1,0,0],
    [5,3,0,2,1,0,0,0,0],
    [0,6,2,7,0,4,5,0,8],
    [0,0,3,0,6,0,4,0,0],
    [0,8,7,3,0,0,0,0,0],
    [0,5,4,0,9,7,6,8,0],
    [0,0,5,9,0,6,0,0,1],
    [7,2,0,0,0,0,3,0,0],
    [8,9,0,0,7,0,0,5,6]
]


# In[2]:


print(grid)


# In[3]:


import numpy as np


# In[4]:


print(np.matrix(grid))


# In[5]:


def possible(y,x,n):
    global grid
    #is it possible inside the row
    for i in range(0,9):
        if grid [y][i] ==n:
            return False
    #is it possible inside the column
    for i in range(0,9):
        if grid [i][x] ==n:
            return False
    #is it possible inside block
    x0 =(x//3)*3
    y0 =(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True
            


# In[6]:


possible(0,1,7)


# In[7]:


def solve():
    global grid
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input('Do you want to try more:')
solve()


# In[ ]:




