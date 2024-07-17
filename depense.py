# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from monnaie import Monnaie
class Depense(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists depense(
        id integer primary key autoincrement,
        user1_id text,
            pays2_id text,
            somme text,
            ckoi text
    , MyTimestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        self.dbMonnaie=Monnaie()
        #self.con.close()
    def getallbyuserid(self,myid):
        self.cur.execute("select depense.*,country.currency as currency,monpays.currency as monpayscurrency,monpays.name as monpaysname, country.name paysname from depense left join user on user.id = depense.user1_id left join country monpays on monpays.id = user.country_id left join country on country.id = depense.pays2_id where depense.user1_id = ?",(myid,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select depense.*,country.currency as currency,monpays.currency as monpayscurrency,monpays.name as monpaysname, country.name paysname from depense left join user on user.id = depense.user1_id left join country monpays on monpays.id = user.country_id left join country on country.id = depense.pays2_id")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from depense where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from depense where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        self.cur.execute("select country.* from country left join monnaie on country.currency like '%'+monnaie.monnaie1+'%' and (select c.currency from country c left join user u on u.country_id = c.id where u.id = ?) like '%'+monnaie2+'%' group by monnaie.id having country.id = ?",(params["user1_id"],params["pays2_id"],))
        xxx=self.cur.fetchall()
        print("telecharger la monnaie?"+("oui" if len(xxx) else "non"))
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into depense (user1_id,pays2_id,somme,ckoi) values (:user1_id,:pays2_id,:somme,:ckoi)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["depense_id"]=myid
        azerty["notice"]="votre depense a été ajouté"+(". telecharger la monnaie?"+("non" if len(xxx) > 0 else "oui"))
        monnaie1=""
        monnaie2=""
        if len(xxx) == 0 or !xxx:
            print(". telecharger la monnaie?"+("non" if len(xxx) > 0 else "oui"))
            self.execute("select country.currency left join user on user.country_id = country.id where user.id = ?",(params["user1_id"],))
            monnaie1=self.cur.fetchone()["currency"]
            self.execute("select country.currency where country.id = ?",(params["user2_id"],))
            monnaie2=self.cur.fetchone()["currency"]
            #telecharger la monnaie
        return azerty




