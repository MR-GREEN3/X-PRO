import os, sys
time.sleep(4)
print("\x1b[38;5;46m  CONGRATULATION YOUR DEVICE SUPPORT MY TOOLS") 
time.sleep(4)
print("\x1b[38;5;46m WELCOME TO MY TOOLS MR.GREEN ✓")
try:
    __import__("green").v1()
except Exception as e:
    exit(str(e))