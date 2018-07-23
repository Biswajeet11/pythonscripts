import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''

ages=re.findall(r'\d{1,3}',exampleString)
names=re.findall(r'[A-Z][a-z]*',exampleString)
print(ages)
print(names)

agedict={}
x=0
for eachname in names:
    agedict[eachname]=ages[x]
    x+=1

print(agedict)

