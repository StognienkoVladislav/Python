import json
import pprint


mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(str(mapping))

print(json.dumps(mapping, indent=4, sort_keys=True))

mapping['d'] = {1, 2, 3}
pprint.pprint(mapping)

