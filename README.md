# H1B statistics
The following code is intended to analyze data obtained from [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis) which is available in `/input` folder as __`H1B_FY_2016.csv`__.  In particular, the code will extract statistics for the most approved H1B visa from "states" and "occupations" column.  Running __`run.sh`__ yields top 10 states/occupations for certified visa applications and saved in __`top_10_states.txt`__ and __`top_10_occupations.txt`__ in `/output` folder.  The main file can be found in __`h1b_counting.py`__ under `/src` folder.  

**Note:** The column header name is different for each year.  Modify h1b_counting.py accordingly or make it a user input.    
