# H1B statistics
The following code is intended to analyze data obtained from [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis) and available in /input folder as **H1B_FY_2016.csv**.  In particular, the code will extract statistics for the most approved H1B visa from states and occupations column.  Running **run.sh** yields top 10 states/occupations for certified visa applications and saved in **top_10_states.txt** and **top_10_occupations.txt** in /output folder.  The main file can be found in h1b_counting.py under /src folder.  

**Note:** The column header name is different for each year.  Modify h1b_counting.py accordingly or make it a user input.    
