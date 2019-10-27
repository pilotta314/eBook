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
    description = treffer[0]
    link = treffer[1]
    if "wikimedia" in link:
        print("TREFFER : " + description + " " + link)
        image_name = re.findall("\/([^\/]*)$", link)[0]
        # print(image_name)

        # get image_name metadata
        session = requests.Session()
        api_url = "https://en.wikipedia.org/w/api.php"
        title = "File:" + image_name
        params_image = {
            "action": "query",
            "format": "json",
            "prop": "imageinfo",
            "titles": "File:" + image_name
        }
        params_rights = {
            "action": "query",
            "format": "json",
            "meta" : "siteinfo",
            "siprop" : "rightsinfo",
            "titles": "File:" + image_name
        }

        image_data = session.get(url=api_url, params=params_image).json()
        rights_data = session.get(url=api_url, params=params_rights).json()
        # print(image_data)
        # print(rights_data)

        IPAGES = image_data["query"]["pages"]
        rights = rights_data["query"]["rightsinfo"]
        # print(IPAGES)
        # print(rights)

        for k, v in IPAGES.items():
            print("ERGEBNIS : " + v["title"] + " is uploaded by User:" + v["imageinfo"][0]["user"] + " under "  + rights["text"])


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
