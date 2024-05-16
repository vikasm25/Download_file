# Import modules 
import copernicusmarine
from pprint import pprint

# Starting Month and Year
m_start=9               #Month
y_start=2012            #Year

#Empty list to store Date
date=[]

#Loop to list of Date for which data to be downloaded
for i in range(1,14):
    if m_start<10:
        date.append(str(y_start)+"0"+str(m_start)+"*")
    else:
        date.append(str(y_start)+str(m_start)+"*")
        
    m_start=m_start+1
    if m_start == 13:
        m_start =1
        y_start=y_start+1        
    
print(date)   

#Project from which data is to be downloaded
data="cmems_mod_glo_phy_my_0.083_P1M-m"

# Define output Directory
output_directory = "G:/Data/"

# Call the get function for each dataset to save files for the date range 
for dat in date:
    get_files = copernicusmarine.get(
        dataset_id=data,
        username="*********", password="********",force_download=True,
        output_directory=output_directory,
        filter=dat
    )