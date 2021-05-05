import pandas as pd
import numpy as np
import pickle5 as pickle
from datetime import datetime
"""

#   ----- *** -----
#      Inactives
#   ----- *** -----


# Create the inactives Dataframe
inactives = pd.read_pickle("./pickle/inactives_key_data_0-5k.pickle")
df_inactives = pd.DataFrame(inactives)


# Convert all the dates to YYYY:MM:DD HH:MM:SS
for i, row in df_inactives.iterrows():
    date = datetime.strptime(row.found_at, '%a %b %d %H:%M:%S %z %Y')
    df_inactives._set_value(i, 'found_at', date)

with open('./pickle/inactives_key_data_0-5k.pickle', 'wb') as g:
    pickle.dump(df_inactives, g)

"""

#   ----- *** -----
#      User Objs
#   ----- *** -----


# Create the user object Dataframe
user_objs = pd.read_pickle("./pickle/user_objects_key_data_0-5k.pickle")
df_user_objs = pd.DataFrame(user_objs)


# Convert all the dates to YYYY:MM:DD HH:MM:SS
for i, row in df_user_objs.iterrows():

    date_f = datetime.strptime(row.found_at, '%a %b %d %H:%M:%S %z %Y')
    df_user_objs._set_value(i, 'found_at', date_f)

    date_c = datetime.strptime(row.created_at, '%a %b %d %H:%M:%S %z %Y')
    df_user_objs._set_value(i, 'created_at', date_c)

with open('./pickle/user_objects_key_data_0-5k.pickle', 'wb') as g:
    pickle.dump(df_user_objs, g)