import time
import sys
import numpy as np
import pandas as pd
from jikanpy import Jikan
api = Jikan()

## ------------------------------------------------------------------------------
## get top 10k anime 15600 / 50 = 312
## get most popular anime + club member amount
## ------------------------------------------------------------------------------

#top_anime = []
#top_anime_list = []
#
#def get_top_anime(y):
#    try:
#        top_anime = api.top(type = 'anime', page = y)
#        for x in range(0, 50):
#            top_anime_list.append([top_anime['top'][x]['mal_id'], top_anime['top'][x]['title'], top_anime['top'][x]['members']])
#        time.sleep(2)
#    except:
#        e = sys.exc_info()[0]
#
#for y in range(1, 314):
#    get_top_anime(y)
#
#top_anime_df = pd \
#    .DataFrame(data=top_anime_list, columns=['mal_id', 'title', 'members']) \
#    .sort_values(['mal_id'], ascending=True)
#top_anime_df.to_csv("anime.csv", encoding='utf-8', index=False)

## ------------------------------------------------------------------------------
##filter out clubs with less than 35 members
## ------------------------------------------------------------------------------

#anime_valid = pd.read_csv("anime.csv").query('members>=35')
#anime_valid.to_csv("anime_valid.csv", encoding='utf-8', index=False)

## ------------------------------------------------------------------------------
## get users from the clubs of most popular anime
## get 10 members from each club OR get 35 members from top 300 clubs
## ------------------------------------------------------------------------------

#search = pd.read_csv("anime_valid.csv")

club = []
member_list = []
def get_club_members( y ):
    try:
        club = api.club(y, 'members')
        for x in range(0, 35):
            if not club['members'][x]['username'] in member_list:
                member_list.append(club['members'][x]['username'])
    except:
        e = sys.exc_info()[0]

for y in range(1, 2):
    get_club_members(y)
    time.sleep(2)

username_df = pd.DataFrame(data=member_list, columns=['username'])
username_df.to_csv("users.csv", encoding='utf-8', index=False)
print(username_df.head())

## ------------------------------------------------------------------------------
## get completed anime amount from user
## ------------------------------------------------------------------------------

#user = []
#user_list = []
#def get_ratings( x ):
#       try:
#           user = api.user(x)
#           user_list.append([anime['username'], user['anime_stats']['completed']])
#       except:
#           e = sys.exc_info()[0]
#for x in member_list:
#    get_ratings( x['members'] )
#    time.sleep(2)
#user_df = pd.DataFrame(data=user_list, columns=['username', 'completed']) 
#print(anime_df.head())
#top_anime_df.to_csv("anime.csv", encoding='utf-8', index=False)

## ------------------------------------------------------------------------------
## get list of rating + mal_id from each user
## ------------------------------------------------------------------------------

#rating = []
#rating_list = []
#def get_ratings( y ):
#    for x in range(0, 35):
#        try:
#            club = api.club(y, 'members')
#            member_list.append(club['members'][x]['username'])
#            time.sleep(2)
#        except:
#            e = sys.exc_info()[0]
#for y in range(1, 300):
#    get_club_members( y )
#username_df = pd.DataFrame(data=member_list, columns=['username'])
#print(username_df)

#https://api.jikan.moe/v3/user/emfcmkh/animelist/completed


