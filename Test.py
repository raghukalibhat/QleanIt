import os, time

#Read the contents of a file specified by full file path
def ReadFile(filePath):
    # Using readline()
    file1 = open(fullPath, 'r')
    count = 0
  
    while True:
        count += 1
  
        # Get next line from file
        line = file1.readline()
  
        # if line is empty
        # end of file is reached
        if not line:
            break
        #print("Line{}: {}".format(count, line.strip()))
  
    file1.close()

def getAbsFilePath(fileName):
    #return (os.path.dirname(__file__)+str('\\')+str(fileName))
    return (os.path.abspath(fileName))

##################################################################
#           printFileMod(path)
#   This api checks the modified time of a file in ISO format 
##################################################################
def printFileMod(path):
    ti_m = os.path.getmtime(path)
 
    m_ti = time.ctime(ti_m)
 
    # Using the timestamp string to create a
    # time object/structure
    t_obj = time.strptime(m_ti)

    print "ti_m",ti_m
    print "m_ti",m_ti
    print "Year=",t_obj[0]
    print "Month=",t_obj[1]
    print "Day=",t_obj[2]
    print "Hour=",t_obj[3]
    print "Minute=",t_obj[4]
    print "Second=",t_obj[5]  
    # Transforming the time object to a timestamp
    # of ISO 8601 format
    T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    return T_stamp

##################################################################
#           printFileExt(path)
# This api checks the type of file extension
##################################################################
def printFileExt(path):
    # this will return a tuple of root and extension
    split_tup = os.path.splitext(path)
    #print(split_tup)    
  
    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]
  
    print "File Name:", file_name 
    print "File Extension:", file_extension 
    
##################################################################
#           main()
##################################################################

rootWorkingDir = os.getcwd()
print rootWorkingDir

currEl = os.listdir(os.getcwd())

for el in currEl:
    fullPath = getAbsFilePath(el)
    print 'fullPath:',fullPath
    if(os.path.exists(el) and os.path.isfile(el)):
        print el,"exists and is a valid file"
        printFileExt(fullPath)
    if(os.path.exists(el) and os.path.isdir(el)):
        print el,"exists and is a valid directory"


    timeStamp = printFileMod(fullPath)
    print 'Last Modified:',timeStamp

    print
