#!/usr/bin/python3

import requests

# define the URL we want to use
url = "http://0.0.0.0:2224/fast"

def main():
    # use requests library to send an HTTP GET
    for count in range(51):
        resp = requests.get(url)
    # display response
        print(resp)


if __name__ == "__main__":
    main()

