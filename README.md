# PSSL-Maltego
Set of Maltego transforms to interface with CIRCL Passive SSL

# Prerequisites
Python Library to access CIRCL Passive SSL (see https://www.circl.lu/services/passive-ssl/)

# INSTALL

- Edit pssl_util.py and set LOGIN and PASSWORD variables.

- Import transforms in Maltego:
   * pssl_IP2hash.py: [CIRCL] IP to SSL/TLS Hash / Returns SSL/TLS Hash for IP
   * pssl_hash2IP.py: [CIRCL] SSL/TLS Hash to IP / Returns IP using SSL/TLS Hash

