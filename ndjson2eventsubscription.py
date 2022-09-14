#!/usr/bin/env python3

import json
import pprint

with open("export.ndjson") as ndjson:
    json_objects = []
    for ndjson_object in ndjson:
        json_objects.append(json.loads(ndjson_object))
    
    kibana_filters = json_objects[1]["attributes"]["filters"]
    for kibana_filter in kibana_filters:
        field_name = kibana_filter["meta"]["key"]
        values = kibana_filter["meta"]["params"]
        pprint.pprint(field_name)
        pprint.pprint(values)
        print("\n")
