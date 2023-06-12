import subprocess
import platform
from sys import argv
import requests
import re
import threading



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

            syst = platform.system()
            if syst == 'Windows':

                for url in list_get: 
                    result = subprocess.run(['nslookup', '-qt=CNAME', '{}'.format(url)], capture_output=True, text=True)
                    output = result.stdout.strip()
                    line = output.split("\n")[-1]

                    if "canonical name = " in line:
                        try:
                            with open('result_cname.txt','a+') as f:
                                f.write(line+'\n')
                            f.close()
                        except Exception as e:
                            print(e)    
            elif syst == 'Linux':
                for url in list_get: 
                    result = subprocess.run(['nslookup', '{}'.format(url)], capture_output=True, text=True)
                    output = result.stdout.strip()
                    line = output.split("\n")[4]

                    if "canonical" in line:
                        try:
                            with open('result_cname.txt','a+') as f:
                                f.write(line+'\n')
                            f.close()
                        except Exception as e:
                            print(e)
            else:
                print('Unsupported type')        

    
    except:
        return False
      

def find_Vunl():

    try:
        with open('result_cname.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print('result_cname.txt not found')
        exit()



    urls_to_check = []
    for url_pattern in ['s3.amazonaws.com', 'animaapp.io','createsend.com','furyns.com','hatenablog.com','helpjuice.com','helpscoutdocs.com','youtrack.cloud','ngrok.io','readme.io','na-west1.surge.sh','surveysparrow.com','read.uberflip.com','wordpress.com']:
        if url_pattern in content:
            pattern = r'.*('+url_pattern+').*'
            result = re.search(pattern, content)
            if result:
                url_all = result.group(0)
                parts = url_all.split(" ")
                if len(parts) > 0:
                    url = 'https://' + parts[0]
                    urls_to_check.append(url)

    for url in urls_to_check:
        try:
            #print(url)
            res = requests.get(url, timeout=5)
            find_strings(res,url)
        except requests.exceptions.RequestException as e:
            print('Error:', e) 



    urls_to_check = []
    for url_pattern in ['cloudapp.net', 'cloudapp.azure.com','azurewebsites.net','blob.core.windows.net','azure-api.net','azurehdinsight.net','azureedge.net','azurecontainer.io','database.windows.net','azuredatalakestore.net','search.windows.net','azurecr.io','redis.cache.windows.net','azurehdinsight.net','servicebus.windows.net','visualstudio.com']:
        if url_pattern in content:
            pattern = r'.*('+url_pattern+').*'
            result = re.search(pattern, content)
            if result:
                url_all = result.group(0)
                parts = url_all.split(" ")
                if len(parts) > 0:
                    url = 'https://' + parts[0]
                    urls_to_check.append(url)

    for url in urls_to_check:
        try:
            res = requests.get(url, timeout=5)
            #print(res.status_code)
        except:
            printer(url)
            

    if 'helprace.com' in content:
            pattern = r".*(helprace\.com).*"
            result = re.search(pattern, content)
            if result:
                url_all = result.group(0)
                parts = url_all.split(" ")
                if len(parts) > 0:
                    url = parts[0]
                    
                    try:
                        url = 'https://' + url
                        #print(url)
                        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                        res = requests.get(url,timeout=5,headers=headers,allow_redirects=False)
                           
                        if res.status_code == 301:
                            printer(url)
                    except:
                        print("error\n")

    if 'launchrock.com' in content:
            pattern = r".*(launchrock\.com).*"
            result = re.search(pattern, content)
            if result:
                url_all = result.group(0)
                parts = url_all.split(" ")
                if len(parts) > 0:
                    url = parts[0]
                    
                    try:
                        url = 'https://' + url
                        #print(url)
                        res = requests.get(url,timeout=5)
                        if res.status_code == 500:
                            printer(url)
                    except:
                        print("error\n") 



def find_strings(res,url):
    if 'The specified bucket does not exist' in res.text:
        printer(url)
    elif 'The page you were looking for does not exist' in res.text:
        printer(url)
    elif 'Trying to access your account' in res.text:
        printer(url)
    elif 'This page could not be found' in res.text:
        printer(url)
    elif 'Blog is not found' in res.text:
        printer(url)
    elif "We could not find what you're looking for" in res.text:
        printer(url)
    elif "No settings were found for this company" in res.text:
        printer(url)
    elif "YouTrack Cloud" in res.text:
        printer(url)
    elif "ngrok.io not found" in res.text:
        printer(url)
    elif "The creators of this project are still working on making everything perfect" in res.text:
        printer(url)
    elif "project not found" in res.text:
        printer(url)
    elif "Account not found" in res.text:
        printer(url)
    elif "The URL you've accessed does not provide a hub" in res.text:
        printer(url)
    elif "Do you want to register" in res.text:
        printer(url)
    
def printer(url):
    print(url + ' ' + '\033[1;31;40mSubdomain Takeover vulnerability may exist\033[0m\n')

     
if __name__== '__main__':
    print ("\n*************** [ Cname is finding ] ***************\n")
    print('''
 ________________________________
 |  ____(_)         | |
 | |__   _ _ __   __| | ___ _ __
 |  __| | | '_ \ / _` |/ _ \ '__|
 | |    | | | | | (_| |  __/ |
 | |    |_|_| |_|\__,_|\___|_|
 ''')
    print("please waiting...\n")
    
    t1 = threading.Thread(target=getUrl)
    t1.start()
    t1.join()
    
    t2 = threading.Thread(target=find_Vunl)
    t2.start()
    t2.join()

    print("Done...")
    
    
