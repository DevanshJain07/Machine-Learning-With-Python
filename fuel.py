import sklearn
from sklearn import tree
from sklearn.linear_model import LinearRegression
    
x=[[2.0,4,8.5],[2.4,4,9.6],[1.5,4,9.6],[3.5,6,11.1],[3.5,6,10.6],[3.5,6,10.0],[3.5,6,10.1],[3.7,6,11,1],[3.7,6,11.6]]
y=[196,221,136,255,244,230,232,255,267]
    
lr=LinearRegression()
    
trained=lr.fit(x,y)
    
res=trained.predict([[2.4,4,9.2]])
print(res)

