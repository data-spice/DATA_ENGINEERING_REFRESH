import sys
print ("arguements", sys.argv)

day = int(sys.argv[1])
print(f"Running pipeline for a {day}")
month = int(sys.argv[2])


import pandas as pd
df =pd.DataFrame({"Day":[1,2],"num_passengers":[3,4]})
df["month"]=month
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.paraquet")


