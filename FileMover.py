import json
import os
import time
import glob

with open('move.config', 'r') as file:
    config = json.load(file)
while True:
    for key, value in list(config.items())[2:]:
        files = glob.glob(config['from']+key)
        for file in files:
            os.rename(file, value+'/'+file[file.rfind('/')+1:])
    time.sleep(config['sleep'])
