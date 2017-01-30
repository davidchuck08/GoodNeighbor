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
from DbConnection import DbConnection

class userDb():
    def __init__(self):
        self.dbConnection = DbConnection(27017)
        self.db = self.dbConnection.getDbConnection('user')
    
    def createUser(self, userInfo):
        found = self.db.find_one({'userId' : userInfo['userId']})
        if found:
            print 'The user name already exists'
            return
        self.db.insert(userInfo)
    def getUserById(self, userIdList):
        result =[]
        for userId in userIdList:
            res = self.db.find_one({'userId':userId})
            if res is not None:
                result.append(res)
                # only take the first hit rule
        return result
    

#testDB = userDb()
#testDB.createUser({'userId':'tester1'})
#print testDB.getUserById( ['tester1'])
