import pandas as pd
import numpy as np

# Constants to create dictionary fields
keys_d = ["1Day", "2Day", "3Day", "4Day", "5Day", "6Day", "7Day"]
keys_w = ["1Week", "2Week", "3Week", "4Week"]

# Function returning a list containing protected profile identifiers
def deleteProtectedAccounts(df):

    # List of ids
    list_of_id_protected = []

    # Create the groups
    groups = df.groupby("id", as_index=False)
    
    # For each group I check if the profile is protected or not
    for id, group in groups:

        for row in group.itertuples():
        
            # If it is protected I add the id to the list
            if (row.protected == True):
                list_of_id_protected.append(id)
                break
    
    return list_of_id_protected
        
# Function that averages the followers of each profile for each day, for the first seven days
def calculateFollowersPerDays(groups):

    # List containing for each profile, the average of followers after X days
    list_of_followers = []

    # Index used to select key from "keys" array
    j = 0

    for id, group in groups:

        # Empty dictionary
        dic = {}

        # Get the id of the user
        dic["id"] = id

        #protected = group["protected"].isin(['True'])
    

        # Begin: 24
        # Finish: 168
        # Step: 24 = 1 day
        for i in range(24, 192, 24):

            day = group.loc[group['age_h'] == i]
            #print(day)

            # If day X is not present, it means that the profile has been suspended/deleted
            if (day.empty == True):
                # Pandas will automatically exclude NaN numbers from aggregation functions
                followers = float("NaN")
            else:
                followers = int(day['followers_count'])
                #print(followers)

            dic[keys_d[j]] = followers
            
            j = j + 1
       
        list_of_followers.append(dic)
        
        j = 0

    return list_of_followers

# Function that averages the followers of each profile for each day, for the first seven days
def calculateFollowersPerWeeks(groups):

    # List containing for each profile, the average of followers after X days
    list_of_followers = []

    # Index used to select key from "keys" array
    j = 0

    for id, group in groups:

        # Empty dictionary
        dic = {}

        # Get the id of the user
        dic["id"] = id

        # Get the first user_obj reference
        first_week = group.loc[group['age_h'] == 168.0]

        # If the user is suspended before one week, we jump to another user
        if (first_week.empty):
            continue


        # Begin: 168
        # Finish: 672
        # Step: 168 = 1 week
        for i in range(168, 840, 168):

            day = group.loc[group['age_h'] == i]
            #print(day)

            # If day X is not present, it means that the profile has been suspended/deleted
            if (day.empty == True):
                # Pandas will automatically exclude NaN numbers from aggregation functions
                diff = float("NaN")
            else:
                followers = int(day['followers_count'])

            dic[keys_w[j]] = followers
            
            j = j + 1
       
        list_of_followers.append(dic)
        
        j = 0

    return list_of_followers



# Function that averages the followers of each profile for each day, for the first seven days
def calculateFriendsPerDays(groups):

    # List containing for each profile, the average of followers after X days
    list_of_friends = []

    # Index used to select key from "keys" array
    j = 0

    for id, group in groups:

        # Empty dictionary
        dic = {}

        # Get the id of the user
        dic["id"] = id

        # Begin: 0
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
                friends = int(day['friends_count'])
                #print(friends)

            dic[keys_d[j]] = friends
            
            j = j + 1
       
        list_of_friends.append(dic)
        
        j = 0

    return list_of_friends

# Function that averages the followers of each profile for each day, for the first seven days
def calculateFriendsPerWeeks(groups):

    # List containing for each profile, the average of followers after X days
    list_of_friends = []

    # Index used to select key from "keys" array
    j = 0

    for id, group in groups:

        # Empty dictionary
        dic = {}

        # Get the id of the user
        dic["id"] = id

        # Get the first user_obj reference
        first_week = group.loc[group['age_h'] == 168.0]

        # If the user is suspended before one week, we jump to another user
        if (first_week.empty):
            continue


        # Begin: 168
        # Finish: 672
        # Step: 168 = 1 week
        for i in range(168, 840, 168):

            day = group.loc[group['age_h'] == i]
            #print(day)

            # If day X is not present, it means that the profile has been suspended/deleted
            if (day.empty == True):
                # Pandas will automatically exclude NaN numbers from aggregation functions
                diff = float("NaN")
            else:
                friends = int(day['friends_count'])

            dic[keys_w[j]] = friends
            
            j = j + 1
       
        list_of_friends.append(dic)
        
        j = 0

    return list_of_friends



# Function that averages the followers of each profile for each day, for the first seven days
def calculateTweetsPerDays(groups):

    # List containing for each profile, the average of followers after X days
    list_of_tweets = []

    # Index used to select key from "keys" array
    j = 0

    for id, group in groups:

        # Empty dictionary
        dic = {}

        # Get the id of the user
        dic["id"] = id

        # Begin: 0
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
                tweets = int(day['statuses_count'])
                #print(friends)

            dic[keys_d[j]] = tweets
            
            j = j + 1
       
        list_of_tweets.append(dic)
        
        j = 0

    return list_of_tweets

# Function that averages the followers of each profile for each day, for the first seven days
def calculateTweetsPerWeeks(groups):

    # List containing for each profile, the average of followers after X days
    list_of_tweets = []

    # Index used to select key from "keys" array
    j = 0

    for id, group in groups:

        # Empty dictionary
        dic = {}

        # Get the id of the user
        dic["id"] = id

        # Get the first user_obj reference
        first_week = group.loc[group['age_h'] == 168.0]

        # If the user is suspended before one week, we jump to another user
        if (first_week.empty):
            continue


        # Begin: 168
        # Finish: 672
        # Step: 168 = 1 week
        for i in range(168, 840, 168):

            day = group.loc[group['age_h'] == i]
            #print(day)

            # If day X is not present, it means that the profile has been suspended/deleted
            if (day.empty == True):
                # Pandas will automatically exclude NaN numbers from aggregation functions
                diff = float("NaN")
            else:
                tweets = int(day['statuses_count'])

            dic[keys_w[j]] = tweets
            
            j = j + 1
       
        list_of_tweets.append(dic)
        
        j = 0

    return list_of_tweets


# Function that returns the bins for the first day, the first week and the first 28 days
def getBins(groupby_df, type):

    bins_1st_day = calculateBins(groupby_df, 0, 48, type) 
        
    bins_7_days = calculateBins(groupby_df, 0, 192, type) 

    bins_28_days = calculateBins(groupby_df, 0, 696, type) 


    return bins_1st_day, bins_7_days, bins_28_days

# Function that calculates bins for the first day, the first week and the first 28 days
def calculateBins(groups, x, y, type):

    arr = []

    for id, group in groups:
        
        i = x

        # Begin: x
        # Finish: y
        # Step: 24 = 1 day
        for i in range(i, y, 24):

            day = group.loc[group['age_h'] == i]
            #print(day)

            # If day X is not present, it means that the profile has been suspended/deleted
            if (day.empty == True):
                # It means that the account is deleted/suspended --> irrelevant for count the tweets
                break

            else:
                stats = int(day[type])
                #print(stats)

                arr.append(stats)
    
    return arr

def showIfSuspended(df_inactives, id, hours):

    df_top_follower = pd.DataFrame(df_inactives[df_inactives['id'] == id])
    print(df_top_follower)
    print(df_top_follower.sort_values(by=['age_h']))
    row = df_top_follower.loc[df_top_follower['age_h'] == hours]
    print(row)
