# ReadXML.py WriteXML.py
To run: python <ReadXML.py>

        Output:
        the new XML files will be in the same folder as ReadXML.py and WriteXML.py
        a backup_XML folder will be created 
        a backup XML file will be added in there for record keeping
About: create XML files with respect to number of testFiles.

# get_diskspd_results.py
To run: python get_diskspd_results.py <your diskspd results folder path>

    Takes a text_file_path,
    Reads file and then parse through it line by line into groups,
    Output to file:
    Total IO: #MiB/s, AvgLat: #ms
    Read IO: #MiB/s, AvgLat: #ms
    Write IO: #MiB/s, AvgLat: #ms

About: this it to parse diskspd results and spit out the above info.
