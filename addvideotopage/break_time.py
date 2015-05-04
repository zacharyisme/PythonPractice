import webbrowser
import time

times = 0
print "Program start at " + time.ctime()
while times < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=OVUPLFLdmpE")
    print "this is "+ str(times+1) +" "+ time.ctime() 
    times += 1

print 'End the program'
