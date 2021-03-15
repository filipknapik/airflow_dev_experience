import requests
import re

files = ['https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/bigquery.html']
#,
#'https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/datafusion.html',
#'https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/automl.html']

toRemove = ['<span class="o">','<span class="n">','<span class="p">','<span class="mf">','<span class="kc">',
    '<span class="mi">','<span class="sa">','<span class="si">','</span>','<span>','<pre>',
    '<div class="highlight">','<span class="s2">','<span class="c1">','<span class="s1">']

entries = []

def addEntry(newEntry):
    entries.append(newEntry)

def downloadFile(url):
    r = requests.get(url, allow_redirects=True)
    return r.content.decode("utf-8") 

def processURLs(files):
    for inpfile in files:
        fileStr = downloadFile(inpfile)
        for removeItem in toRemove:
            fileStr = fileStr.replace(removeItem, '')
        fileStr = fileStr.replace("&quot;","'")
        fileStr = fileStr.replace("\n","'")
        fileStr = fileStr.replace("&#39","'")
        allItems = re.findall(r"<div class=\"highlight-python notranslate\">(.*?)</pre", fileStr)
    
        for item in allItems:
            newEntry = {}
            body = re.findall(r" = (.*?)$", item)[0]

            methodName = body[:body.find("(")]
            
            body = body.replace("'    ","\n    ")
            body = body.replace(",')''","\n)\n\n")
            body = body.replace(",')'","\n)")
            body = body.replace("')'","\n)")
            body = body.replace('\';','\'')
            body = body.replace('\'\'','\'')
            body = body.replace(')\'',')')

            if len(methodName)>0 and ("Operator" in methodName or "Sensor" in methodName):
                newEntry['method'] = methodName
                
                searchFor = " = "+methodName+"("
                position = fileStr.index(searchFor)
                if(position>0):
                    beginning = fileStr[1:position]
                    linkStart = beginning.rindex("class=\"headerlink\"")
                    theLink = beginning[linkStart:]
                    theLink = theLink[:theLink.index(">")]
                    properties = theLink.split(" ")
                    for prop in properties:
                        if(prop.find("href=")>=0):
                            tag = prop.replace("href=","")
                            tag = tag.replace("\"","")
                            finalLink = inpfile + tag
                            newEntry['link'] = finalLink
                    newEntry['body'] = body
                    addEntry(newEntry)

def html_encode(s):
    htmlCodes = (
            ('&#39;',"'"),
            ('&quot;','"'),
            ('&#10;','\n')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

def createPyCharm(entries):
    buffer = ""
    buffer += "<templateSet>\n"

    pycharmTemplateFile = open("pycharmTemplate.txt", "r")
    pycharmTemplate = pycharmTemplateFile.read()

    for theEntry in entries:
        value = html_encode(theEntry['body']+"\n# Reference available at: " + theEntry['link'])
        newEntry = pycharmTemplate
        newEntry = newEntry.replace("#value",value)
        newEntry = newEntry.replace("#method",theEntry['method'])
        buffer += newEntry
    buffer += "</templateSet>"

    AirflowFile = open("Airflow.xml", "w")
    AirflowFile.write(buffer)
    return

processURLs(files)
createPyCharm(entries)
