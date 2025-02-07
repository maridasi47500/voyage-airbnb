# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Stuff(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.tablename="stuff"
        self.cur.execute("""create table if not exists stuff(
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
    def getall1(self,myid):
        self.cur.execute("select "+self.tablename+".*, '"+self.tablename+"' as stuff from "+self.tablename+" where "+self.tablename+".region_id = ?", (myid,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from stuff")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from stuff where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getallbyregionid(self,myid):
        self.cur.execute("select * from "+self.tablename+" where region_id = ?",(myid,))
        job=self.cur.fetchall()
        return job
    def getbyid(self,myid):
        self.cur.execute("select * from stuff where id = ?",(myid,))
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
          self.cur.execute("insert into stuff (region_id,type,name,user_id,description,lat,lon) values (:region_id,:type,:name,:user_id,:description,:lat,:lon)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["stuff_id"]=myid
        azerty["notice"]="votre stuff a été ajouté"
        return azerty




