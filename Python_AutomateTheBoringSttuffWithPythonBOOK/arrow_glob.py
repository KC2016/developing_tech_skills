from pathlib import Path
import arrow
import os
from datetime import date
from datetime import time

parentsPath = "Tutorials/items_delete"
filename = "text1.txt"
filePath = os.path.join(parentsPath, filename)


import time
import os.path
ftime = os.path.getmtime(filePath)
curtime = time.time()
difftime = curtime - ftime
if difftime > 400:   #86400:
    os.remove(filePath)
