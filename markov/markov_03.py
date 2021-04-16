import numpy as np
import time

start = ['R','Su']
#Start probability
p_start = [0.2,0.8]

#t1 = [['R|R','Su|R'],['R|Su','Su|Su']]
#Transition probability
t1 = ['R','Su']
p_t1=[[0.4,0.6],[0.3,0.7]]

#t2 = [['W|R','Sh|R','C|R'],['W|Su','Sh|Su','C|Su']]
t2 = ['Walk','Shop','Clean']
#Emission probability
p_t2=[[0.1,0.4,0.5],[0.6,0.3,0.1]]

initial = np.random.choice(start,replace=True,p=p_start)

#Number of days of simulation
n = 20

st = 1
for i in range(n):
    if st:
        state = initial
        st = 0
        print(state)
    if state == 'R':
        activity = np.random.choice(t2,p=p_t2[0])
        print(state)
        print(activity)
        state = np.random.choice(t1,p=p_t1[0])
    elif state == 'Su':
        activity = np.random.choice(t2,p=p_t2[1])
        print(state)
        print(activity)        
        state = np.random.choice(t1,p=p_t1[1])
    print("\n")
    time.sleep(0.5)
    
    # Output (I printed out the hidden state too)
    # R R Shop -- R Clean -- Su Walk -- Su Walk -- Su Walk -- Su Clean -- Su Walk -- R Shop -- R Shop -- R Shop -- R Shop -- Su Shop -- R Clean -- Su Walk -- Su Walk -- R Shop -- R Clean -- R Clean -- Su Shop -- Su Shop
