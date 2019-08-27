#!/usr/bin/env python3

import yaml
import json
import sys

with open("metadata.yml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

    data['@context'] = 'http://schema.org/'
    data['publisher']['@type'] = 'Person'
    data['creator']['@type'] = 'Person'

    with open("metadata.json", 'w', encoding='utf8') as outputfile:
        jsonstring = json.dumps(data, indent=4, ensure_ascii=0)
        tagstring = '<link rel="license" href="' + data['license'] + '"/>'
        tagstring = tagstring + '<script type="application/ld+json">' + jsonstring + '</script>'
        outputfile.write(tagstring)

    with open('title.txt', 'w', encoding='utf8') as titlefile:
        titlecontent = '---\n'
        titlecontent = titlecontent + 'title: ' + data['name'] + '\n'
        titlecontent = titlecontent + 'author: ' + data['creator']['givenName'] + ' ' + data['creator']['familyName'] + '\n'
        titlecontent = titlecontent + 'rights: ' + data['license'] + '\n'
        titlecontent = titlecontent + 'language: ' + data['inLanguage'] + '\n'
        titlecontent = titlecontent + '...\n'
        titlefile.write(titlecontent)
