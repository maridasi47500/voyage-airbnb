from directory import Directory
from render_figure import RenderFigure
from geolocation import Geolocation
from user import User
from mydb import Mydb
from mymusic import Music
from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import random
import traceback
import sys
from lignecommande import Lignecommande

class Route():
    def __init__(self):
        self.dbUsers=User()
        self.Program=Directory("voyage ville par ville mois par mois")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.render_figure=RenderFigure(self.Program)
        self.db=Mydb()
        self.getparams=("id",)
    def set_post_data(self,x):
        self.post_data=x
    def get_some_post_data(self,params=()):
        x={}
        try:
          for y in params:
              print(self.post_data[y])
              x[y]=self.post_data[y][0]
        except:
          print("wow")
        return x
    def get_post_data(self):
        return self.post_data
    def set_my_session(self,x):
        print("set session",x)
        self.Program.set_my_session(x)
        self.render_figure.set_session(self.Program.get_session())

    def set_redirect(self,x):
        self.Program.set_redirect(x)
        self.render_figure.set_redirect(self.Program.get_redirect())
    def render_some_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_some_json(x)
    def render_my_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_my_json(x)
    def set_json(self,x):
        self.Program.set_json(x)
        self.render_figure.set_json(self.Program.get_json())
    def set_notice(self,x):
        print("set session",x)
        self.Program.set_session_params({"notice":x})
        self.render_figure.set_session(self.Program.get_session())
    def set_session(self,x):
        print("set session",x)
        self.Program.set_session(x)
        self.render_figure.set_session(self.Program.get_session())
    def get_this_get_param(self,x,params):
        print("set session",x)
        hey={}
        for a in x:
          hey[a]=params[a][0]
        return hey
    def get_this_route_param(self,x,params):
        print("set session",x)
        return dict(zip(x,params["routeparams"]))
    def logout(self,search):
        self.Program.logout()
        self.set_notice("vous êtes déconnecté(e)")
        self.set_redirect("/sign_in")

        return self.render_figure.render_redirect()
    def profil(self,search):
        self.render_figure.set_param("aider",random.choice(["voudra vuos aider","ne voudra pas vous aider"]))
        self.render_figure.set_param("rencontrer",random.choice(["vous voudrez rencontrer","vous voudrez quitter"]))
        self.render_figure.set_param("nb",random.choice(["seulement 1","2","20","100","200"]))
        self.render_figure.set_param("bon",random.choice(["bonnes","mauvaises"]))

        return self.render_figure.render_figure("welcome/profil.html")
    def addtopexperience(self,search):
        return self.render_figure.render_figure("welcome/addtopexperience.html")
    def addisland(self,search):
        return self.render_figure.render_figure("welcome/addisland.html")
    def adddepense(self,search):
        return self.render_figure.render_figure("welcome/adddepense.html")
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def getenregistrement(self,search):
        return self.render_some_json("welcome/somerecording.json")
    def audio_save(self,search):
        myparam=self.get_post_data()(params=("recording",))
        hi=""
        return self.render_some_json("welcome/hey.json")
    def search(self,wow):

        myparam=self.get_some_post_data(params=("search",))
        print(myparam,"P A R A M E T R E")
        s=myparam["search"]
        try:
          self.set_notice("vous avez cherché "+s)

        except:
          self.set_notice("erreur quand vous avez envoyé le formulaire")
        self.render_figure.set_param("search",s)
        return self.render_figure.render_figure("welcome/voirsearch.html")
    def shootvid(self,search):
        return self.render_figure.render_figure("welcome/shootvid.html")
    def mydiv(self,search):
        myparam=self.get_some_post_data(params=("div1","user_id"))
        hi=self.db.Link.find_by_url(url=myparam["div1"],user_id=myparam["user_id"])
        self.render_figure.set_param("url",hi)
        return self.render_some_json("welcome/myurl.json")
    def myband(self,search):
        myparam=self.get_some_post_data(params=("div1",))
        print(myparam, "my band fync")
        hi=self.db.Member.getallbybandid(myparam["div1"])
        self.render_figure.set_param("members",hi)
        return self.render_some_json("welcome/myband.json")
    def myurl(self,search):
        myparam=self.get_post_data()(params=("url","shorturl","div","user_id","band_id","member_id"))
        hi=self.db.Link.create(myparam)
        if hi:
          self.set_notice("votre article a été téléchargé")
        else:
          self.set_notice("erreur quand vous avez envoyé le formulaire")
        self.render_figure.set_param("post_id",hi["post_id"])
        return self.render_some_json("welcome/mypost.json")
    def updatelocation(self,search):
        myparam=self.get_post_data()(params=("userid","latitude","longitude",))
        hi=self.db.User.updatelocation(myparam["latitude"],myparam["longitude"],myparam["userid"])
        if hi:
          self.set_notice("votre localisation a été modifié")
        else:
          self.set_notice("erreur quand vous avez envoyé le formulaire")
        self.render_figure.set_param("url","/")

        return self.render_some_json("welcome/myurl.json")
    def updatepost(self,search):
        myparam=self.get_post_data()(params=("id","title","content",))
        hi=self.db.Post.update(myparam)
        if hi:
          self.set_notice("votre post a été modifié")
        else:
          self.set_notice("erreur quand vous avez envoyé le formulaire")
        self.render_figure.set_param("post_id",myparam["id"])
        return self.render_some_json("welcome/mypost.json")
    def aboutme(self,search):
        print("hello action")
        print("hello action")
        print("hello action")
        return self.render_figure.render_figure("welcome/aboutme.html")
    def mesdepenses(self,search):
        return self.render_figure.render_figure("welcome/mesdepenses.html")
    def hello(self,search):
        print("hello action")
        return self.render_figure.render_figure("welcome/index.html")
    def delete_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(self.getparams)
        self.render_figure.set_param("user",User().deletebyid(myparam["id"]))
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def edit_user(self,params={}):
        getparams=("id",)

        myparam=self.get_this_route_param(getparams,params)
        print("route params")
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("user/edituser.html")
    def editerpost(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("post",self.db.Post.getbyid(myparam["id"]))
        return self.render_figure.render_figure("ajouter/editerpost.html")
    def sauvernote(self,params={}):
        print(params)
        search=self.get_some_post_data(params=("note","address","user_id",))
        print(search)
        print("action translation")
        x=self.db.Note.create(search)
        self.render_figure.set_param("redirect","/")
        return self.render_some_json("welcome/redirect.json")
    def location(self,params={}):
        print(params)
        search=self.get_some_post_data(params=("lat","lon",))
        print(search)
        print("action translation")
        self.render_figure.set_param("bar",[])
        self.render_figure.set_param("restaurant",[])
        return self.render_some_json("welcome/location.json")
    def translate(self,params={}):
        print(params)
        search=self.get_some_post_data(params=("somecontent",))
        print(search)
        print("action translation")
        self.render_figure.set_param("content",Translate(search["somecontent"]).detect_and_translate("en"))
        return self.render_some_json("welcome/content.json")
    def chercherimage(self,params={}):
        getparams=("sex","country_id")
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        pays=self.db.Country.getbyid(myparam["country_id"])["name"]
        mysex="woman" if myparam["sex"] ==  "f" else "man"
        q=mysex+" "+pays+" soldier"
        self.render_figure.set_param("images",[])
        self.render_figure.set_param("q",q)
        return self.render_some_json("welcome/someimages.json")
    def ajouterjob(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        monmembre=self.db.Userfamily.getbyid(myparam["id"])
        self.render_figure.set_param("membre",monmembre)
        self.render_figure.set_param("membre_id",monmembre["member_id"])
        return self.render_figure.render_figure("ajouter/jobs.html")
    def voirpersonne(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        try:
          personn1=""
          self.render_figure.set_param("person",personn1)

          if not personn1:
            self.Program.set_code422(True);
            return self.render_some_json("ajouter/personne1.json")
          return self.render_some_json("ajouter/personne.json")
        except:
          self.Program.set_code422(True);
          return self.render_some_json("ajouter/personne1.json")
    def voirphoto(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("photo",self.db.Photo.getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/voirphoto.html")
    def seetopexperience(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("topexperience",self.Topexperience.getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/topexperience.html")
    def seeuser(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("user/voir.html")
    def myusers(self,params={}):
        self.render_figure.set_param("users",User().getall())
        return self.render_figure.render_figure("user/users.html")
    def update_user(self,params={}):
        myparam=self.post_data(self.getparams)
        self.user=self.dbUsers.update(params)
        self.set_session(self.user)
        self.set_redirect(("/seeuser/"+params["id"][0]))
    def login(self,s):
        search=self.get_post_data()(params=("phone","password"))
        self.user=self.dbUsers.getbyphonepw(search["phone"],search["password"])
        print("user trouve", self.user)
        if self.user["phone"] != "":
            print("redirect carte didentite")
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/\"}")
        else:
            self.set_json("{\"redirect\":\"/youbank\"}")
            print("session login",self.Program.get_session())
        return self.render_figure.render_json()
    def addband(self,search):

        return self.render_figure.render_figure("ajouter/band.html")
    def addmusician(self,search):

        return self.render_figure.render_figure("ajouter/musician.html")
    def ajouterenregistrement(self,search):
        getparams=("id",)

        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)

        try:
          event1="hey"
          self.render_figure.set_param("myid",myparam["id"])
          self.render_figure.set_param("event",event1)
        except:
          print("i missed event")
        return self.render_figure.render_figure("ajouter/enregistrement.html")
    def ajouterlieu(self,search):
        return self.render_figure.render_only_figure("ajouter/lieu.html")
    def ajouterhack(self,search):
        self.render_figure.set_param("personnes",[])
        self.render_figure.set_param("lieux",[])
        return self.render_figure.render_only_figure("ajouter/hack.html")
    def ajouterrumeur(self,search):
        self.render_figure.set_param("personnes",[])
        self.render_figure.set_param("lieux",[])
        return self.render_figure.render_only_figure("ajouter/rumeur.html")
    def nouveau(self,search):
        return self.render_figure.render_figure("welcome/new.html")
    def getlyrics(self,params={}):
        getparams=("id",)

       
        myparam=self.get_this_get_param(getparams,params)
        print("my param :",myparam)
        try:
          print("hey",hey)
          if not hey:
            hey=[]
        except:
          hey=[]

        self.render_figure.set_param("lyrics",hey)
        return self.render_some_json("welcome/lyrics.json")
    def jouerjeux(self,search):
        return self.render_figure.render_figure("welcome/jeu.html")

    def signup(self,search):
        return self.render_figure.render_figure("user/signup.html")
    def signin(self,search):
        return self.render_figure.render_figure("user/signin.html")
    def voirtouttopexperience(self,search):
        return self.render_figure.render_figure("welcome/voirtouttopexperience.html")

    def createisland(self,params={}):
        myparam=self.get_post_data()(params=("user_id","country_id","name"))
        x=self.db.Island.create(myparam)
        if x["island_id"]:
            print("user user1")
            self.set_notice(x["notice"])
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
        else:
            print("user user Non")
            self.set_notice("erreur pour créer votre ile ")
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
    def createtopexperience(self,params={}):
        myparam=self.get_post_data()(params=("title","content","photo"))
        x=self.db.Topexperience.create(myparam)
        if x["topexperience_id"]:
            print("user user1")
            self.set_notice(x["notice"])
            self.set_json("{\"redirect\":\"/topexperiences/"+x["topexperience_id"]+"\"}")
            return self.render_figure.render_json()
        else:
            print("user user Non")
            self.set_notice("erreur pour créer votre top experience ")
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
    def createdepense(self,params={}):
        myparam=self.get_post_data()(params=("user1_id","pays2_id","ckoi","somme"))
        x=self.db.Depense.create(myparam)
        if x["depense_id"]:
            print("user user1")
            self.set_notice(x["notice"])
            self.set_json("{\"redirect\":\"/mesdepenses\"}")
            return self.render_figure.render_json()
        else:
            print("user user Non")
            self.set_notice("erreur pour créer votre depense ")
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
    def save_user(self,params={}):
        myparam=self.get_post_data()(params=("mypic","sex","username","email","country_id","phone","password","passwordconfirmation"))
        self.user=self.dbUsers.create(myparam)
        if self.user["user_id"]:
            print("user user1")
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
        else:
            print("user user Non")
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
    def run(self,redirect=False,redirect_path=False,path=False,session=False,params={},url=False,post_data=False):
        if post_data:
            print("post data")
            self.set_post_data(post_data)
            print("post data set",post_data)
        if url:
            print("url : ",url)
            self.Program.set_url(url)
        self.set_my_session(session)

        if redirect:
            self.redirect=redirect
        if redirect_path:
            self.redirect_path=redirect
        if not self.render_figure.partie_de_mes_mots(balise="section",text=self.Program.get_title()):
            self.render_figure.ajouter_a_mes_mots(balise="section",text=self.Program.get_title())
        if path and path.endswith("png"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("mp3"):
            self.Program=Music(path)
            self.Program.set_path("./")
        elif path and path.endswith("images"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpeg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("gif"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("svg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith(".jfif"):
            self.Program=Pic(path)
        elif path and path.endswith(".css"):
            self.Program=Css(path)
        elif path and path.endswith(".js"):
            self.Program=Js(path)
        elif path:
            path=path.split("?")[0]
            print("link route ",path)
            ROUTES={
            '^/mesdepenses$': self.mesdepenses,
            '^/createtopexperience$': self.createtopexperience,
            '^/$addisland': self.addisland,
            '^/voirtouttopexperience$': self.voirtouttopexperience,
            '^/addtopexperience$': self.addtopexperience,
            '^/adddepense$': self.adddepense,
            '^/aboutme$': self.aboutme,
            '^/sign_in$': self.signin,
            '^/sign_up$': self.signup,
            '^/logmeout$':self.logout,
            '^/signup$':self.save_user,
            '^/createdepense$':self.createdepense,
            '^/save_user$':self.save_user,
            '^/update_user$':self.update_user,

            "^/seetopexperience/([0-9]+)$":self.seetopexperience,
            "^/seeuser/([0-9]+)$":self.seeuser,
            "^/edituser/([0-9]+)$":self.edit_user,
            "^/deleteuser/([0-9]+)$":self.delete_user,
            '^/login$':self.login,
            '^/users$':self.myusers,
            '^/$': self.hello
            }
            REDIRECT={"/save_user": "/welcome"}
            for route in ROUTES:
               print("pattern=",route)
               mycase=ROUTES[route]
               x=(re.match(route,path))
               print(True if x else False)
               
               if x:
                   params["routeparams"]=x.groups()
                   try:
                       html=mycase(params)
                       print("html bon")
                       #print(html)
                   except Exception as e:  
                       print("erreur"+str(e),traceback.format_exc())
                       html=("<p>une erreur s'est produite dans le code server  "+(traceback.format_exc())+"</p><a href=\"/\">retour à l'accueil</a>").encode("utf-8")
                       print("html mauvais")
                   
                   self.Program.set_html(html=html)
                   self.Program.clear_notice()
                   return self.Program
               else:
                   self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")
        return self.Program
