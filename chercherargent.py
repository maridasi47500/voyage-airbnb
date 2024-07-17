import requests
from chaine import Chaine
from bs4 import BeautifulSoup
import urllib.request
import urllib
from country import Country
from monnaie import Monnaie
dbMonnaie=Monnaie()
import json


class Chercherargent():
    def __init__(self,monnaie1 = "", monnaie2 = ""):
       self.someparams={"Amount":"1","From":monnaie1,"To":monnaie2}
       print(self.someparams)
    def search(self):
       html = requests.get("https://www.xe.com/fr/currencyconverter/convert/", params=self.someparams)
       soup = BeautifulSoup(html.text, 'html.parser')
       k=soup.select("table td")[1]
       wow=[]
       ye={}
       ye={}
       ye["value"]=k.get_text().split(" ")[0]
       wow.append(ye)
       return wow
    def dlpic(self):
       ok=self.search()
       ok1=[]
       xx={"src":"","q":"","nom":""}
       if len(ok) > 0:
           xx=ok[0]
           opener=urllib.request.build_opener()
           opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
           urllib.request.install_opener(opener)
           filename=xx["src"].split("/")[-1].split("?")[0]
           nom=Chaine().fichier(filename)
           urllib.request.urlretrieve(xx["src"], f'./uploads/'+nom)
           xx["nom"]=nom
           return xx
       else:
           return xx
           

dbCountry=Country()
pays1=""
pays2=""
value=""
azerty=""
wow1=[]
#for x in dbCountry.getall():
#  try:
#    pays1=x["currency"].split(", ")[1].split(")")[0]
#  except:
#    print("erreur",pays1,pays2)
#    continue
#  for y in dbCountry.getall():
#    try:
#      pays2=y["currency"].split(", ")[1].split(")")[0]
#      azerty=Chercherargent(pays1,pays2).search()
#      print(azerty)
#      value=azerty[0]["value"]
#      wow1.append({"monnaie1":pays1,"monnaie2":pays2,"value":value})
#      dbMonnaie.create({"monnaie1":pays1,"monnaie2":pays2,"value":value})
#    except Exception as e:
#      print("erreur",pays1,pays2,e)
#      continue
#with open('public/argent.json', 'w') as f:
#    json.dump({"monnaies":wow1},f)
