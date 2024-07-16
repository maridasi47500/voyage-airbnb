import json
from fichier import Fichier
from country import Country
dbPays=Country()
x=json.loads(Fichier("./public/","flag.json").lire())
for pays in x["pays"]:
    phone=""
    name=""
    unicode=""
    code=""
    currency=""
    timezone=""
    
    try:
        phone=pays["callingcode"]
    except:
        phone=""
    try:
        name=pays["country"]
    except:
        name=""
    try:
        unicode=pays["unicode"]
    except:
        unicode=""
    try:
        currency=pays["currency"]
    except:
        currency=""
    try:
        timezone=pays["timezone"]
    except:
        timezone=""

    try:
        code=pays["countrycode"]
    except:
        code=""
    dbPays.create({"name":name,"unicode":unicode,"phone":phone,"code":code,"timezone":timezone,"currency":currency})
