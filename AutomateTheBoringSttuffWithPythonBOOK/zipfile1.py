#import datetime
#import pathlib
#import zipfile

#FILE_PATTERN = "*.csv"
#ARCHIVE = "archive"

#if __name__ == '__main__':
    #date_string = datetime.date.today().strftime("%Y-%m-%d")

    #cur_path = pathlib.Path(".")
    #paths = cur_path.glob(FILE_PATTERN)

    #zip_file_path = cur_path.joinpath(ARCHIVE, date_string +  ".zip")
    #zip_file = zipfile.ZipFile(str(zip_file_path),"w")

    #for path in paths:
       # zip_file.write(str(path))
       # path.unlink()

import zipfile
        
import zipfile
import os


#os.makedirs(os.path.join('Tutorials/zipfiles'))
#zf = zipfile.ZipFile("sample.zip", "w", zipfile.ZIP_DEFLATED)
#zf.write("Tutorials/zipfiles/dataset1.csv")

# Directory 
directory = "compressed"
  
# Parent Directory path 
parent_dir = "Tutorials/zipfiles"
  
# Path 
path = os.path.join(parent_dir, directory) 
  

os.makedirs(path) 
print("Directory '%s' created" %directory) 