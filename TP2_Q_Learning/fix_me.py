

# MERZOUK OUMEDDAH 4 IABD CLASSE 1


import numpy as np
import random

############ EDIT ABOVE FUNCTIONS ####

def create_Q_table():  # create q table with zeros and size
    q_table = np.zeros((9,4))  # number of states, number of actions
    return q_table

def update(q_table, state, action, r, Gamma, stateNext, actionNext):
    # use formula to update q_table
    q_table[state][action] = q_table[state][action]  +  0.7* ( r + Gamma* np.argmax(q_table[stateNext, ]) - q_table[stateNext][actionNext] )
    return q_table

def choose_action(state, q_table, epsilon):
    if epsilon >= random.random(): #  take a random number and compare to exploratio rate
        action = random.randint(0, 3)
        # choose a random action
    else:
        action = np.argmax(q_table[state, ])  # choose the best action for a state
    return action

def reduce_epsilon(epsilon):

    epsilon = epsilon * 0.99  # reduce epsilon after each step
    epsilon = max(epsilon, 0.5) # set a minimum value for epsilon
    return epsilon