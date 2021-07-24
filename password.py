# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 09:30:27 2021

@author: Mahesh B
"""

import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    a=requests.get(url)
    if a.status_code != 200:
        raise RuntimeError(f'error:{a.status_code},try again')
    return a    

def print_res(hashes,hashtocheck):
    hashes=(line.split(':')for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hashtocheck:
         return count
    return 0
    
    

def pwned_api_check(password):
    b=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    c,d=b[:5],b[5:]
    response=request_api_data(c)
    return print_res(response,d)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count}')
        else:
            print(f'{password} was not found')
    
if __name__ == '__main__':
      main(sys.argv[1:])
    

