import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on "+ time.ctime())
while break_count < 3:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=KpAvweU0kac&list=PLrG6CrteQRQIELlUzhfJnYvhCDHIvrmcf&index=1")
    break_count = break_count + 1
    
