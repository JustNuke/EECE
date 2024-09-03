import pandas as pd
#read sheet named pythonF, skip first row if needed
dF=pd.read_excel("ExcelData.xlsx",'pythonF')

# Range of Grades

zeroGrade = dF[dF['Grade'] == 0]
zeroGradeRange = zeroGrade.shape[0]
print(f"0 : {zeroGradeRange}")
i = 1
k = 0
while k < 4:
    Grade_range = dF[(dF['Grade']  >= i ) & (dF['Grade'] <= i + 9)]
    range = Grade_range['Grade'].count()
    print (i,"-",i+9, ":",range)
    i = i + 10
    k += 1

# Number of students
numberOfStudents = dF['ID'].shape[0]
print (f"Total Number of students: {numberOfStudents}")

# Average Grade
gradeInfo = dF['Grade'].describe()
print("Average Grade:", round(gradeInfo['mean'],2))

#IDs with Highest Grades
highestGrade = dF['Grade'].max()
topStudents = dF[dF['Grade'] == highestGrade]
idList = [int(id) for id in topStudents['ID'].values]
print(f"IDs with Highest Grade: {idList}")

# Oldest student age
print("The oldest student has the age of:", dF['Age'].max())

#Student average
print("The student age average is:", round(dF['Age'].mean(),2))

# Student age mode
print("The student age mode is:",dF['Age'].mode().iloc[0])

