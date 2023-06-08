import subprocess
from sys import argv
import re


def remove_protol(text):
    pattern = r'https?://'
    return re.sub(pattern, '',text)


def getUrl():
    try:
        filename = argv[1]
        
        with open(filename,'r') as f:
            
            content = remove_protol(f.read())
            list_get = list(content.split('\n'))
            #print(list_get)
            for url in list_get: 

                
                result = subprocess.run(['nslookup', '-qt=CNAME', '{}'.format(url)], capture_output=True, text=True)
                
                output = result.stdout.strip()
                line = output.split("\n")[-1]

                if "canonical name = " in line:
                    with open('result.txt','a+') as f:
                        f.write(line+'\n')
                    f.close()
                """ else: 
                    print("no CNAME!")  """
    except:
        return False
    
if __name__== '__main__':
    print ("\n*************** [ Cname is finding ] ***************\n")
    print('''
 |  ____(_)         | |
 | |__   _ _ __   __| | ___ _ __
 |  __| | | '_ \ / _` |/ _ \ '__|
 | |    | | | | | (_| |  __/ |
 | |    |_|_| |_|\__,_|\___|_|
 ''')
    print("please waiting...")
    getUrl()
    print("check result.txt")
    
