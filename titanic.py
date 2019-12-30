
import pandas as pd
'''
url="https://tinyurl.com/titanic-csv"
dataframe=pd.read_csv(url)
a=dataframe.head()
print(dataframe)
'''

dataframe=pd.DataFrame()
dataframe['name']=['ram','raja']
dataframe['roll']=[20,25]
dataframe["area"]=["gunter","ap"]
new1=pd.Series(["surya",23,"ap"],index=["name","roll","area"])
dataframe=dataframe.append(new1,ignore_index=True)
dataframe.to_csv('Name_of_file.csv',index=False,header=False)
'''
dataframe=dataframe[(dataframe['area']=="ap")&(dataframe["name"]=="raja")]
dataframe=dataframe["name"].replace("raja","gopal").head()
dataframe=dataframe.rename(columns={"name":"iot"})
dataframe=dataframe["area"].unique()
'''
