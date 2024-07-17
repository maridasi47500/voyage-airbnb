import requests
from chaine import Chaine
from bs4 import BeautifulSoup
import urllib.request
import urllib
from country import Country
from monnaie import Monnaie
dbMonnaie=Monnaie()

class Chercherargent():
    def __init__(self,monnaie1, monnaie2):
        q="1 "+monnaie1+" to "+monnaie2
       self.someparams={"q":q}
       print(q,"q")
    def search(self):
       html = requests.get("https://www.google.com/search", params=self.someparams)
       soup = BeautifulSoup(html.text, 'html.parser')
       malist=soup.select("curr_totxt")
       wow=[]
       ye={}
       for k in malist:
           ye={}
           ye["value"]=k.get_text()
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
for x in dbCountry.getall():
  try:
    pays1=x["currency"].split(", ")[1].split(")")[0]
  except:
    continue
  for y in dbCountry.getall():
    try:
      pays2=y["currency"].split(", ")[1].split(")")[0]
      dbMonnaie.create({"monnaie1":pays1,"monnaie2":pays2,"value":value})
    except:
      continue
