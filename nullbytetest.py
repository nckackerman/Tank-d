if '\0' in open('poop.py').read():
    print "you have null bytes in your input file"
else:
    print "you don't"