#! /usr/bin/python


'''
This file defines the class to establish DB connection.  
'''
import pymongo
from pymongo import MongoClient
import json
from pprint import pprint
from array import *
import types
import re

class DbConnection():
    
    def __init__(self, portNum):
        self.client = MongoClient('localhost', portNum)
        self.db = self.client['GoodNeighbor']
        self.collection = None
    
    def getDbConnection(self, collectionName):
        self.collection = self.db[collectionName]
        return self.collection
    