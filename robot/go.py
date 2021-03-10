import requests
import re

files = ['https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/bigquery.html',
'https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/datafusion.html',
'https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/automl.html']

toRemove = ['<span class="o">','<span class="n">','<span class="p">','<span class="mf">','<span class="kc">',
    '<span class="mi">','<span class="sa">','<span class="si">','</span>','<span>','<pre>',
    '<div class="highlight">','<span class="s2">','<span class="c1">','<span class="s1">']

def downloadFile(url):
    r = requests.get(url, allow_redirects=True)
    return r.content.decode("utf-8") 

for inpfile in files:
    fileStr = downloadFile(inpfile)
    for removeItem in toRemove:
        fileStr = fileStr.replace(removeItem, '')
    fileStr = fileStr.replace("&quot;","'")
    fileStr = fileStr.replace("\n","'")
    fileStr = fileStr.replace("&#39","'")
    allItems = re.findall(r"<div class=\"highlight-python notranslate\">(.*?)</pre", fileStr)
 
    for item in allItems:
        
        body = re.findall(r" = (.*?)$", item)[0]
        methodName = body[:body.find("(")]
        
        body = body.replace("'    ","\n    ")
        body = body.replace(",')''","\n)\n\n")
        body = body.replace(",')'","\n)")
        body = body.replace("')'","\n)")
        if len(methodName)>0:
            print("\n--"+methodName+"--")
            print(body)
    #print(allItems)