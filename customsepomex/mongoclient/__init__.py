from pymongo import MongoClient

import logging, os

logging.basicConfig(level=logging.INFO)

class CustomMongoClient(object):
    MONGO_HOST = os.getenv('CUSTOM_MONGO_HOST')
    MONGO_PORT = 27017
    MONGO_DATABASE = 'sepomex'
    dbInstance = None
    dbCollection = {}
    MONGO_USERNAME = os.getenv('MONGO_USERNAME')
    MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
    uri = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DATABASE}?authSource=admin'

    logging.info('Connecting :::: ', uri)

    @staticmethod
    def initialize():
        logging.debug('Opening connection')
        client = MongoClient(CustomMongoClient.uri)
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
