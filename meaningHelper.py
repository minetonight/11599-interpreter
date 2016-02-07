#-*-coding:utf8;-*-
from os.path import join, dirname
import urllib

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
    
    pastebin_vars = {'api_dev_key':'8fa8dc71c640f0159758990f8e3ab5e6',
    'api_option':'paste', # a new paste
    'api_paste_private':'1', #unlisted
    'api_paste_expire_date':'1W', #1 week
    
    'api_paste_code':fullInfo, 
    'api_paste_name':fname,}
    result = ' '
    
    try:
        response = urllib.urlopen('http://pastebin.com/api/api_post.php', urllib.urlencode(pastebin_vars))
        result = response.read()
    except IOError :
        result = "IOError"
          
    return result  
    
#eof share




if __name__ == "__main__" :
    archiveReading("event", "01011987", "Test", "I know if you are going on pause.") 
    res = pastebinShare("event", "01011987", "Амелия", "I know if you are going on pause.") 
    print res
    print ("Done") 
    
    
    
    
    
    
    
