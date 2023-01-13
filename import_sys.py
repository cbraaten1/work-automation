import sys
import platform

print("Python EXE     : " + sys.executable)
print("Architecture   : " + platform.architecture()[0])

# This information was found on Stack Overflow: https://stackoverflow.com/questions/44727232/scheduling-a-py-file-on-task-scheduler-in-windows-10
# I have removed 'import imp' becuase of the deprecation warning & 'raw_input("\n\nPress ENTER to quit")' the library wasn't downloaded.