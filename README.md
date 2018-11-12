# Problem
The following code is intended to analyze data obtainable from [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).  Under **LCA Programs (H-1B, H-1B1, E-3)**, you will find data containing all H-1B application information for each applicants.  The following code is made to extract statistics for the most approved H1B visa from each STATES and OCCUPATIONS. 

# Approach
The main code is written in python and can be found in __`h1b_counting.py`__ under `/src` folder.  Place __`H1B_FY_2016.csv`__ file (or equivalent) in `\input` folder before running.  __`h1b_input.csv`__ is there for testing purpose.  The file and header name  is different for each year.  Modify h1b_counting.py accordingly or make it a user input.   

# Instruction
Running __`run.sh`__ yields top 10 STATES/OCCUPATIONS for certified visa applicants and saved in __`top_10_states.txt`__ and __`top_10_occupations.txt`__ in `/output` folder.  

 
