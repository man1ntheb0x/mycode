#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
import requests

def main():
    ## URL to post to
    url = 'http://10.11.68.58:2224/answer'

    ## Data to post to the url
    answer = {'team_name': 'green bay'}

    x = requests.post(url, json=answer)

    print(x.text)


if __name__ == "__main__":
    main()
