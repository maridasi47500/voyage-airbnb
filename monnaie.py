# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Monnaie(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists monnaie(
        id integer primary key autoincrement,
        monnaie1 text,
            monnaie2 text,
            value text
    , MyTimestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from monnaie")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from monnaie where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyname(self,myid,myid2):
        self.cur.execute("select * from monnaie where monnaie1 = ? and monnaie2 = ?",(myid,myid2))
        row=(self.cur.fetchone())
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from monnaie where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
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
          self.cur.execute("insert into monnaie (monnaie1,monnaie2,value) values (:monnaie1,:monnaie2,:value)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["monnaie_id"]=myid
        azerty["notice"]="votre monnaie a été ajouté"
        return azerty




