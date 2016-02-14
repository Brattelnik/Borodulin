from sys import argv

#No comments, the code is obvious

if len(argv) < 2:
    print('usage: python ex3.py [file names]')
    exit()
    
output = []
    
for path in argv[1:]:
    try:
        file = open(path, "r")
        output.append(file.read())
        file.close()
    except:
        print("Error: could not open file " + path)
        exit()
        
print("\n".join(output))
