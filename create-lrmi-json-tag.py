#!/usr/bin/env python3

import yaml
import json
import sys

with open("metadata.yml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

    data['publisher']['@type'] = 'Person'
    data['creator']['@type'] = 'Person'
    #json.dump(data, sys.stdout, indent=4, ensure_ascii=0)
    with open("metadata.json", 'w', encoding='utf8') as outputfile:
        jsonstring = json.dumps(data, indent=4, ensure_ascii=0)
        tagstring = '<script type="application/ld+json">' + jsonstring + '</script>'
        outputfile.write(tagstring)
