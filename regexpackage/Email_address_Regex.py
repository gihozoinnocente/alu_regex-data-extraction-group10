#!/usr/bin/python3
import json
import re

def EmailAddressRegex(data):
    matches = re.findall(r'\b\S+(?:[A-Za-z]+)?(?:\d+)?(?:[A-Za-z]+)?(?:\d+)?(?:\+|-|_|\.)?(?:[A-Za-z]+)?(?:\d+)?(?:[A-Za-z]+)?(?:\d+)?@(?:[a-z]+)\.\w+\S?\w+\b', data);
    print(matches)
    with open("Email-address.json", "a", encoding="utf-8") as ep:
        json.dump(matches, ep)
        print("Succesfully saved Email addresses in json format")

if __name__ == "__main__":
    import re
    import json
    import sys
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as fp:
            data = fp.read()
        matches = re.findall(r'\b\S+(?:[A-Za-z]+)?(?:\d+)?(?:[A-Za-z]+)?(?:\d+)?(?:\+|-|_|\.)?(?:[A-Za-z]+)?(?:\d+)?(?:[A-Za-z]+)?(?:\d+)?@(?:[a-z]+)\.\w+\S?\w+\b', data);
        print(matches)
        with open("Email-address.json", "a", encoding="utf-8") as ep:
            json.dump(matches, ep)
            print("Succesfully saved Email addresses in json format")
    except FileNotFoundError as err:
        print(err)
    except IndexError as err:
        print(err)
        print("Make sure you put the full file path as the command line argument after your shell script")
