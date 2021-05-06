import pandas as pd
import numpy as np
import pickle5 as pickle


#       ----- ***** -----
#       Inactives Section
#       ----- ***** -----

# Unpickling data
inactives = pd.read_pickle('./pickle/inactives_0-5k.pickle')

# Empty list that will contain only, for each dictionary, the part relevant for the purposes of analysis
inactives_list = []

# Browse the entire pickle file by selecting and saving the important information for the purpose
for i in range(len(inactives)):

    # Reference to the element
    dic = inactives[i]

    # Get the id of the profile
    id = dic["_source"]["id_str"]

    # Get the deleted value
    deleted = dic["_source"]["meta"]["deleted"]

    # Get the found_at date
    found_at = dic["_source"]["meta"]["found_at"]

    # Get the number of days from creation_date to found_at date (in hours)
    age_h = dic["_source"]["meta"]["age_h"]

    # Create new dict 
    new_row = { "id": id,
                "deleted": deleted, 
                "found_at": found_at, 
                "age_h": age_h
    }

    # Append the dict to the list
    inactives_list.append(new_row)

# Save all to pickle file
with open('./pickle/inactives_key_data_0-5k.pickle', 'wb') as g:
    pickle.dump(inactives_list, g)




#       ----- ***** -----
#       User objs Section
#       ----- ***** -----

# Unpickling data
user_objs = pd.read_pickle("./pickle/user_objects_0-5k.pickle")

# Empty list that will contain only, for each dictionary, the part relevant for the purposes of analysis
user_objs_list = []

# Browse the entire pickle file by selecting and saving the important information for the purpose
for i in range(len(user_objs)):

    # Reference to the element
    dic = user_objs[i]

    # Get the id of the profile
    id = dic["_source"]["id_str"]

    # Get the creation date
    created_at = dic["_source"]["created_at"]

    # Get the number of tweets liked
    tweetsLiked = dic["_source"]["favourites_count"]

    # Get the number of followers 
    followersCount = dic["_source"]["followers_count"]

    # Get the number of friends
    friendsCount = dic["_source"]["friends_count"]

    # Get the number of tweets
    statuses_count = dic["_source"]["statuses_count"]

    # Get the found_at date
    found_at = dic["_source"]["meta"]["found_at"]

    # Get the number of days from creation_date to found_at date (in hours)
    age_h = dic["_source"]["meta"]["age_h"]

    # Create new dict 
    new_row = { "id": id,
                "created_at": created_at,
                "favourites_count": tweetsLiked,
                "followers_count": followersCount,
                "friends_count": friendsCount, 
                "statuses_count": statuses_count,
                "found_at": found_at, 
                "age_h": age_h
    }

    # Append the dict to the list
    user_objs_list.append(new_row)

# Save all to pickle file
with open('./pickle/user_objects_key_data_0-5k.pickle', 'wb') as f:
    pickle.dump(user_objs_list, f)