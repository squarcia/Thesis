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


#           ----- *** -----
#      Media e Dev. Std primi 7gg/28gg
#           ----- *** -----

_list_days = cf.calculateFollowersPerDays(groupby_df)
_list_weeks = cf.calculateFollowersPerWeeks(groupby_df)

# Create the average days Dataframe
df_followers_7gg = pd.DataFrame(_list_days)

# Create the average weeks Dataframe
df_followers_4week = pd.DataFrame(_list_weeks)

sS.showDaysStats(df_followers_7gg)
sS.showWeeksStats(df_followers_4week)


