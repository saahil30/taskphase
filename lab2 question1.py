import pandas as pd
a={'Roll No':['1','2','3','4','5','6','7','8','9','10'],'Name':['A','B','C','D','E','F','G','H','I','J'],
'Gender':['M','M','F','M','F','F','M','F','M','F'],'Marks1':[41,33,88,74,30,98,11,78,91,59],
   'Marks2':[67,45,49,80,97,66,32,45,81,22], 'Marks3':[44,21,36,67,59,89,90,55,43,76]
       }
df=pd.DataFrame(a)
print(df)
df['Total']= df['Marks1'] + df['Marks2'] + df['Marks3']
print(df)
print("lowest marks in Marks1 "+str(df['Marks1'].min()))
print("highest marks in Marks2 "+str(df['Marks2'].max()))
print("average marks in Marks3 "+str(df['Marks3'].mean()))
t=df[df['Total']==df['Total'].max()]
print("student with highest average is \n",str(t['Name']))
f=df[df['Marks2']<40]
print(f)
