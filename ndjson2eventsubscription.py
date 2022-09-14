#!/usr/bin/env python3

import json
import pprint

"""
    <QueryList>
    <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
      <Select Path="Microsoft-Windows-Sysmon/Operational">
      *[System[EventID='1']] and
      *[EventData[Data[@Name='ParentImage'] != '']] and
      *[EventData[Data[@Name='Image'] != '']]
      </Select>
    </Query>
    </QueryList>
"""

with open("export.ndjson") as ndjson:
    json_objects = []
    for ndjson_object in ndjson:
        json_objects.append(json.loads(ndjson_object))
    
    kibana_filters = json_objects[1]["attributes"]["filters"]
    for kibana_filter in kibana_filters:
        field_name = kibana_filter["meta"]["key"]
        if field_name == "process.parent.executable.keyword":
            foo = "*[EventData[Data[@Name='ParentImage'] != '%s']] and" % (field_name)
            print(foo)
        else:
            pprint.pprint(field_name)
        
        values = kibana_filter["meta"]["params"]
        pprint.pprint(values)
        print("\n")