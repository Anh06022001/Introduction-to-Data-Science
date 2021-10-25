#!/usr/bin/env python
# coding: utf-8

# In[308]:


# Task 2
def check_id(id_number):
    num = 0
    for _ in id_number:
        if (_.isalpha()):
            num+=1
    if (num==1 and len(id_number)==9 and id_number[0]=='N'):
        return True
    else:
        return False
    

def check_valid(f):
    count=0
    valid = 0
    print('\n**** ANALYZING ****')
    for line in f:
        check = True
        count+=1
        line_read = line.split(',')
        if (len(line_read)!=26):
            print('Invalid line of data: does not contain exactly 26 values')
            print(line)
            check=False
        if (check_id(line_read[0])==False):
            print('Invalid line of data: N# is invalid')
            print(line)
            check=False
        if (check==True):
            valid += 1
    if (valid==count):
        print('No errors found!')
    print('\n**** REPORT ****')
    print('Total valid lines of data: ',valid)
    print('Total invalid lines of data',count-valid)
    f.seek(0)
    
# Task 3
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
def calculate_grade(answer_key,line):
    total = 0
    answer = answer_key.split(',')
    for i in range(len(answer)):
        if (line[i]==answer[i]):
            total += 4
        elif (line[i]!=answer[i] and line[i]!=''):
            total -= 1
        else:
            total += 0
    return total
    

def calculate_grade_dict(f, answer_key):
    grade_dict = {}
    for line in f:
        line = line.strip()
        line_read = line.split(',')
        if (len(line_read)==26 and check_id(line_read[0])==True):
            line_use = line_read[1:]
            grade = calculate(answer_key,line_use)
            grade_dict[line_read[0]]=grade
    return grade_dict

def calculate_metrics(f, answer_key):
    score_array = np.array([])
    grade_dict = calculate_grade_dict(f, answer_key)
    for key, value in grade_dict.items():
        score_array = np.append(score_array,value)
    print('Mean (average) score: ', np.mean(score_array))
    print('Highest score: ', np.max(score_array))
    print('Lowest score: ', np.min(score_array))
    print('Range of scores: ', np.max(score_array)-np.min(score_array))
    print('Median score: ', np.median(score_array)) 

# Task 4
import pandas as pd
import numpy as np

def convert_file(file,answer_key,filename):
    grade_dict = calculate_grade_dict(file, answer_key)
    grade_items = grade_dict.items()
    grade_list = list(grade_items)

    data = pd.DataFrame(grade_list)
    name_to_save = filename+'_grades'+'.txt'
    data.to_csv(name_to_save,index=False,header=False) 
    
# Task 1
import pandas as pd
import numpy as np
filename = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
filename_appended = filename + '.txt'
try:
    file = open(filename_appended,"r")
    print('Successfully opened ',filename_appended)
    check_valid(file)
    calculate_metrics(file,answer_key) 
    convert_file(file,answer_key,filename)
except IOError:
    print('File cannot be found')

