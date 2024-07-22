# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from stuff import Stuff
class Activities(Stuff):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.tablename="activities"
        self.cur.execute("""create table if not exists activities(
        id integer primary key autoincrement,
        region_id text,
            type text,
            name text,
            user_id text,
            description text,
            lat text,
            lon text
    , MyTimestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from activities")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from activities where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from activities where id = ?",(myid,))
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
          self.cur.execute("insert into activities (region_id,type,name,user_id,description,lat,lon) values (:region_id,:type,:name,:user_id,:description,:lat,:lon)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["activities_id"]=myid
        azerty["notice"]="votre activities a été ajouté"
        return azerty




