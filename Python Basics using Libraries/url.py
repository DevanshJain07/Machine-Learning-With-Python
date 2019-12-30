import urllib
try:
    output=urllib.request.urlopen("https://www.google.com/search?q=python")
    headers={}
    headers['User-Agent']="Chrome/24.0.1312.25"
    output=urllib.request.urlopen("https://www.google.com/search?q=python",headers=headers)
    res=urllib.request.urlopen(output)
    print(res.read())
    
    print(output.read())
except Exception as e:
    print(str(e))
  

import urllib
import re
url="https://docs.python.org/3/tutorial/index.html"
resp=urllib.request.Request(url)
resp=urllib.request.urlopen(resp)
data=resp.read()  
paras=re.findall(r'<p>(.*?)</p>',str(data)) 
for i in paras:
    print(i)
    
    
    
