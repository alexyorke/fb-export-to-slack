import json
import csv
import sys
import re
from functools import partial

channel = input(
    "Enter name of Slack channel to import to (without # prefix): ")

# https://stackoverflow.com/a/50011987
fix_mojibake_escapes = partial(
     re.compile(rb'\\u00([\da-f]{2})').sub,
     lambda m: bytes.fromhex(m.group(1).decode()))

fbMessages = []
with open(sys.argv[1], 'rb') as binary_data:
    json_file = fix_mojibake_escapes(binary_data.read())
    data = json.loads(json_file.decode('utf8'))
    for message in data['messages']:
        if (message['type'] == "Generic") and ('sticker' not in message):
		    # messages are in milliseconds; have to divide by 1000 to get epoch
            fbMessages.append([int(message['timestamp_ms'])/1000.00, channel, str(message['sender_name']),
                               str(message['content'])])

# sort them by timestamp (youngest first)
fbMessages = sorted(fbMessages, key=lambda x: x[0])

# https://stackabuse.com/reading-and-writing-csv-files-in-python/
csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)

# write to file
myFile = open(sys.argv[2], 'w', newline='\n', encoding='utf-8')
with myFile:
    writer = csv.writer(myFile, dialect='myDialect')
    writer.writerows(fbMessages)
