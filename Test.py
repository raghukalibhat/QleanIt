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
    if(os.path.exists(fileName) and os.path.isfile(fileName)):
        print "getAbsFilePath : File Path",os.path.abspath(fileName)
        return (os.path.abspath(fileName))
    else:
        return os.getcwd()

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

print "Current WD : ",rootWorkingDir

currEl = os.listdir(rootWorkingDir)
print currEl

for el in currEl:
    
    fullPath = getAbsFilePath(el)
    print 'fullPath:',fullPath
    
    #if its a file dont perform any computation, we will check the time stamp and the modified date to decide
    #whether to delete ot not 
    if(os.path.exists(el) and os.path.isfile(el)):
        print el,"exists and is a valid file"
        printFileExt(fullPath)

    #for a directory, change to the dir and find the elements inside 
    if(os.path.exists(el) and os.path.isdir(el)):
        print el,"exists and is a valid directory"
        os.chdir(el)
        print "Elements in the changed directory |", os.chdir(el),"| are : ",os.listdir(rootWorkingDir)
        os.chdir(rootWorkingDir)

    timeStamp = printFileMod(fullPath)
    print 'Last Modified:',timeStamp

    print
