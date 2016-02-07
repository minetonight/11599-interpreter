#-*-coding:utf8;-*-
from os.path import join, dirname

def archiveReading( g_type, birthday, name, fullInfo ):
    curdir = dirname(__file__)
    fname = "%s_%s_%s.txt" % (g_type[0], name, birthday) 
    filename = join(curdir, 'archives', fname)
    
    f = open(filename, "w") 
    f.write(fullInfo) 
    f.close()
    
#eof archive


if __name__ == "__main__" :
    archiveReading("event", "01011987", "Test", "I know if you are going on pause.") 
    print ("Done") 
    
    import urllib

    pastebin_vars = {'api_dev_key':'8fa8dc71c640f0159758990f8e3ab5e6',
    'api_option':'paste', # a new paste
    'api_paste_private':'1', #unlisted
    'api_paste_expire_date':'1W', #1 week
    
    'api_paste_code':'testing pastebin right now', 
    'api_paste_name':'namePaste',}
    response = urllib.urlopen('http://pastebin.com/api/api_post.php', urllib.urlencode(pastebin_vars))
    url = response.read()
    
    print url
    
    
    
    
    
