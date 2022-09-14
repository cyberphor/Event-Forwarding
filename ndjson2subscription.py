#!/usr/bin/env python3

import json
import pprint

parsed = []

with open("export.ndjson") as data:
    for line in data:
        parsed.append(json.loads(line))

for item in parsed[1]["attributes"]["filters"]:
    field_name = item["meta"]["key"]
    values = item["meta"]["params"]
    pprint.pprint(field_name)
    pprint.pprint(values)
    print("\n")
