import argparse

parser = argparse.ArgumentParser()
parser.add_argument('csv',type=str,help='The name of the file we are importing into Google')
args = parser.parse_args()

mypath = args.csv
myfile = open(mypath)
mytext = myfile.read()
myfile.close()
thelines = mytext.split("\n")

for line in thelines:
    thisline = line.split(',')
    counter = 0
    while counter < len(thisline):
        if (thisline[counter] == '' or thisline[counter] == ','):
            thisline.pop(counter)
        else:
            counter += 1
    print thisline
