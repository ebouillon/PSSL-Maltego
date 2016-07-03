#############################################
# PSSL API IP to Cert Hash
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
        ip = sys.argv[1]
        mt = MaltegoTransform()
        mt.addUIMessage("[INFO] " + ip + " to Cert Hash")
        try:
            retrieveHash(mt, ip)
        except Exception as e:
            mt.addUIMessage("[Error] " + str(e))
        mt.returnOutput()


