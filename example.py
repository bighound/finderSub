#!/usr/bin/python3

import argparse
import requests
import urllib3.exceptions
import errno
from socket import error as socket_error
from termcolor import colored
from urllib3.exceptions import HTTPError as BaseHTTPError

urlsOkHttp=[]
urlsOkHttps=[]
urlsProbHttp=[]
urlsProbHttps=[]
urlsNotOk=[]

def check_url(line, url):
    try:
        r = requests.head(url,allow_redirects=True,timeout=2)
        if r.status_code == 200 or r.status_code == 404:
            if "https" in url:
                urlsOkHttps.append(line.strip())
            else:
                urlsOkHttp.append(line.strip())

            print(colored("[+] Subdomain/Domain {} is active!".format(line.strip()),'green'))
        if r.status_code == 403:
            if "https" in url:
                 urlsProbHttps.append(line.strip())
            else:
                 urlsProbHttp.append(line.strip())

            print(colored("[!] Subdomain/Domain {} access is Forbidden".format(line.strip()),'yellow'))
        if r.status_code == 301 or r.status_code == 302 or r.status_code == 307 or r.status_code == 308:
            print(" <<<REDIRECTED>>>    -->   {}".format(line.strip()))
            if "https" in url:
                 urlsOkHttps.append(line.strip())
            else:
                 urlsOkHttp.append(line.strip())
        else:
            urlsNotOk.append(line.strip())
            print ("[-] Server {} is not found".format(line.strip()))

    except socket_error:
        print ("Failed to establish a new connection with the active {}".format(line.strip()))
    except requests.exceptions.Timeout:
        print ("[X] Server {} is not active".format(url))
    except requests.exceptions.SSLError:
        print ("Error with the SSL Certificate with the active {}".format(line.strip()))

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--file', '-f', dest='file', help='file help')
    args = parser.parse_args()

    file=args.file

    with open(file) as f:
        for line in f:
            url="http://{}".format(line.strip())
            check_url(line, url)
            url="https://{}".format(line.strip())
            check_url(line, url)

        for i in range(1,15):
            print("\n")


        print(colored("[+] Let's hunt to this subdomains to get the Rewards!!","yellow"))
        for u in urlsOkHttp:
            print(colored(u,'green'))

        for u in urlsOkHttps:
            print(colored(u,'green'))


        print("    - URLS with 403 status code:")
        for e in urlsProbHttp:
            print(colored(e,'green'))

        for e in urlsProbHttps:
            print(colored(e,'green'))

if __name__ == '__main__':
    main()
