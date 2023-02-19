import sys,os

def doesFileExist(path):
    if os.path.exists(path):
        print("File exists", path)
    else:
        print("File not found", path)
        raise FileNotFoundError


path = sys.argv[1]
doesFileExist(path)
data = None
with open(path) as fp:
    data = fp.read()
    
if data:
    for line in data.split('\n'):
        if line:
            #print("line:", line.split('-'))
            word, defn = line.split('-')
            print("\n{}\n".format(word))
            mult_def = defn.split(',')
            str_def = "\n\n".join([n.strip() for n in mult_def])
            print("{}".format(str_def))
            