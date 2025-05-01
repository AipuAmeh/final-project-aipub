import requests
import pandas as pd

## Research Question: Are there specific racial and ethnic disparities in weekly RSV vaccination coverage rates among pregnant women?

# Get data
def get_rsv_data():
    data_url ="https://data.cdc.gov/resource/g4jn-64pd.json"
    data_file = requests.get(data_url)
    data_file = data_file.json()
    return data_file


get_rsv_data()
# Question A: At what weeks are these disparities most pronounced? 
def weekly_disparities():
    data_file = get_rsv_data()
    weekly_disparities_list = []

    # filter data
    for item in data_file:
        cover_estimate = float(item.get("cover_estimate"))
        if (cover_estimate) == 0:
            weekly_disparities_list.append({
                "week_ending_date": item.get("week_ending_date"),
                "demographic": item.get("demographic"),
                "num_pregnant_women": item.get("denominator")
            })
    weekly_disparities_df =  pd.DataFrame(weekly_disparities_list)
    weekly_disparities_df["week_ending_date"] = pd.to_datetime(weekly_disparities_df["week_ending_date"])
    weekly_disparities_df.columns = ["Week_Ending_Date", "Demographics", "Num_Pregnant_Women"]
    print(weekly_disparities_df)
        
weekly_disparities()


# Question B: What does it look like over time? 
# line graph showing weeks and percentage of women in each racial group?


# Question C: What is breakdown of racial groups?
# show piechart of race/ethnicity

