import time
import msvcrt

finish=10
count=0

print "press enter to start:"
raw_input()
s_time=time.time()

while 1:
	key=msvcrt.getch()
	if key=='\xe0' :
			count=count+1
			print "--> " ,
			if count==finish:
					break

time_elapsed=time.time() - s_time
print "game over. time taken: " + str(time_elapsed)	

'''
1. Understand the assignment again and redo. :<	
'''
