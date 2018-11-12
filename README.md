# Problem
The following code is intended to analyze data obtained from [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).  The code will extract statistics for the most approved H1B visa from "states" and "occupations" column. 

# Approach
The main file can be found in __`h1b_counting.py`__ under `/src` folder.  Place __`H1B_FY_2016.csv`__ file in `\input` folder before running.  __`h1b_input.csv`__ is there for testing purpose.  The column header name is different for each year.  Modify h1b_counting.py accordingly or make it a user input.   

# Instruction
Running __`run.sh`__ yields top 10 states/occupations for certified visa applications and saved in __`top_10_states.txt`__ and __`top_10_occupations.txt`__ in `/output` folder.  

 
