import time
import os, sys
# Open a file
suffix = ".jpg"
path = "authentication"
names = []
paths = []
for root, directories, files in os.walk(path):
    for filename in directories:
        # Join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        names.append(filename)
        paths.append(filepath)
#print(names)
#print(paths)

for i in range(len(names)):
	print names[i]
	for rt, drts, fls  in os.walk(paths[i]):
		for flname in fls:
			flpath = os.path.join(rt, flname)
			if flpath.endswith(suffix):
				print flpath