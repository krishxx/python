import glob2
import glob, os

filenames = glob2.glob('*regout.txt')  # list of all .txt files in the directory

with open('activeRegOut.txt', 'w') as f:
    for file in filenames:
        with open(file) as infile:
            f.write(infile.read()+'\n')

"""
print "removing existing split files"
filelist = glob.glob("split_file*.txt")
filelist2 = glob.glob("*mxout.txt")
filelist3 = glob.glob("*regout.txt")
for f in filelist:
        os.remove(f)
for f in filelist2:
	os.remove(f)
for f in filelist3:
	os.remove(f)
"""
