#!/usr/bin/env python3

#import yaml
#import json
import requests
import re
import sys

# find wikimedia images
course = open("course.md", "rt")
text = course.read()
images = re.findall("!\[([^\]]*)\]\(([^\)]*)\)", text)
for treffer in images:
    if "wikimedia" in treffer[1]:
        description = treffer[0]
        link = treffer[1]
        print("TREFFER : " + description + " " + link)
        image = re.findall("\/([^\/]*)$", link)[0]
        # print(image)

        # get image metadata
        S = requests.Session()
        URL = "https://en.wikipedia.org/w/api.php"
        title = "File:" + image
        PARAMS_IMAGE = {
            "action": "query",
            "format": "json",
            "prop": "imageinfo",
            "titles": "File:" + image
        }
        PARAMS_RIGHTS = {
            "action": "query",
            "format": "json",
            "meta" : "siteinfo",
            "siprop" : "rightsinfo",
            "titles": "File:" + image
        }

        I = S.get(url=URL, params=PARAMS_IMAGE)
        R = S.get(url=URL, params=PARAMS_RIGHTS)
        IDATA = I.json()
        RDATA = R.json()
        # print(IDATA)
        # print(RDATA)

        IPAGES = IDATA["query"]["pages"]
        RPAGES = RDATA["query"]["rightsinfo"]
        # print(RPAGES)

        for k, v in IPAGES.items():
            print("ERGEBNIS : " + v["title"] + " is uploaded by User:" + v["imageinfo"][0]["user"] + " under "  + RPAGES["text"])


course.close()




# with open("course.md", 'r') as stream:
    # try:
    #     data = yaml.safe_load(stream)
    # except yaml.YAMLError as exc:
    #     print(exc)

    # data['@context'] = 'http://schema.org/'
    # data['publisher']['@type'] = 'Person'
    # data['creator']['@type'] = 'Person'

    # with open("metadata.json", 'w', encoding='utf8') as outputfile:
    #     jsonstring = json.dumps(data, indent=4, ensure_ascii=0)
    #     tagstring = '<link rel="license" href="' + data['license'] + '"/>'
    #     tagstring = tagstring + '<script type="application/ld+json">' + jsonstring + '</script>'
    #     outputfile.write(tagstring)

    # with open('title.txt', 'w', encoding='utf8') as titlefile:
    #     titlecontent = '---\n'
    #     titlecontent = titlecontent + 'title: ' + data['name'] + '\n'
    #     titlecontent = titlecontent + 'author: ' + data['creator']['givenName'] + ' ' + data['creator']['familyName'] + '\n'
    #     titlecontent = titlecontent + 'rights: ' + data['license'] + '\n'
    #     titlecontent = titlecontent + 'language: ' + data['inLanguage'] + '\n'
    #     titlecontent = titlecontent + '...\n'
    #     titlefile.write(titlecontent)
