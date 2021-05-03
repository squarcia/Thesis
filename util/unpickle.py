import pandas as pd
import numpy as np
from datetime import datetime


#       ----- ***** -----
#       Inactives Section
#       ----- ***** -----

# Unpickling data
inactives = pd.read_pickle('./pickle/inactives_0-5k.pickle')

# A dataframe is created to hold important information
df = pd.DataFrame(columns=('_id', 'deleted', 'found_at', 'age_h'))

# Browse the entire pickle file by selecting and saving the important information for the purpose
for i in range(len(inactives)):

    dic = inactives[i]

    _id = dic["_id"]

    deleted = dic["_source"]["meta"]["deleted"]
    deleted = 1 if deleted == True else 0

    found_at = dic["_source"]["meta"]["found_at"]
    data_modified = datetime.strptime(found_at, '%a %b %d %H:%M:%S %z %Y')

    age_h = dic["_source"]["meta"]["age_h"]

    new_row = { "_id": _id,
                "deleted": deleted, 
                "found_at": data_modified, 
                "age_h": age_h
    }

    # Store into Dataframe
    df = df.append(new_row, ignore_index=True)

# Save all to pickle file
df.to_pickle("./pickle/inactives_key_data_0-5k.pickle")




#       ----- ***** -----
#       User objs Section
#       ----- ***** -----

# Unpickling data
user_objs = pd.read_pickle("./pickle/user_objects_0-5k.pickle")

# A dataframe is created to hold important information
df = pd.DataFrame(columns=('_id', 'created_at', 'favourites_count', 'followers_count', 'friends_count', 'found_at', 'age_h'))



# Browse the entire pickle file by selecting and saving the important information for the purpose
for i in range(len(user_objs)):
    
    dic = user_objs[i]

    _id = dic["_id"]

    created_at = dic["_source"]["created_at"]
    created_at = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')

    tweetsLiked = dic["_source"]["favourites_count"]
    followersCount = dic["_source"]["followers_count"]
    friendsCount = dic["_source"]["friends_count"]

    found_at = dic["_source"]["meta"]["found_at"]
    data_modified = datetime.strptime(found_at, '%a %b %d %H:%M:%S %z %Y')

    age_h = dic["_source"]["meta"]["age_h"]

    new_row = { "_id": _id,
                "created_at": created_at,
                "favourites_count": tweetsLiked,
                "followers_count": followersCount,
                "friends_count": friendsCount, 
                "found_at": data_modified, 
                "age_h": age_h
    }

    df = df.append(new_row, ignore_index=True)

# Save all to pickle file
df.to_pickle("./pickle/user_objects_key_data_0-5k.pickle")



