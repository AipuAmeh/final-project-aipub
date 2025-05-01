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
# weeks show where the percentage of women who were vaccinated are 0
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
    weekly_disparities_df = pd.DataFrame(weekly_disparities_list)
    weekly_disparities_df["week_ending_date"] = pd.to_datetime(weekly_disparities_df["week_ending_date"])
    weekly_disparities_df.columns = ["Week_Ending_Date", "Demographics", "Num_Pregnant_Women"]
        
# weekly_disparities()


# Question B: What does it look like over time? 
def over_time():
    data_file = get_rsv_data()
    disparities_over_time = []
    for item in data_file:
        disparities_over_time.append({
            "week_ending_date": item.get("week_ending_date"),
            "percent_vaccinated": item.get("cover_estimate"),
            "demographic": item.get("demographic")
        })
    disparities_over_time_df = pd.DataFrame(disparities_over_time)
    disparities_over_time_df["week_ending_date"] = pd.to_datetime(disparities_over_time_df["week_ending_date"])
    disparities_over_time_df.columns = ["Week_Ending_Date","Percent_Vaccinated", "Demographics"]

# over_time()

# Question C: What is breakdown of racial groups included in study?
# show piechart of race/ethnicity
def demographics_breakdown():
    data_file = get_rsv_data()
    asian = []
    pacific_island = []
    black = []
    native = []
    white = []
    hispanic = []
    unknown = []
    
    for item in data_file:
        race = item.get("demographic")
        match race:
            case _ if race.startswith("Black"):
                black.append(item.get("denominator"))
            case _ if race.startswith("American"):
                native.append(item.get("denominator"))
            case _ if race.startswith("Asian"):
                asian.append(item.get("denominator"))
            case _ if race.startswith("Hispanic"):
                hispanic.append(item.get("denominator"))
            case _ if race.startswith("White"):
                white.append(item.get("denominator"))
            case _ if race.startswith("Native"):
                pacific_island.append("denominator")
            case _:
                unknown.append("denominator")
    
       
   
        

demographics_breakdown()


