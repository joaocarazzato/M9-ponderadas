import polars as pl


# Read data file
df = pl.scan_csv(
    "measurements.txt", # 1b line archive
    separator=";", # archive data separator
    has_header=False, # first line is header(col_name)?
    with_column_names=lambda cols: ["station_name", "measurement"], # creating anonymous function to set column names as argument "cols"
)

# Group data in one dataframe
grouped = (
    df.group_by("station_name") # grouping data by station name
    .agg( # Aggregations for each group of operation(and doing the operations)
        pl.min("measurement").alias("min_measurement"), # create col for min value measurement
        pl.mean("measurement").alias("mean_measurement"), # create col for mean value measurement
        pl.max("measurement").alias("max_measurement"), # create col for max value measurement
    )
    .sort("station_name") # sorting df by station name followed by each of it's own values
    .collect(streaming=True) # materialize to dataframe
)
print(grouped) # print df

# Print final results
print("{", end="")
for data in grouped.iter_rows(): # get data for each row
    print(
        f"{data[0]} = min_val: {data[1]:.1f} | mean_val: {data[2]:.1f} | max_val: {data[3]:.1f}", # (Station_name = min_value | mean_value | max_value)
        end=", \n",
    )
print("\b\b} ")
