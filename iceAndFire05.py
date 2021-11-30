#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"
AOIF_HOUSES = "https://www.anapioficeandfire.com/api/houses"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        ## Sent the HTTPS GET to the API of Ice and fire resource to get allegiances.
        print(f"\n\n{got_dj['name']} is aligned with the following Houses:")
        if got_dj['allegiances']:
            for allegiance in got_dj['allegiances']:
                ## Check for each allegiance returned for this character
                got_allegianceToLookup = requests.get(allegiance)
                ## Decode the response
                got_allegiance = got_allegianceToLookup.json()
                ## Print the house name
            print("  " + got_allegiance['name'])
        else:
            print("  None")

        ## Send the HTTPS GET to the API of Ice and Fire Books resource, then check if the char appears as a secondary character.
        if got_dj['books']:
            print(f"\n\n{got_dj['name']} appears in the following books:")
            for book in got_dj['books']:
                ## Check for each book returned for this character
                got_bookToLookup = requests.get(book)
                ## Decode the response
                got_book = got_bookToLookup.json()
                ## Print the book name
                print("  " + got_book['name'])

        ## Send the HTTPS GET to the API of Ice and Fire Books resource, then check if the char appears as a POV character.
        print(f"\n\n{got_dj['name']} is a POV character in the following books:")
        if got_dj['povBooks']:
            for book in got_dj['povBooks']:
                ## Check for each book returned for this character
                got_bookToLookup = requests.get(book)
                ## Decode the response
                got_book = got_bookToLookup.json()
                ## Print the book name
                print("  " + got_book['name'])
        else:
            print("  None")       


if __name__ == "__main__":
        main()
