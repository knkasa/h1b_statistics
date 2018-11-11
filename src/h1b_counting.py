# main python file

# extract column
def extract_col(data,col_num,col_num0):
	name = []
	for n in range(1,len(data)):
	
		if data[n][col_num0] == 'CERTIFIED' :
			bin = [ data[n][col_num], 1 ]
			name.append(bin)
	return name

# counting and storing in dictionary	
def count_name(col):
	result = {}
	for k,v in col:
		if k in result:
			result[k] += v
		else:
			result[k] = v
	return result

#---------------------------------------------------
	
f = []
with open('./input/H1B_FY_2016.csv', encoding='utf-8') as f0:
	f = f0.readlines()

# converting each line into list separated by semicolumn
data = []
for line in f:
    data_line = line.rstrip().split(';')
    data.append(data_line)
	
#print('Enter column name for STATE:')
#col_name1 = input()  
#print('Enter column name for OCCUPATION:')
#col_name2 = input()  
#print('Enter column name for CERTIFIED:')
#col_name0 = input()  

col_name1 = 'EMPLOYER_STATE'
col_name2 = 'JOB_TITLE'
col_name0 = 'CASE_STATUS'

# determining column integer for extracting
head = data[0][:]
for n in range(len(head)):
	if head[n]==col_name1:
		col_num1=n
	elif head[n]==col_name2:
		col_num2=n
	elif head[n]==col_name0:
		col_num0=n
	
# taking strings from column that contains CERTIFIED
col1 = extract_col(data,col_num1,col_num0)
col2 = extract_col(data,col_num2,col_num0)

total_st = len(col1)
total_emp = len(col2)

# counting unique string
dict1 = count_name(col1)
dict2 = count_name(col2)

# sorting (desending)
dict1_sort = [(k, dict1[k]) for k in sorted(dict1, key=dict1.get, reverse=True)]
dict2_sort = [(k, dict2[k]) for k in sorted(dict2, key=dict2.get, reverse=True)]

# keeping only top 10
dict1_sort = dict1_sort[0:10]
dict2_sort = dict2_sort[0:10]

with open('./output/top_10_states.txt', 'w') as f:
		f.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
		for name, val in dict1_sort:
			f.write("%s;%i;%2.1f%%\n" % (name, val, round(val/total_st*100,1)  )  )
			
with open('./output/top_10_occupations.txt', 'w') as f:
		f.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
		for name, val in dict2_sort:
			f.write("%s;%i;%2.1f%%\n" % (name, val, round(val/total_emp*100,1)  )  )	
		
		