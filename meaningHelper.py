#-*-coding:utf8;-*-
from os.path import join, dirname
#import urllib, urllib.parse, urllib.request

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
    
    pastebin_vars = {'api_dev_key':'ztwMYWnoU4It7SHiEZlMLMWodHVRWMx2',
    'api_option':'paste', # a new paste
    'api_paste_private':'1', #unlisted
    'api_paste_expire_date':'1W', #1 week
    
    'api_paste_code':fullInfo, 
    'api_paste_name':fname}
    
    #url_vars = urllib.parse.urlencode(pastebin_vars)
    #print("http://pastebin.com/api/api_post.php?"+url_vars) 
    #url_vars = url_vars.encode('utf-8')
    
    result = 'pasteBin share is TBA'
    
    try:
        # https://stackoverflow.com/a/36485152
        #TODO pastebin stopped working for me.
        pass
        #see meaningHelper_toPy3 for working on PC
        #req = urllib.request.Request('http://pastebin.com/api/api_post.php', data=url_vars) 
         
        #resp = urllib.request.urlopen(req) 
        #result = resp.read() 
    except IOError as err :
        result = str(err)
          
    return result  
    
#eof share




if __name__ == "__main__" :
    #archiveReading("event", "01011987", "Test", "I know if you are going on pause.") 
    res = pastebinShare("event", "01011987", "Амелия", "I know if you are going on pause.") 
    print (res) 
    print ("Done") 
