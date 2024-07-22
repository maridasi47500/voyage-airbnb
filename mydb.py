from country import Country
from user import User
from post import Post
from job import Job
from song import Song
from chercherimage import Chercherimage
from depense import Depense
from topexperience import Topexperience
from island import Island
from region import Region
#stuff 
from activities import Activities
from sights import Sights
from drinking import Drinking
from tour import Tour
from festivals import Festivals
from entertainment import Entertainment
from eating import Eating
from shopping import Shopping
from sleeping import Sleeping
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
    self.Island=Island()
    self.Region=Region()
    self.Activities=Activities()
    self.Sights=Sights()
    self.Drinking=Drinking()
    self.Tour=Tour()
    self.Festivals=Festivals()
    self.Entertainment=Entertainment()
    self.Eating=Eating()
    self.Shopping=Shopping()
    self.Sleeping=Sleeping()
