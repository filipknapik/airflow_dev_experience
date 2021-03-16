import requests
import re

files = []

toRemove = ['<span class="o">','<span class="n">','<span class="p">','<span class="mf">','<span class="kc">',
    '<span class="mi">','<span class="sa">','<span class="si">','</span>','<span>','<pre>',
    '<div class="highlight">','<span class="s2">','<span class="c1">','<span class="s1">']

entries = []

def loadURLs(fileName):
    URLs = open(fileName, "r")
    TempFiles = URLs.readlines()
    Files = []
    for item in TempFiles:
        Files.append(item.strip())
    return Files

def addEntry(newEntry):
    entries.append(newEntry)
    return

def downloadFile(url):
    r = requests.get(url, allow_redirects=True)
    return r.content.decode("utf-8") 

def processURLs(files):
    for inpfile in files:
        print(inpfile)
        fileStr = downloadFile(inpfile)
        for removeItem in toRemove:
            fileStr = fileStr.replace(removeItem, '')
        fileStr = fileStr.replace("&quot;","'")
        fileStr = fileStr.replace("\n","'")
        fileStr = fileStr.replace("&#39","'")
        allItems = re.findall(r"<div class=\"highlight-python notranslate\">(.*?)</pre", fileStr)
    
        for item in allItems:
            newEntry = {}
            try:
                body = re.findall(r" = (.*?)$", item)[0]
            except:
                continue
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
            ('&#10;','\n'),
            ('&gt;','>'),
            ('&lt;','<')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

def createPyCharm(entries):
    buffer = ""
    buffer += "<templateSet group=\"Airflow\">\n"

    pycharmTemplateFile = open("pycharmTemplate.txt", "r")
    pycharmTemplate = pycharmTemplateFile.read()

    for theEntry in entries:
        value = html_encode(theEntry['body']+"\n# Reference available at: " + theEntry['link'] + "\n")
        newEntry = pycharmTemplate
        newEntry = newEntry.replace("#value",value)
        newEntry = newEntry.replace("#method",theEntry['method'])
        buffer += newEntry
    buffer += "</templateSet>"

    AirflowFile = open("Airflow.xml", "w")
    AirflowFile.write(buffer)
    return

def createVSCode(entries):
    buffer = "{\n"

    vscodeTemplateFile = open("vscodeTemplate.txt", "r")
    vscodeTemplate = vscodeTemplateFile.read()

    for theEntry in entries:
        value = theEntry['body']+"\n# Reference available at: " + theEntry['link'] + "\n"
        value = value.replace("\"","\\\"")
        value = value.replace("\n","\",\n\"")
        newEntry = vscodeTemplate
        newEntry = newEntry.replace("#value",value)
        newEntry = newEntry.replace("#method",theEntry['method'])
        buffer += newEntry

    buffer += "\n}"
    AirflowFile = open("python.json", "w")
    AirflowFile.write(buffer)
    return

files = loadURLs("url.txt")
processURLs(files)
createPyCharm(entries)
createVSCode(entries)