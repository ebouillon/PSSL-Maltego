#############################################
# PSSL API miscellaneous functions.
# 
# Author: Emmanuel Bouillon
# Email:  emmanuel.bouillon.sec@gmail.com
# Date: 11/06/2016
#############################################

# BASE URL (CIRCL)
BASE_URL = 'https://www.circl.lu/'
# Login (basic auth)
LOGIN = '<YOUR LOGIN>'
# Password (basic auth)
PASSWORD = '<YOUR PASSWORD>'
# Max nb of results (otherwise Maltego gets sick)
MAX = 50

import pypssl
import json
from MaltegoTransform import *

def init():
    return pypssl.PyPSSL(base_url=BASE_URL, basic_auth=(LOGIN, PASSWORD))

def retrieveIP(mt, cert_hash):
    pssl = init()
    result = json.loads(json.dumps(pssl.query_cert(cert_hash)))
    for ip in result['seen'][:MAX]:
        me = MaltegoEntity('maltego.IPv4Address',ip);
        mt.addEntityToMessage(me);
    return

def retrieveHash(mt, ip):
    pssl = init()
    result = json.loads(json.dumps(pssl.query(ip)))
    for cert_hash in result[ip]['certificates']:
        me = MaltegoEntity('maltego.Hash',cert_hash);
        me.addAdditionalFields('notes#', 'notes', False, result[ip]['subjects'][cert_hash]['values'][0])
        mt.addEntityToMessage(me);
    return

