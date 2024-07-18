from country import Country
from user import User
from post import Post
from job import Job
from song import Song
from chercherimage import Chercherimage
from depense import Depense
from topexperience import Topexperience
class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.Job=Job()
    self.User=User()
    self.Song=Song()
    self.Post=Post()
    self.Chercherimage=Chercherimage
    self.Depense=Depense()
    self.Topexperience=Topexperience()
