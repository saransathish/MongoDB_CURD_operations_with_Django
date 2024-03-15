from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.environ['mongodb_url'])
db = client.sample_analytics
coll = db.accounts

def index(request):
    return HttpResponse(client.list_database_names())
    return HttpResponse('hello world')



