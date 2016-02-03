#-*-coding:utf8;-*-
from os.path import join, dirname

def getMeaning(card, sectionName):
    # get any files into images directory
    curdir = dirname(__file__)
    filename = join(curdir, 'meanings', sectionName+".py")
    try:
        f = open(filename, "r") 
    except IOError:
        f = open(filename, "w+r") 
        text = (
'''#-*-coding:utf8;-*-

buf = " още няма данни, попълни %s" ''') % (sectionName, ) 
        f.write(text) 
        f.flush()
        f.seek(0)
        
    contents = f.read() 
    #print(contents)
    f.close()
    
    #http://lucumr.pocoo.org/2011/2/1/exec-in-python/
    exec(contents) 
    # buf is defined in the file 
    return buf 
        
#eof getMeaning(filename)


def archiveReading():
    pass

if __name__ == "__main__":
    card = [0, 
    	2, 2, 1,
    	1, 1, 1,
    	1, 1, 2]
    	
    
    print (getMeaning(card, "test")) 
    print ("Done") 
    
    
    
    
    