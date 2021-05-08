import pandas as pd
import numpy as np

# Constants to create dictionary fields
keys = ["1Day", "2Days", "3Days", "4Days", "5Days", "6Days", "7Days"]

# Function that averages the followers of each profile for each day, for the first seven days
def calculateFollowersPerDays(groups):

    # List containing for each profile, the average of followers after X days
    list_of_diff = []

    # Index used to select key from "keys" array
    j = 0

    for id, group in groups:

        # Empty dictionary
        dic = {}

        # Get the id of the user
        dic["id"] = id

        # Get the first user_obj reference
        first_day = group.loc[group['age_h'] == 0.0]
        followers_iniziali = int(first_day['followers_count'])


        # Begin: 24
        # Finish: 168
        # Step: 24
        for i in range(24, 192, 24):

            day = group.loc[group['age_h'] == i]
            #print(day)

            # If day X is not present, it means that the profile has been suspended/deleted
            if (day.empty == True):
                # Pandas will automatically exclude NaN numbers from aggregation functions
                diff = float("NaN")
            else:
                followers = int(day['followers_count'])
                #print(followers)

                diff = followers - followers_iniziali
                #print(diff)

            dic[keys[j]] = diff
            
            i = i + 24
            j = j + 1
       
        list_of_diff.append(dic)
        
        j = 0

    return list_of_diff