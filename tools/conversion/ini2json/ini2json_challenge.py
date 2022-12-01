import ConfigParser
import json
import sys

if len(sys.argv) < 2:
	print 'Need file parameter'
	sys.exit(1)

config = ConfigParser.ConfigParser()
config.optionxform = str # stop making keys lowercase
config.read(sys.argv[1])

def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

data = {}
accum = []
for section in config.sections():
	entry = {}
	for opt in config.items(section):
		key = opt[0]
		value = opt[1]
		if value.startswith('"') and value.endswith('"'):
			value = value[1:-1]
		entry[key] = int(value) if is_number(value) else value
	assert section not in data, f'{section} conflicts'
	data[section] = entry
data = {}
