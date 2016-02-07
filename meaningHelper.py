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
    
    
    
    
    
