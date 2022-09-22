#!/usr/bin/python3

import requests
import sys

urls_opened_http = []
urls_opened_https = []

with open(sys.argv[1]) as f:
    for l in f.readlines():
        print("[!] Trying with http: ")
        try:
            url = "http://"+l.strip()
            r = requests.get(url)
            print(r.status_code)
            if r.status_code == 200:
                urls_opened_http.append(url)
                print("[+] {} is available".format(url))
        except Exception as err:
            print("[-] No Connection with {}".format(url))
        
        print("[!] Trying with https: ")
        try:
            url = "https://"+l.strip()
            r = requests.get(url)
            print(r.status_code) 
            if r.status_code == 200:
                urls_opened_https.append(url)
                print("[+] {} is available".format(url))
        except Exception as err:  
            print("[-] No Connection with {}".format(url))

print("The next urls are available: \n")
print("HTTP: \n")
for u in urls_opened_http:
    print(u)

print("HTTPS: \n")
for u in urls_opened_https:
    print(u)
