
from slide_completion import *
from sklearn.metrics import *
from sklearn.model_selection import *
import pandas as pd
from general_functions import * 


"""
    This function produces the module-level datasets used for classification. The function does this
    by extracting the interaction sequences for all students that have participated in the module,
    and treating the interaction seqeuences as row vectors that can be concatenated into a Data Frame
    representing the training dataset
"""
def test(challenge_name):
    file = 'events_processed.csv'
    df = pd.read_csv(file)

    df_filtered = df[(df.challenge_name == challenge_name)] 
    print(df_filtered["event_name"].unique())
    return


def module_prediction(challenge_name):

    file = 'events_processed.csv'

    # Module names 
    if challenge_name == "challenge-newbies-2018":
        problem_names = ["w1p1", "w1p2", "w2p1", "w2p2", "w3p1n", "w3p2", "w4p1", "w4p2", "w5p1", "w5p2"]
    else:
        problem_names = ["w1p1", "w1p2", "w2p1", "w2p2", "w3p1", "w3p2", "w4p1", "w4p2", "w5p1", "w5p2"]
 
    # Go through each of the modules 
    for problem_name in problem_names: 
    
        # Data to be converted into a dataframe 
        data = []

        # Inputs
        X = []
        # Outcomes 
        y = []

        # Filter the dataframe based on challenge name and module name 
        df = filter(file, challenge_name, problem_name)
        os.chdir(r"C:\Users\vince\Documents\thesis\data\events")

        if challenge_name == "challenge-newbies-2018" and problem_name == "w4p2":
            df = df[df.user_id != "c5efdcfda95bd5fdfcfe6b1a2a2eb737"]

        # Test: Work out how many slide complete events there are 
        filtered_df = df[(df.event_name == "slide_steps_complete")] 
        print(len(filtered_df))

        # The number of slides in the module (+1 to account for 0-indexing)
        num_slides = df["slide_no"].max() + 1  
        problem_slides = get_problem_slides(df, challenge_name)

        # Sort the dataset by users 
        df = df.sort_values(by=['user_id'])  
        
        # Retrieve the interaction sequences of each student in the module 
        temp_dict = get_student_dict(df, num_slides, problem_slides, challenge_name)

        # Last problem slide 
        # last_idx = problem_slides[-1]
        last_idx = problem_slides[-1]

        # Go through all students in the module 
        for student in temp_dict:

            # Row of the dataframe 
            row = []

            # Retrieve the student's interaction sequence 
            sequence = temp_dict[student]
            if problem_name == "w5p2":
                print(len(sequence))

            # Re-label the different slide interactions
            sequence[:] = [x if x != "N" else "No submission" for x in sequence]
            sequence[:] = [x if x != "F" else "Fail" for x in sequence]
            sequence[:] = [x if x != "P" else "Pass" for x in sequence]
            sequence[:] = [x if x != 0 else "No attempt" for x in sequence]
            sequence[:] = [x if x != 1 else "Completed" for x in sequence]

            # The outcome is the outcome of the last problem slide in the module 
            outcome = sequence[last_idx] 
            sequence = sequence[:last_idx]

            # Append the outcome to the list of outcomes 
            y.append(outcome)

            # Store the remaining sequence in the inputs vector 
            X.append(sequence)

            # Append the sequence to the row
            row.extend(sequence)

            # Append the outcome to the row vector 
            row.append(outcome)

            # Append the row to the dataframe 
            data.append(row)

        df = pd.DataFrame(data)
        rename_dict = {}
        columns = list(df.columns)
        for i in range(len(columns) + 1):
            if i != len(columns):
                col = columns[i]
                rename_dict[col] = "slide" + str(col)
            else:
                rename_dict[col] = "Outcome"

        df.rename(columns=rename_dict, inplace=True)
        df.to_csv("{}-{}.csv".format(challenge_name, problem_name), index=False)



