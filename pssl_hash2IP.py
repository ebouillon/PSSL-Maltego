#############################################
# PSSL API Cert Hash to IP
# 
# Author: Emmanuel Bouillon
# Email:  emmanuel.bouillon.sec@gmail.com
# Date: 11/06/2015
#############################################
import sys
import json
import pypssl
from pssl_util import *

if __name__ == '__main__':
        cert_hash = sys.argv[1]
        mt = MaltegoTransform()
        mt.addUIMessage("[INFO] " + cert_hash + " to IP")
        try:
            retrieveIP(mt, cert_hash)
        except Exception as e:
            mt.addUIMessage("[Error] " + str(e))
        mt.returnOutput()


