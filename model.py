import sqlite3
import sys
class Model():
        mydb=db="myFileDb.db"
        con=sqlite3.connect(self.mydb)
        tablename="mytablename"
        def __init__(self):
            print("ok")
            self.con.row_factory = sqlite3.Row
            self.cur=self.con.cursor()
        def create(self,params):
            sql="insert into "+self.tablename+" ("
            values=tuple(params.values())
            paspremier=False
            for x in params:
                if paspremier:
                  sql+=","
                sql+=x
                paspremier=True
            paspremier=False
            sql+=") values ("
            for x in params:
                if paspremier:
                  sql+=","
                sql+="?"
                paspremier=True
            self.cur.execute(sql,values)
            self.con.commit()
            lastrow=self.cur.lastrowid
            return {"notice":"votre "+self.tablename+" a été créé(e)" ,(self.tablename+"_id"): lastrow}
