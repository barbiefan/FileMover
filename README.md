# FileMover
move files from one directory to anywhere according to file extensions associations

# Requirements 
python 3.*  
tkinter (python lib)  
easygui (python lib)  

# Setup
Edit move.config for your needs.  
You will be asked on every file with new extension which directory to put it to, move.config will memorize that decision.  
Directory paths should be absolute and look like: "/home/username/Pictures/"  

Params:  
"from": directory to watch  
"sleep": delay between scans in seconds  
