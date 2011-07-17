import re
import sys
from subprocess import Popen, PIPE, STDOUT

def set_volume(target_volume):
    if type(target_volume) is not int:
        print "Invalid type"
        return False
    elif target_volume not in range(101): 
        print "Invalid range"
        return False
    else:
        Popen(["/usr/bin/amixer", "-c", "0", "sset", "Master,0", "%s%%" % target_volume, ">", "/dev/null"])
        return True

def get_volume():
    res = Popen(["/usr/bin/amixer", "-c", "0", "sget", "Master,0"], stdout=PIPE)
    return re.findall(r'\d{1,3}', res.stdout.read())[4]
        
if __name__ == '__main__':
    try:
        if sys.argv[1] == "-g":
            response = get_volume()
        else:
            num = int(sys.argv[2])
            response = set_volume(num)
    except (ValueError, KeyError): # Conversion of argv out of range
        response = False
    if response is not False:
        print "Command completed successfully"
    else:
        print "Command failed"
