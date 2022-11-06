# Predicting Programming Progress for K-12 Students

This repository implements the Decision Tree based approach proposed for predicting student programming progress. 

## Experiments 

1) Exploratory data analysis on content slide and problem slide completion behaviours
2) Prediction of end of module outcomes using a range of classifiers 
3) Prediction of end of module outcomes using Decision Tree classifier with two feature selection methods
4) Prediction of middle of course outcomes with Gain Ratio Feature Selection 

## Implementation 

Our approach extracts slide interaction features (i.e. the degree
of interaction that a student has with the slides in each module of an online coding
course), selects the most important features, and creates a decision tree to predict how
students will perform at the end of each module.

Our approach extracts slide interaction features (i.e. the degree
of interaction that a student has with the slides in each module of an online coding
course), selects the most important features, and creates a decision tree to predict how
students will perform at the end of each module.

## Repository Structure 

The folder, 'data-processed' contains all processed data used for Experiments 2 - 4. Each sub-folder within 'data-processed' is named in reference to an experiment. Specifically, the sub-folder, 'Experiment 2 Data' contains the individual training sets for each module in the 2018 NCSS Challenge Newbies stream. The sub-folder, 'Experiment 3 Data'contains the individual training sets for each module in all streams of the 2018 NCSS Challenge. The sub-folder, 'Experiment 4 Data' contains the individual training sets for all streams (where each training vector is a student's interaction sequence for the entire stream). 

The folder, 'figures' contains all relevant figures used in the final report, such as accuracy graphs for Experiments 2-4, heat map diagrams from Experiment 1, tree diagrams from Experiment 3 and tree size diagrams from Experiment 4. 

The folder, 'results' contains the main results for this work, categorised by the experiment, with results shown for Experiments 2-4, since the results for Experiment 1 are heat maps, which are located in the 'figures' folder. Each file within the experiments folders are WEKA's output files, which can be read as a text document. In addition, the file located in 'results' named 'classification-results' contains all results from the experiments tabluated, with supporting plots where applicable. 

Lastly, the folder, 'scripts' contains all scripts used to run the experiments as well as test and validate any of the processes used in this work. The module 'Enrolments.py' processes enrolment data from the 2018 NCSS Challenge, and produces a summary of enrolment statistics. Similarly, the module 'participation.py' produces a summary of student participation within modules and streams. The module 'modules.py' performs the slide interaction data extraction process, and produces module-level and course-level training sets for classification in Experiment 2,3,4. The module 'slide_completion.py' contains the main slide interaction data extraction process, as well as implementation of Experiment 1.



 
