#-*-coding:utf8;-*-
from os.path import join, dirname
import requests

def archiveReading(g_type, birthday, name, fullInfo):
    curdir = dirname(__file__)
    fname = "%s_%s_%s.txt" % (g_type[0], name, birthday) 
    filename = join(curdir, 'archives', fname)
    
    f = open(filename, "w") 
    f.write(fullInfo) 
    f.close()
    
#eof archive

def pastebinShare(g_type, birthday, name, fullInfo):
    fname = "%s_%s_%s.txt" % (g_type[0], name, birthday) 
    
    #from https://stackoverflow.com/questions/63077603/pastebin-api-invalid-api-dev-key
    API_ENDPOINT = "https://pastebin.com/api/api_post.php"
    data = {'api_dev_key':'ztwMYWnoU4It7SHiEZlMLMWodHVRWMx2',
        'api_option':'paste', # a new paste
        'api_paste_code':fullInfo, 
        'api_paste_private':'1', #unlisted
        'api_paste_expire_date':'1W', #1 week
        'api_paste_name':fname
    }
    
    result = ' '
    
    try:
        resp = requests.post(url = API_ENDPOINT, data = data)
        result = resp.text 
    except IOError as err :
        result = str(err)
          
    return result  
    
#eof share




if __name__ == "__main__" :
    archiveReading("event", "01011987", "Test", "I know if you are going on pause.") 
    resp = pastebinShare("event", "01011987", "Амелия", "I know if you are going on pause.") 
    
    print(resp) 
    print("Done") 

