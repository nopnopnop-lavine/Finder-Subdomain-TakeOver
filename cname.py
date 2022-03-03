import requests
from sys import argv
import time




def checkUrlCname():
    try:
        filename = argv[1]
        with open(filename,'r') as f:

            content = f.read()
            if 'http' in content:
                print('\033[1;31;40m Only need domain not protocol \033[0m')
                return false

            listread = list(content.split('\n'))

        for url in listread:
            req = requests.get('https://resolve-cname.josephharrisonlim.now.sh/api?hostname={}'.format(url))
            if not 'error' in req.text:
                print(url +' '+'cname name is finding'+ ' '+ req.text)
                with open('result.txt','a+') as f:
                    f.write(url + ' ' + 'has Cname name'+' '+' '+req.text+'\n')
                f.close()
                continue
    except:
        print('error')


if __name__ == '__main__':
    print ("\n*************** [ Cname is finding ] ***************\n")
    print('''
 |  ____(_)         | |
 | |__   _ _ __   __| | ___ _ __
 |  __| | | '_ \ / _` |/ _ \ '__|
 | |    | | | | | (_| |  __/ |
 | |    |_|_| |_|\__,_|\___|_|
 ''')
    print("please waiting...")
    checkUrlCname()
    print("check result.txt")

