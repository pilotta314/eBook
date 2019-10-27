#!/usr/bin/env python3

import yaml
import json
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

        # get image_name metadata
        session = requests.Session()
        api_url = "https://en.wikipedia.org/w/api.php"
        params_image = {
            "action": "query",
            "format": "json",
            "prop" : "imageinfo",
            "iiprop": "user|userid|canonicaltitle|url|extmetadata",
            "titles": "File:" + image_name
        }

        image_data = session.get(url=api_url, params=params_image).json()
        # print(json.dumps(image_data, indent=4, ensure_ascii=0))

        IPAGES = image_data["query"]["pages"]

        for k, v in IPAGES.items():
            print("LIZENZ : " + v["imageinfo"][0]["extmetadata"]["LicenseShortName"]["value"])
            image_info = v["imageinfo"][0]
            image_title = image_info["extmetadata"]["ObjectName"]["value"]
            image_author = image_info["user"]
            image_author_link = "https://commons.wikimedia.org/wiki/User:" + image_author
            image_page = image_info["descriptionurl"]
            license_name = image_info["extmetadata"]["UsageTerms"]["value"]
            license_short_name = image_info["extmetadata"]["LicenseShortName"]["value"]
            license_url = image_info["extmetadata"]["LicenseUrl"]["value"]
            tullu = ("\"" + image_title + "\" von [" + image_author + "](" + image_author_link + ") unter ["  + license_short_name + "](" + license_url + ") auf [Wikimedia Commons](" + image_page + ")")
            # print(tullu)
            text = re.sub("!\[" + description + "\]\(" + link + "\)", "![" + description + "](" + link + ")" + "  \n" + tullu, text)

course_license = ""
ATTRIBUTES = dict(
    by = 'Attribution',
    nc = 'Non-Commercial',
    nd = 'No Derivatives',
    sa = 'Share-Alike',
    )

with open("metadata.yml", 'r') as course_metadata:
    try:
        data = yaml.safe_load(course_metadata)
    except yaml.YAMLError as exc:
        print(exc)

    course_title = data["name"]
    course_url = data["url"]
    course_author = data["creator"]["givenName"] + " " + data["creator"]["familyName"]
    # course_author_url = 

    course_license_url = data["license"]
    course_license_components = re.findall("licenses\/([^\/]*)\/([^\/]*)", course_license_url)
    course_license_code = course_license_components[0][0]
    course_license_version = course_license_components[0][1]
    course_license_short_name = "CC " + course_license_code.upper() + " " + course_license_version

    course_license_text = "Dieses Werk und dessen Inhalte sind - sofern nicht anders angegeben - lizenziert unter " + course_license_short_name + ". Nennung gemäß [TULLU-Regel](https://open-educational-resources.de/oer-tullu-regel/) bitte wie folgt: " + "\"[" + course_title + "](" + course_url + ")\" von " + course_author + ", Lizenz: [" + course_license_short_name + "](" + course_license_url + ")"

course_tagged = open("course-tagged.md", "w")
course_tagged.write(text + "\n\n" + course_license_text)
course_tagged.close()
course.close()
