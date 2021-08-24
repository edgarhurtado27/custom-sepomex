from pymongo import MongoClient

import logging

logging.basicConfig(level=logging.INFO)

class CustomMongoClient(object):
    MONGO_HOST = 'mongo'
    MONGO_PORT = 27017
    MONGO_DATABASE = 'sepomex'
    dbInstance = None
    dbCollection = {}

    @staticmethod
    def initialize():
        logging.debug('Opening connection')
        client = MongoClient(CustomMongoClient.MONGO_HOST, CustomMongoClient.MONGO_PORT)
        CustomMongoClient.dbInstance = client[CustomMongoClient.MONGO_DATABASE]

    @staticmethod
    def getCollection(collectionName):
        if CustomMongoClient.dbInstance is None : CustomMongoClient.initialize()

        if CustomMongoClient.dbCollection.get(collectionName) is not None :
            return CustomMongoClient.dbCollection.get(collectionName)

        logging.debug('Fetching collection')
        collection = CustomMongoClient.dbInstance[collectionName]
        CustomMongoClient.dbCollection[collectionName] = collection
        return collection

    @staticmethod
    def insertOne(collectionName, data):
        logging.debug('Inserting ', data)
        collection = CustomMongoClient.getCollection(collectionName)
        collection.insert(data)

    @staticmethod
    def findOne(collectionName, query):
        collection = CustomMongoClient.getCollection(collectionName)
        result = collection.find_one(query, {'_id' : 0 })
        return result
