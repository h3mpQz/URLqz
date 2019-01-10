import os, requests

os.system('clear')
print ('URLqz by h3mpQz v 1.0')
print ('Contact us: h3mpqz.prod@gmail.com')

url = raw_input('URL: ')
token = ('8ceaac0e8ceaac0e8ceaac0e598c8cc64b88cea8ceaac0ed0dcd73d663ee1b4baf9b740')

def func1():
    
    try:
        method = ('utils.checkLink')
        apiurl = ('https://api.vk.com/method/'+method+'?url='+url+'&access_token='+token+'&v=V')
        r = requests.get(apiurl).json()
        response = r.get('response')
        status = response.get('status')
    
        if status == ('not_banned'):
        
            print('\n' + 'THIS LINK IS NOT BANNED')
        
        elif status == ('banned'):
    
            print('\n' + 'THIS LINK IS BANNED' + '\n')
        
            quit()
            
    except AttributeError:
        
        print ('\n' + 'Error: Incorrect URL!' + '\n')
        quit()
        
func1()

def func2():
    
    method = ('utils.getShortLink')
    private = ('0')
    apiurl = ('https://api.vk.com/method/'+method+'?url='+url+'&private='+private+'&access_token='+token+'&v=V')
    r = requests.get(apiurl).json()
    response = r.get('response')
    short_url = response.get('short_url')
    print('YOU SHORT LINK: ' + short_url + '\n')
    quit()
func2()



