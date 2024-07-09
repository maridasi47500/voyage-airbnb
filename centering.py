# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Centering(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists centering(
        id integer primary key autoincrement,
        focalpoint text,
            muscles text,
            aim text,
            piece text,
            intention text,
            soundlike text,
            tryagain text,
            notes text,
            cue text,
            rating text,
            elapsedtime text,
            user_id integer
    , MyTimestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getallbyuserid(self,userid):
        self.cur.execute("select * from centering where user_id = ?",(userid,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from centering")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from centering where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from centering where id = ?",(myid,))
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
          self.cur.execute("insert into centering (focalpoint,muscles,aim,piece,intention,soundlike,tryagain,notes,cue,rating,elapsedtime,user_id) values (:focalpoint,:muscles,:aim,:piece,:intention,:soundlike,:tryagain,:notes,:cue,:rating,:elapsedtime,:user_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["centering_id"]=myid
        azerty["notice"]="votre centering a été ajouté"
        return azerty




