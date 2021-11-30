#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/mycode/nasa/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## ask for the start date
    startdate = input("Enter a start date in the following format: YYYY-MM-DD: ")

    ## ask for the end date
    enddate = input("Enter an end date in the following format(MAX IS 7 DAYS): YYYY-MM-DD: ")

    # make a request with the request library
    neowrequest = requests.get(NEOURL + "start_date=" + startdate + "&" + "end_date="+ enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
#    print(neodata)
   
    ## display the date the data was taken from
    print(f"Date range: {startdate} - {enddate}")

    ## print the number of near earth objects for the given day
    print(f"\nNumber of NEOs: {neodata['element_count']}")

    ## count and print the number of hazardous objects
    count = 0
    for date in neodata["near_earth_objects"].keys():
        for neo in neodata["near_earth_objects"][date]:
            if neo["is_potentially_hazardous_asteroid"]:
                count += 1 
    print(f"Potentially hazardous asteroids between {startdate} and {enddate}: {count}")

if __name__ == "__main__":
    main()
