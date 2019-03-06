import time
import sys
import numpy as np
import pandas as pd
from jikanpy import Jikan

api = Jikan()
## get top 10k anime
top_anime = api.top(type='anime', page=2, subtype='upcoming')
print(top_anime['top'][0]['title'])

#anime = []
#anime_list = []
#for x in range(1, 10):
#    try:
#        anime = api.anime(x)
#        anime_list.append([anime['mal_id'], anime['title']])
#        time.sleep(2)
#    except:
#        e = sys.exc_info()[0]
##better and easier to create list first then convert to df, than to append to df
#anime_df = pd.DataFrame(data=anime_list, columns=['mal_id', 'title']) 
#print(anime_df.head())

#club = []
#member_list = []
#def get_club_members( y ):
#    for x in range(0, 5):
#        try:
#            club = api.club(y, 'members')
#            member_list.append(club['members'][x]['username'])
#            time.sleep(2)
#        except:
#            e = sys.exc_info()[0]
#for y in range(1, 3):
#    get_club_members( y )
#username_df = pd.DataFrame(data=member_list, columns=['username'])
#print(username_df)