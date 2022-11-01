#!/usr/bin/env python3
"""
RZFeeser || Alta3 Research
Using regular expression to parse HTTPS responses
"""

import requests
import re

def main():
    # prompt user for "url" and "searchFor"
    #print(f"Welcome to the simple HTTP response parser. Where should we search (ex: https://alta3.com)?")
    #url = input()
    #if (url == 'quit'):
    #    exit()
    #else:
    #    print(f"Great! So we'll try to open this url {url} to search for the phrase:")

    #searchFor = input()
    searchFor = 'Alta3'

    # send an HTTP GET to the "url", then strip off the attached HTML data
    #searchMe = requests.get(url).text
    searchMe = requests.get('https://alta3.com').text

    if re.search(searchFor, searchMe):
        print("Found a match!")
    else:
        print("No match!")
   
    #print(searchMe) 
    print(len(re.findall(searchFor,searchMe)))

if __name__ == "__main__":
    main()

