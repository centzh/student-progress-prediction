import os
import pandas as pd
"""
    This function creates a summary of module level participation for given stream
"""
def get_module_participation(challenge_name):

    os.chdir(r"C:\Users\vince\Documents\thesis\results\processed\module_prediction")
    os.chdir(challenge_name)
    file = 'events_processed.csv'

    # Module names 
    if challenge_name == "challenge-newbies-2018":
        problem_names = ["w1p1", "w1p2", "w2p1", "w2p2", "w3p1n", "w3p2", "w4p1", "w4p2", "w5p1", "w5p2"]
    else:
        problem_names = ["w1p1", "w1p2", "w2p1", "w2p2", "w3p1", "w3p2", "w4p1", "w4p2", "w5p1", "w5p2"]
    
    num_students = []
    # Go through each of the modules 
    for problem_name in problem_names: 
        df = pd.read_csv(challenge_name + "-" + problem_name + ".csv")
        num_students.append(len(df))

    print(sum(num_students)/len(num_students))
