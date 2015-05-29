from bs4 import BeautifulSoup
from indeed import IndeedClient
from indeedkey import iclient #keeping my credentials out of git
from pymongo import MongoClient
from subprocess import call

basePath = '/mnt/data/Python/indeed/'

job_list = ["machine learning", "technology", "AI",
           "director technology", "data mining",
           "research technology", "data scientist",
           "python", "business analytics"]

try:
    serverCall = call([basePath+'db/bin/mongod -f '+basePath+'db/mongodb.conf'],shell=True)
except:
    pass

client = MongoClient('localhost', 27020)
db = client.job
indeed = db.indeed

class QueryIndeed(object):
    """Main Indeed Stub"""

    json_results = []

    def __init__(self, keyWord):
       self.params = {}
       self.params['l'] = "75057"
       self.params['radius'] =  "25"
       self.params['fromage'] =  "1"
       self.params['userip'] =  "71.164.153.200"
       self.params['useragent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
       self.params['q'] = keyWord

    def runSearch(self):
        """ run query via indeed lib, catch errors"""
        self.json_results = iclient.search(**self.params)

for job_title in job_list:
    job_group = QueryIndeed(job_title)
    job_group.runSearch()
    indeed.insert(job_group.json_results)
