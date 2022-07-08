import xml.etree.ElementTree as gfg
import os
from datetime import datetime
#Write XML file
num_of_targets = 250         #number of testFiles
counter = 1

def GenerateXML(fileName) :
  
  root = gfg.Element("Profile")
  
  m1 = gfg.Element("TimeSpans")
  root.append (m1)
  
  m2 = gfg.Element("TimeSpan")
  m1.append (m2)

  m3 = gfg.Element("Targets")
  m2.append (m3)

  m4 = gfg.Element("Target")
  m3.append (m4)

  global counter
  while counter != num_of_targets+1: 
        b1 = gfg.SubElement(m4, "Path")                 #WRITE <Target>
        b1.text = f"d:\\testFile{counter}.dat"
        counter += 1
        b2 = gfg.SubElement(m4, "FileSize")
        b2.text = "134217728"
        # b3 = gfg.SubElement(m4, "RequestCount")
        # b3.text = "1"
        b4 = gfg.SubElement(m4, "ThinkTime")
        b4.text = "1"
        b11 = gfg.SubElement(m4, "SequentialScan")
        b11.text = "false"
        b5 = gfg.SubElement(m4, "BlockSize")
        b5.text = "262144"
        b6 = gfg.SubElement(m4, "BurstSize")
        b6.text = "5"
        b7 = gfg.SubElement(m4, "DisableOSCache")
        b7.text = "true"
        b8 = gfg.SubElement(m4, "WriteRatio")
        b8.text = "100"
        m5 = gfg.Element("WriteBufferContent")
        m4.append (m5)
        b9 = gfg.SubElement(m5, "Pattern")
        b9.text = "random"
        b10 = gfg.SubElement(m4, "Throughput")
        b10.text = "1200"
        if counter != num_of_targets+1:
            m4 = gfg.Element("Target")
            m3.append (m4)
        else:
            continue                                    #</Target>

  b1 = gfg.SubElement(m2, "Duration")
  b1.text = "600"
  b2 = gfg.SubElement(m2, "Warmup")
  b2.text = "10"
  b2 = gfg.SubElement(m2, "ThreadCount")
  b2.text = "1"
  b2 = gfg.SubElement(m2, "MeasureLatency")
  b2.text = "true"
  b2 = gfg.SubElement(m2, "CalculateIopsStdDev")
  b2.text = "true" 

  b1 = gfg.SubElement(root, "ResultFormat")
  b1.text = "xml" 

  tree = gfg.ElementTree(root)
  
  with open (fileName, "wb") as files :
    tree.write(files)

  name_dir = "backup_XML"
  current_dir = os.getcwd()
  path = os.path.join(current_dir, name_dir)
  now = datetime.now() # current date and time
  date_time = now.strftime("%m_%d_%Y_%H%M%S")
  completeName = os.path.join(path, date_time + fileName)
  isdir = os.path.isdir(path)
  if isdir != True:
    os.mkdir(name_dir) 
    with open (completeName, "wb") as files :
      tree.write(files)
  elif isdir == True:  
    with open (completeName, "wb") as files :
      tree.write(files)

# Driver Code
if __name__ == "__main__":
  GenerateXML(f"AccWriteProfile_H264_{num_of_targets}C_v2.xml")
