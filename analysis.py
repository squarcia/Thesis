import pandas as pd
import numpy as np
import pickle5 as pickle
from datetime import datetime
from util.calculate import calculateFollowersPerDays as calculateFollowers
import matplotlib
import matplotlib.pyplot as plt

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
#      Media e Dev. Std primi 7gg
#           ----- *** -----

_list = calculateFollowers(groupby_df)

# Create the average Dataframe
df_followers_7gg = pd.DataFrame(_list)

# +++++ È utile per vedere quali profili hanno più followers (serve per verifica dev. std) +++++
#print(df_followers_7gg.nlargest(10, '1Day'))

# Calculate, for each column, standard deviation
stds_array = df_followers_7gg.std()

# Calculate, for each column, average
df_avg_days = df_followers_7gg.mean()
df_avg_days_new = np.array(df_avg_days.values)

# Delete the inf value at the top of array
avg_array = np.delete(df_avg_days_new, 0)

days = range(1, 8)

# Plot mean
plt.plot(days, avg_array, label = "Avg")

# Plot std dev
plt.plot(days, stds_array, label = "Dev. Std.")

# Set x-label
plt.xlabel('Days')

# Set y-label
plt.ylabel('Followers')

# Set title
plt.title('Average and dev. std. followers')

# Set legend
plt.legend()

# Show plot
plt.show()








