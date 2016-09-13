from time import sleep, ctime
from webbrowser import open

print ("The program started on %s" % ctime())
for break_number in range(1,4):
    sleep(10)
    print("Its time for break number %s" % break_number)
    open("https://www.youtube.com/watch?v=DQfiWFwVF8M")
