#!/usr/bin/env python
 
import csv
import sys
import yaml
 
csv_data = []
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
	    ### Strip the comment lines
        if str(row).strip().startswith('#'):
            continue
        else:
			csv_data.append(row)
 
with open(sys.argv[1] + '.yml', 'w') as outfile:
    outfile.write(yaml.dump({'csv_data': csv_data}))