from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file,'w').write(open(from_file).read())
#print(f"copying from {from_file}to {to_file}...")

#in_file = open(from_file)
#indata = in_file.read()

#print(f"the input file is {len(indata)} bytes long")

#print(f"does the output file exist? {exists(to_file)}")
#print(f"ready, hit RETURN to continue, CTRL-c to abort")
#input()

#out_file = open(to_file,'w')
#out_file.write(indata)

#print("alright, all done")

#out_file.close()
#in_file.close()
