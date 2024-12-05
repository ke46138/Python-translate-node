from flask import Flask
from googletrans import Translator

app = Flask("translateNode")
t = Translator()

@app.route("/translate/api/rus/<query>")
def toRus(query):
    try:
        bytes_string = query.encode('latin1')
        corrected_string = bytes_string.decode('windows-1251')
        print("Before: " + corrected_string)
        tempB = corrected_string.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="ru")
        return temp.text
    except:
        print("Before: " + query)
        tempB = query.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="ru")
        return temp.text
    

@app.route("/translate/api/eng/<query>")
def toEng(query):
    try:
        bytes_string = query.encode('latin1')
        corrected_string = bytes_string.decode('windows-1251')
        print("Before: " + corrected_string)
        tempB = corrected_string.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="en")
        return temp.text
    except:
        print("Before: " + query)
        tempB = query.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="en")
        return temp.text

@app.route("/translate/api/ger/<query>")
def toGer(query):
    try:
        bytes_string = query.encode('latin1')
        corrected_string = bytes_string.decode('windows-1251')
        print("Before: " + corrected_string)
        tempB = corrected_string.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="de")
        return temp.text
    except:
        print("Before: " + query)
        tempB = query.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="de")
        return temp.text

@app.route("/translate/api/fre/<query>")
def toFre(query):
    try:
        bytes_string = query.encode('latin1')
        corrected_string = bytes_string.decode('windows-1251')
        print("Before: " + corrected_string)
        tempB = corrected_string.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="fr")
        return temp.text
    except:
        print("Before: " + query)
        tempB = query.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="fr")
        return temp.text

@app.route("/translate/api/ita/<query>")
def toIta(query):
    try:
        bytes_string = query.encode('latin1')
        corrected_string = bytes_string.decode('windows-1251')
        print("Before: " + corrected_string)
        tempB = corrected_string.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="it")
        return temp.text
    except:
        print("Before: " + query)
        tempB = query.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="it")
        return temp.text

@app.route("/translate/api/pol/<query>")
def toPol(query):
    try:
        bytes_string = query.encode('latin1')
        corrected_string = bytes_string.decode('windows-1251')
        print("Before: " + corrected_string)
        tempB = corrected_string.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="pl")
        return temp.text
    except:
        print("Before: " + query)
        tempB = query.replace("&", " ")
        print("After: " + tempB)
        temp = t.translate(tempB, dest="pl")
        return temp.text
app.run(port=8001, host='0.0.0.0')