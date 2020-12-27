import json
import os
import time
import glob
import easygui

with open('move.config', 'r') as file:
    config = json.load(file)

while True:

    content = glob.glob(config['from']+'*.*')

    for file in content:
        name = file[file.rfind('/')+1:]
        print(name)
        ext = file[file.rfind('.')+1:]
        print(ext)
        if ext in config.keys():
            print(f'{ext} in config')
            if config[ext]:
                print(config[ext])
                os.rename(file, config[ext]+name)
                print(file)
                print(config[ext]+name)
        else:
            path = easygui.enterbox(f'unsigned extension {ext}\ntype a path for files with this extension\n(empty to ignore {ext}):')
            config[ext] = None if path == '' else path
            with open('move.config', 'w') as file:
                json.dump(config, file)

    time.sleep(config['sleep'])
