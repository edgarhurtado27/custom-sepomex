import requests
import logging
from zipfile import ZipFile

import sys, os
sys.path.append(os.path.join(sys.path[0], '..'))

from mongoclient import CustomMongoClient

logging.basicConfig(level=logging.INFO)


HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
API_ENDPOINT = "https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx"
DATA = "__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUINzcwOTQyOTgPZBYCAgEPZBYCAgEPZBYGAgMPDxYCHgRUZXh0BTnDmmx0aW1hIEFjdHVhbGl6YWNpw7NuIGRlIEluZm9ybWFjacOzbjogQWdvc3RvIDE1IGRlIDIwMjFkZAIHDxAPFgYeDURhdGFUZXh0RmllbGQFA0Vkbx4ORGF0YVZhbHVlRmllbGQFBUlkRWRvHgtfIURhdGFCb3VuZGdkEBUhIy0tLS0tLS0tLS0gVCAgbyAgZCAgbyAgcyAtLS0tLS0tLS0tDkFndWFzY2FsaWVudGVzD0JhamEgQ2FsaWZvcm5pYRNCYWphIENhbGlmb3JuaWEgU3VyCENhbXBlY2hlFENvYWh1aWxhIGRlIFphcmFnb3phBkNvbGltYQdDaGlhcGFzCUNoaWh1YWh1YRFDaXVkYWQgZGUgTcOpeGljbwdEdXJhbmdvCkd1YW5hanVhdG8IR3VlcnJlcm8HSGlkYWxnbwdKYWxpc2NvB03DqXhpY28UTWljaG9hY8OhbiBkZSBPY2FtcG8HTW9yZWxvcwdOYXlhcml0C051ZXZvIExlw7NuBk9heGFjYQZQdWVibGEKUXVlcsOpdGFybwxRdWludGFuYSBSb28QU2FuIEx1aXMgUG90b3PDrQdTaW5hbG9hBlNvbm9yYQdUYWJhc2NvClRhbWF1bGlwYXMIVGxheGNhbGEfVmVyYWNydXogZGUgSWduYWNpbyBkZSBsYSBMbGF2ZQhZdWNhdMOhbglaYWNhdGVjYXMVIQIwMAIwMQIwMgIwMwIwNAIwNQIwNgIwNwIwOAIwOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNQIyNgIyNwIyOAIyOQIzMAIzMQIzMhQrAyFnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIdDzwrAAsAZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQULYnRuRGVzY2FyZ2G2iMbH35u3WADeV8JN3PTuofYbzw%3D%3D&__VIEWSTATEGENERATOR=BE1A6D2E&__EVENTVALIDATION=%2FwEWKAKe5L2iBwLG%2FOLvBgLWk4iCCgLWk4SCCgLWk4CCCgLWk7yCCgLWk7iCCgLWk7SCCgLWk7CCCgLWk6yCCgLWk%2BiBCgLWk%2BSBCgLJk4iCCgLJk4SCCgLJk4CCCgLJk7yCCgLJk7iCCgLJk7SCCgLJk7CCCgLJk6yCCgLJk%2BiBCgLJk%2BSBCgLIk4iCCgLIk4SCCgLIk4CCCgLIk7yCCgLIk7iCCgLIk7SCCgLIk7CCCgLIk6yCCgLIk%2BiBCgLIk%2BSBCgLLk4iCCgLLk4SCCgLLk4CCCgLL%2BuTWBALa4Za4AgK%2BqOyRAQLI56b6CwL1%2FKjtBYL74Dewt%2F4T3RA0oKJjVZ0%2FcjO2&cboEdo=00&rblTipo=txt&btnDescarga.x=18&btnDescarga.y=14"

# Getting data from SEPOMEX
r = requests.post(url = API_ENDPOINT, data = DATA, headers = HEADERS)

# Saving zip file
with open(r'./customsepomex/source/salida.zip','wb') as f:
    f.write(r.content)

# Extract data
with ZipFile('./customsepomex/source/salida.zip', 'r') as myzip:
    myzip.extractall('./customsepomex/source/')

logging.info('Reading file')
zipCodesFile = open('./customsepomex/source/CPdescarga.txt', encoding='latin-1')

zipCodesMap = {}

count = 0
while True:
    count += 1
    line = zipCodesFile.readline()

    # if line is empty end of file is reached
    if not line: break

    if count > 2:
        register = {}
        data = line.strip().split('|')
        cp = data[0]

        if zipCodesMap.get(cp) is not None :
            register = zipCodesMap.get(cp)
            register.get('colonias').append(data[1])
        else :
            register = {
                "codigoPostal": cp,
                "estado": data[4],
                "municipio": data[3],
                "colonias": [data[1]]
            }
            zipCodesMap[cp] = register
logging.info('Closing file')
zipCodesFile.close()

logging.info('Begin import')

for key in zipCodesMap:
    CustomMongoClient.insertOne('zipCodes', zipCodesMap[key])


logging.info('Deleting files')
os.remove('./customsepomex/source/salida.zip')
os.remove('./customsepomex/source/CPdescarga.txt')

logging.info('Import finished')
