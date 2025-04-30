import requests
import pandas as pd

## Research Question: Are there specific racial and ethnic disparities in weekly RSV vaccination coverage rates among pregnant women?

    # Key:
    # demographic: dem info of pregnant women
    # denonimator: estimated # of pregnant women aged 18-49 years 
    # cover_estimate: percentage of pregnant women who were vaccinated

# Get data
def get_rsv_data():
    data_url ="https://data.cdc.gov/resource/g4jn-64pd.json"
    data_file = requests.get(data_url)
    data_file = data_file.json()
    return data_file
    # rsv_df = pd.DataFrame(data_file)
    # print(rsv_df)

get_rsv_data()
# Question A: At what weeks are these disparities most pronounced? 
# made a df table that shows columns for weeks, ethnicity, percentage of vaccinations
# find weeks were coverage is 0 and plot bar chart for percentage of demographics
    ## shows which demographics did not get vaccinated at these weeks
def weekly_disparities():
    data_file = get_rsv_data()
    weekly_disparities = []
    for item in data_file:
        cover_estimate = float(item.get("cover_estimate"))
        if (cover_estimate) == 0:
            weekly_disparities.append({
                "week_ending_date": item.get("week_ending_date"),
                "demographic": item.get("demographic")
            })
    weekly_disparities_df = pd.DataFrame(weekly_disparities)
    weekly_disparities_df.columns = ["Week_Ending_Date", "Demographics"]
    print(weekly_disparities_df)
        

weekly_disparities()
# Question B: What does it look like over time? 
# line graph showing weeks and percentage of women in each racial group?


# Question C: What is breakdown of racial groups?
# show piechart of race/ethnicity

