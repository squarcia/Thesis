import pandas as pd
import numpy as np
import pickle5 as pickle
from datetime import datetime
import util.calculate as cf
import util.showStats as sS

# Create the inactives Dataframe
inactives = pd.read_pickle("./pickle/inactives_key_data_0-5k.pickle")
df_inactives = pd.DataFrame(inactives)

# Order the inactives Dataframe by id and ascending found_at date
df_inactives = df_inactives.sort_values(by=['id', 'found_at'])

# Create the user object Dataframe
user_objs = pd.read_pickle("./pickle/user_objects_key_data_0-5k.pickle")
df_user_objs = pd.DataFrame(user_objs)

# Order the inactives Dataframe by id and ascending found_at date
df_user_objs = df_user_objs.sort_values(by=['id', 'found_at'])

# I get all user objects with 28gg
df_user_objs = df_user_objs[df_user_objs['age_h'] <= 672]

# 5000 user --> OK!
groupby_df = df_user_objs.groupby("id", as_index=False)



#            ----- *** -----
#     Create Dataframes for analysis          
#            ----- *** -----


# Get aggregate data for followers_count field
_list_days_followers = cf.calculateFollowersPerDays(groupby_df)
_list_weeks_followers = cf.calculateFollowersPerWeeks(groupby_df)


# Get aggregate data for friend_count field
_list_days_friends_ = cf.calculateFriendsPerDays(groupby_df)
_list_weeks_friends = cf.calculateFriendsPerWeeks(groupby_df)


# Get aggregate data for statuses_count field
_list_days_tweets = cf.calculateTweetsPerDays(groupby_df)
_list_weeks_tweets = cf.calculateTweetsPerWeeks(groupby_df)





#   ---------- *** ----------
#     SHOWS FOLLOWERS STATS
#   ---------- *** ----------

# Create the average days Dataframe
df_followers_7gg = pd.DataFrame(_list_days_followers)

# Create the average weeks Dataframe
df_followers_4week = pd.DataFrame(_list_weeks_followers)

sS.show(df_followers_7gg, "first_week", "Followers")
sS.show(df_followers_4week, "first_month", "Followers")



#   ---------- *** ----------
#       SHOWS FRIENDS STATS
#   ---------- *** ----------


# Create the average days Dataframe
df_friends_7gg = pd.DataFrame(_list_days_friends_)

# Create the average weeks Dataframe
df_friends_4week = pd.DataFrame(_list_weeks_friends)

sS.show(df_friends_7gg, "first_week", "Friends")
sS.show(df_friends_4week, "first_month", "Friends")



#   ---------- *** ----------
#       SHOWS TWEETS STATS
#   ---------- *** ----------


# Create the average days Dataframe
df_tweets_7gg = pd.DataFrame(_list_days_tweets)

# Create the average weeks Dataframe
df_tweets_4week = pd.DataFrame(_list_weeks_tweets)

sS.show(df_tweets_7gg, "first_week", "Tweets")
sS.show(df_tweets_4week, "first_month", "Tweets")

