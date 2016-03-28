import os
import json
import urllib2
import hashlib


MainPath = os.path.dirname(os.path.abspath(__file__))
database = []

def init():
    global database
    with open(MainPath + "/DB.json") as data_file:
        database = json.load(data_file)


def main():
    for item in database:
        url = item["url"]
        response = urllib2.urlopen(url)
        html = response.read()
        hash = hashlib.md5(html).hexdigest()

        if item["hash"] != hash:
            # Notfiy the change
            print item["name"]

            # Dump new hash
            item["hash"] = hash
            with open(MainPath + "/DB.json", 'w') as outfile:
                json.dump(database, outfile)


if __name__ == '__main__':
    init()
    main()