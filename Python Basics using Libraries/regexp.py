import re
data="""Anshu is 19 years old, Deepak is 40 years old, Sheeran is 20 years old,
Georgia is 33 years old"""
ages=re.findall(r'\d{1,3}',data)
names=re.findall(r'[A-Z][a-z]*',data)
print(ages)
print(names)


