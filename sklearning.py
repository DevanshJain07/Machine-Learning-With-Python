import sklearn
from sklearn import tree
'''
feature=[[190,1,1],[180,1,1],[100,0,0],[90,0,0]]
label=['apple','apple','orange','orange']
clf=tree.DecisionTreeClassifier()
trained=clf.fit(feature,label)
result=trained.predict([[150,0,]])
print(result)
'''
'''
feature=[[0,1,2,1],[0,1,2,2],[1,1,2,1],[2,1,2,1],[2,0,0,1],[2,0,0,2],[1,0,0,2],[0,1,1,1],[0,0,0,1],[2,1,1,1],[0,0,1,2],[1,1,1,2],[1,0,2,1],[2,1,1,2]]
label=['drug A','drug A','drug B','drug B','drug B','drug A','drug B','drug A','drug B','drug B','drug B','drug B','drug B','drug A']
clf=tree.DecisionTreeClassifier()
trained=clf.fit(feature,label)
result=trained.predict([[1,1,0,1]])
print(result)
'''
from sklearn.linear_model import LinearRegression

x=[[1975,5],[1979,7],[1983,8],[2003,4],[2015,5]]
y=[5,6,10,2,1]
    
lr=LinearRegression()
    
trained=lr.fit(x,y)
    
res=trained.predict([[2019,10]])
print(res)
