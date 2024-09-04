import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PROBLEM 2 AND 4 COMBINED

#read sheet named pythonF, skip first row if needed
dF=pd.read_excel("ExcelData.xlsx",'pythonF')
F=open('output_results.txt','w')
F.write("Count of students in Different Ranges:" +"\n")

# Range of Grades
zeroGrade = dF[dF['Grade'] == 0]
zeroGradeRange = zeroGrade.shape[0]
print(f"0 : {zeroGradeRange}")
F.write("0 : " + str(zeroGradeRange) + "\n")

i = 1
k = 0
while k < 4:
    Grade_range = dF[(dF['Grade']  >= i ) & (dF['Grade'] <= i + 9)]
    gRange = Grade_range['Grade'].count()
    print (i,"-",i+9, ":",gRange)
    F.write(str(i) + "-" + str(i+9) + ": " + str(gRange) +"\n")
    i = i + 10
    k += 1

# Number of students
numberOfStudents = dF['ID'].shape[0]
print (f"Total Number of students: {numberOfStudents}")
F.write("The Number of students : " + str(numberOfStudents) + "\n")

# Average Grade
gradeInfo = dF['Grade'].describe()
print("Average Grade:", round(gradeInfo['mean'],2))
F.write("Average Grade: " + str(round(gradeInfo['mean'],2)) + "\n"
        )
#IDs with Highest Grades
highestGrade = dF['Grade'].max()
topStudents = dF[dF['Grade'] == highestGrade]
idList = [int(id) for id in topStudents['ID'].values]
print(f"IDs with Highest Grade: {idList}")
F.write("IDs with Highest Grade:" + str(idList) + "\n")

# Oldest student age
print("The oldest student has the age of:", dF['Age'].max())
F.write("The oldest student has the age of: " + str(dF['Age'].max()) + "\n")

#Student average
print("The student age average is:", round(dF['Age'].mean(),2))
F.write("The student age average is:" + str(round(dF['Age'].mean(),2)) + "\n")

# Student age mode
print("The student age mode is:",dF['Age'].mode().iloc[0])
F.write("The student age mode is:" + str(dF['Age'].mode().iloc[0]) + "\n")

F.close()
# PROBLEM 3
sizes = [12.3, 21.1, 35.1, 8.8, 22.8]
labels = ["0", "1-10", "11-20", "21-30", "31-40"]
colors=['yellow', 'lightgreen', 'salmon', 'skyblue', 'red']

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(sizes,labels=labels, colors=colors, autopct='%1.1f%%', startangle=150)

ax.axis('equal')

plt.show()

histData = []
for x in dF['Grade']:
    histData.append(x)

plt.hist(histData, bins= dF['Grade'].max(), alpha=0.5)
plt.xticks(ticks=np.arange(0, 41, 2))

plt.title('Grade Distribution Historgram')
plt.xlabel('Grade ranges from 0  to 40')
plt.ylabel('Number of students')

plt.show()




