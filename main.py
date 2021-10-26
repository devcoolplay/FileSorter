import shutil
import os
import sys
from tqdm import tqdm
from datetime import date

if len(sys.argv) == 2:
    sourceFolder = str(sys.argv[1]) + "/"
else:
    print("Please specify a path. (Use /)")
    exit(1)

filesInFolder = os.listdir(sourceFolder)

for i in tqdm(filesInFolder):
    if os.path.isfile(sourceFolder + i):
        dateCreated = os.stat(sourceFolder + i).st_ctime
        targetPath = sourceFolder + str(date.fromtimestamp(dateCreated)) + "\\"
        targetFilePath = targetPath + i
        if not os.path.exists(targetPath):
            os.mkdir(targetPath)
        shutil.move(sourceFolder + i, targetFilePath)

print("categorization complete!")
