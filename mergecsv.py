import os, glob
import pandas as pd

#get a list of the csv files in the location
path = 'D:\\GoogleDrive\\bikedata'
all_files = glob.glob("*.csv")#os.path.join(path, "*.csv"
print(all_files)
#loop through and read all the csv files, cat them together to make one file dropping the header, and make new csv file
df_merged = (pd.read_csv(f, sep=',') for f in all_files)
df_merged = pd.concat(df_merged, ignore_index=True)
df_merged.to_csv( "all_merged.csv")
print("file ready: all_merged.csv ")
