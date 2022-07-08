import sys
import re
import os
from pathlib import Path
from datetime import datetime

# HOW TO USE:
# IN CMD > python get_diskspd_results.py <your diskspd results folder path>

now = datetime.now() # current date and time
date_time = now.strftime("%m_%d_%Y_%H%M%S")
new_file = date_time + "_diskspd_results.txt"

def main():
    path = Path(sys.argv[1])
    global_path = path.glob('*')
    for file_path in global_path:
        #print(file_path)
        is_file = os.path.isfile(file_path)
        if is_file == True:
            collect_info(file_path)
        #print(is_file)
        elif is_file != True:
            #print(file_path)
            file_path1 = file_path.glob('*')
            #print(file_path1)
            for text_file_path in file_path1:
                #print(text_file_path)
                collect_info(text_file_path)

def collect_info(text_file_path):
    """
    Takes a text_file_path,
    Reads file and then parse through it line by line into groups,
    Output to file:
    Total IO: #MiB/s, AvgLat: #ms
    Read IO: #MiB/s, AvgLat: #ms
    Write IO: #MiB/s, AvgLat: #ms
    """
    counter = 0
    with open(text_file_path, encoding='utf16') as f: # The txt files are in UCS-2 LE BOM format so without 'utf16' encoding regex won't work
                lines = f.readlines()
    with open(new_file, 'a') as a_writer: # The output txt file is in UTF-8
        for line in lines:
            result = re.search(r'(total:)\s+(\S+)\s\|\s+(\S+)\s\|\s+(\S+)\s\|\s+(\S+)\s\|\s+(\S+)\s\|\s+(\S+)', line)                   
            if result != None:
                counter += 1
                if counter == 1:
                    a_writer.write(f'File Path: {text_file_path}\nTotal IO: {result.group(4)}MiB/s, AvgLat: {result.group(6)}ms\n')
                elif counter == 2:
                    a_writer.write(f'Read IO: {result.group(4)}MiB/s, AvgLat: {result.group(6)}ms\n')
                elif counter == 3:
                    a_writer.write(f'Write IO: {result.group(4)}MiB/s, AvgLat: {result.group(6)}ms\n\n')
                    counter = 0

if __name__ == "__main__":
    main()        


                    

        