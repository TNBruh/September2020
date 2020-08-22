import random
from flask import g
from pymongo import MongoClient
from datetime import datetime

class FractalDatabase:
    def __init__(self, address=""):
        self.client = MongoClient(address)
        self.db = self.client["fractal"]

    def GetDocuments(self, collectionName, query):
        return list(self.db[collectionName].find(query))

    def GetDocument(self, collectionName, query):
        return self.db[collectionName].find_one(query)

    def GetDocumentById(self, collectionName, objId):
        return self.db[collectionName].find_one({"_id":objId})

    def InsertDocument(self, collectionName, data):
        return self.db[collectionName].insert_one(data).inserted_id

    def InsertDocuments(self, collectionName, lstData):
        self.db[collectionName].insert_many(lstData)

    def UpdateDocument(self, collectionName, query, newData):
        self.db[collectionName].update_one(query, {"$set" : newData})

    def UpdateDocumentById(self, collectionName, objId, newData):
        self.db[collectionName].update_one({"_id" : objId}, {"$set" : newData})

    def DeleteDocument(self, collectionName, query):
        self.db[collectionName].delete_one(query)

    def DeleteDocumentById(self, collectionName, objId):
        self.db[collectionName].delete_one({"_id" : objId})

    def DeleteDocuments(self, collectionName, query):
        self.db[collectionName].delete_many(query)

    def GenerateNumId(self, collectionName):
        while True:
            currentNumId = random.randint(0, 999999)
            currentNumId = str(currentNumId)
            currentNumId = "0"*(6-len(currentNumId))+currentNumId
            if(self.getADocument(collectionName, {"num_id" : currentNumId}) is None):
                return currentNumId

    def Close(self):
        self.client.close()

def GetDB():
  if "db" not in g:
    g.db = FractalDatabase("mongodb+srv://PemiluUNJ:Harambe1234@pemiluunj.cbtxd.azure.mongodb.net/test")

  return g.db




