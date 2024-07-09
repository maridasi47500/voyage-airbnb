# coding=utf-8
import sqlite3
import sys
import re
from model import Model
import requests
from bs4 import BeautifulSoup
import urllib.request
from country import Country
class User(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists user(
        id integer primary key autoincrement,
        username text,
        country_id text,
        sex text,
        job text,
        phone text,
        email text,
lat text,
lon text,
            password text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from user")

        row=self.cur.fetchall()
        return row
    def updatelocation(self,latitude,longitude,myid):

        self.cur.execute("update user set latitude = ?, longitude = ? where id = ?",(latitude, longitude, myid,))

        self.con.commit()
        job=self.cur.lastrowid
        self.cur.execute("select * from user where id = ?",(myid,))
        job1=self.cur.fetchone()
        print(dict(job1))
        
        return job1["latitude"] == latitude and job1["longitude"] == longitude
    def deletebyid(self,myid):

        self.cur.execute("delete from user where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyphonepw(self,email,pw):
        self.cur.execute("select * from user where phone like ? and password = ?",(email,pw,))
        azerty=self.cur.fetchone()
        row=dict({})
        if azerty:
          row=dict(azerty)
          row["user_id"]=row["id"]
          row["notice"]="Vous êtes connecté(e)"
          print(row["id"], "row id")
        else:
          row=dict({})
          row["notice"]="le numero de téléphone ou le mot de passe ne sont pas bon"
          row["user_id"]=""
        return row
    def getbyid(self,myid):
        try:
           self.cur.execute("select user.*, m.name as instrumentdemusique,m.unicode as iconmusic, country.name as pays from user left join country on country.id = user.country_id left join musicalinstrument m on m.id = user.instrument_id where user.id = ? ",(myid,))
           row=dict(self.cur.fetchone())
           print(row["id"], "row id")
           job=self.cur.fetchall()
           return row
        except Exception as e:
           print(e)
           return None
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
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
        azerty={}



        try:
            if params["password"] == params["passwordconfirmation"]:
                 del myhash["passwordconfirmation"]
                 self.cur.execute("insert into user (lat,lon,instrument_id,job,sex,username,email,country_id,phone,password) values (:lat,:lon,:instrument_id,:job,:sex,:username,:email,:country_id,:phone,:password)",myhash)
                 self.con.commit()
                 myid=self.cur.lastrowid

                 azerty["notice"]="votre user a été ajouté"
                 print(azerty["notice"])
            else:
                 myid=None
                 azerty["notice"]="votre user n'a pas été ajouté les mots de passe ne sont pas identiques"
                 print(azerty["notice"])
            azerty["user_id"]=myid

        except Exception as e:
            print("my error"+str(e))
            azerty["user_id"]=None
            azerty["notice"]="votre user n'a pas été ajouté les mots de passe ne sont pas identiques"+str(e)


        return azerty




