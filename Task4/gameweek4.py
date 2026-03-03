#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np

user = str(input("Choose between Paper (P), Scissors(S) or Rock (R):"))  #the user inputs R, P or S
random = np.array(['P', 'R', 'S'])    #I made an array with R, P and S strings
index = np.random.randint(0, len(random),1)   #generating a random value of the array by the index
print(random[index])

#describing any situation
if user=="P" and random[index]=='R':
    print("You win")
elif user=="P" and random[index]=='P':
    print("Tie")
elif user=="P" and random[index]=='S':
    print("You lost")
    
elif user=="R" and random[index]=='P':
    print("You lost")
elif user=="R" and random[index]=='R':
    print("Tie")
elif user=="R" and random[index]=='S':
    print("You win")

elif user=="S" and random[index]=='P':
    print("You win")
elif user=="S" and random[index]=='S':
    print("Tie")
else:
    print("You lost")

