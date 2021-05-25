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

# Get all the protected accounts
list_of_id_protected = cf.deleteProtectedAccounts(df_user_objs)

# Delete all the protected accounts
df_user_objs_without_protected = df_user_objs[~df_user_objs['id'].isin(list_of_id_protected)]

# 5000 user --> OK!
groupby_df = df_user_objs.groupby("id", as_index=False)

# Dataframe without protected profiles (used in tweets analysis)
groupby_df_only_for_tweets = df_user_objs_without_protected.groupby("id", as_index=False)

# 5000 user --> OK!
groupby_df_inactives = df_inactives.groupby("id", as_index=False)

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
_list_days_tweets = cf.calculateTweetsPerDays(groupby_df_only_for_tweets)
_list_weeks_tweets = cf.calculateTweetsPerWeeks(groupby_df_only_for_tweets)



#   ---------- *** ----------
#     SHOWS FOLLOWERS STATS
#   ---------- *** ----------

# Create the average days Dataframe
df_followers_7gg = pd.DataFrame(_list_days_followers)

# Create the average weeks Dataframe
df_followers_4week = pd.DataFrame(_list_weeks_followers)


sS.showBoxPlots(df_followers_7gg, "first_week", "Followers")
sS.showBoxPlots(df_followers_4week, "first_month", "Followers")



#   ---------- *** ----------
#       SHOWS FRIENDS STATS
#   ---------- *** ----------


# Create the average days Dataframe
df_friends_7gg = pd.DataFrame(_list_days_friends_)

# Create the average weeks Dataframe
df_friends_4week = pd.DataFrame(_list_weeks_friends)

sS.showBoxPlots(df_friends_7gg, "first_week", "Friends")
sS.showBoxPlots(df_friends_4week, "first_month", "Friends")



#   ---------- *** ----------
#       SHOWS TWEETS STATS
#   ---------- *** ----------


# Create the average days Dataframe
df_tweets_7gg = pd.DataFrame(_list_days_tweets)

# Create the average weeks Dataframe
df_tweets_4week = pd.DataFrame(_list_weeks_tweets)

sS.showBoxPlots(df_tweets_7gg, "first_week", "Tweets")
sS.showBoxPlots(df_tweets_4week, "first_month", "Tweets")




#   ---------- *** ----------
#        SHOWS HISTOGRAMS
#   ---------- *** ----------


# Tweets
sS.showBins(groupby_df, 'statuses_count')

# Followers
sS.showBins(groupby_df, 'followers_count')

# Friends
sS.showBins(groupby_df, 'friends_count')




#   ---------- *** ----------
#         TOP 20 TWEETERS
#   ---------- *** ----------


top_20_4week = df_tweets_4week.nlargest(20, "4Week")
#print(top_20_4week)

top_20_1week = df_tweets_4week.nlargest(20, "1Week")
#print(top_20_1week)

top_20_1day = df_tweets_7gg.nlargest(20, "7Day")
#print(top_20_1day)




#   ---------- *** ----------
#   SUSPENDED/DELETED PROFILES
#   ---------- *** ----------


# Take the last records for each profile from the inactives table
last_items_each_groups = pd.DataFrame(groupby_df_inactives.last())

# Verify that the profiles that tweeted the most were then suspended
top_20_4week_susdel = top_20_4week.merge(last_items_each_groups, how='inner', on='id')

# Verify that the profiles that tweeted the most were then suspended
top_20_7gg_susdel = top_20_1week.merge(last_items_each_groups, how='inner', on='id')




#   ---------- *** ----------
#        WORD CLOUD TWEETS
#   ---------- *** ----------


