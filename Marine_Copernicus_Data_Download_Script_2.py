import copernicusmarine
import datetime
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

start="01-01-1998"
end="01-01-2003"
endate=None
day= -1
end=datetime.strptime(end, "%d-%m-%Y")
original_date = datetime.strptime(start, "%d-%m-%Y")
print(end)

while day < 0:
    new_date = original_date + relativedelta(months=1)
    # print(new_date.strftime("%Y-%m-%dT00:00:00"))
    endate=new_date-timedelta(days=1)
    # print(endate.strftime("%Y-%m-%dT00:00:00"))

    difference = new_date - end
    day=difference.days

    print("Downloading From : {} To : {}".format(original_date,endate))
    copernicusmarine.subset(
  dataset_id="cmems_mod_glo_bgc_my_0.083deg-lmtl_PT1D-i",
  variables=["zooc"],
  username="*****",password="*****",
  minimum_longitude=-180,
  maximum_longitude=179.9166717529297,
  minimum_latitude=-80,
  maximum_latitude=89.91666412353516,
  start_datetime=original_date,
  end_datetime=endate,
  force_download=True,
  output_directory="G:/Zooplankton/",
  output_filename="Zooplankton_Data_{}".format(original_date.strftime("%Y-%m"))
)
    original_date=new_date
    
