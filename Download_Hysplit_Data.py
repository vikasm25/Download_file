
import os
import wget
import pandas as pd 
import time

# File path which contains list of files to be downloaded
input="D:/New_FTP.xlsx"

# Path where file to be downloaded
path='D:/HYSPLIT_Data/'

#List of files which already exist in the directory
list=os.listdir(path)
print(list)

#Read file which contains input list of files to be downloaded
file=pd.read_excel(input)

#Empty list to store file name which can't be downloaded due to error
error=[]
# print(file['Name'][1][18:])

#Loop to download all the files and skip file which already exist
for i in range(len(file)):
    t_s = time.time()
    print("\n{}. File  Name : {}".format(i+1,file['Name'][i][18:]))
    link="ftp://arlftp.arlhq.noaa.gov"+file['Name'][i]
    if file['Name'][i][18:] in list:
        print("File already Exist")
        pass
    else:
        try:
            print(link)
            wget.download(link,path)
        except Exception as e:
            print("Error Downloading : {} \n {}\n".format(file['Name'][i][18:],e))
            error.append(file['Name'][i])        
            pass
    
    t_e = time.time()
    print('\nTotal Time: %f minutes = %f hours.' % ( (t_e - t_s) / 60.0 , (t_e - t_s) / 3600.0 ))
    
#create dataframe for file not downloaded and store in a excel file
err=pd.DataFrame({'Error':error})
err.to_excel("D:/error.xlsx",index=True,sheet_name='Error')
    

