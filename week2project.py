# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()
# finding best math schools
best_math_schools=schools[schools["average_math"]>=640][["school_name","average_math"]]
best_math_schools=best_math_schools.sort_values("average_math",ascending=False)
print(best_math_schools)
print(schools.columns)

# finding top 10 schools with best SAT
schools["total_SAT"]=schools["average_math"]+schools["average_reading"]+schools["average_writing"]
top_10_schools=schools.sort_values("total_SAT",ascending=False).head(10)[["total_SAT","school_name"]]
print(top_10_schools)
# Finding school with largest standard deviation of SAT
largest_std_dev=schools.groupby("borough").agg(
num_schools=("school_name","count"),
average_SAT=("total_SAT","mean"),
std_SAT=("total_SAT","std")
).round(2)
largest_std_dev=largest_std_dev.sort_values("std_SAT",ascending=False).head(1).reset_index()
print(largest_std_dev)
