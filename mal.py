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

def get_anime_list():
    top_anime = []
    top_anime_list = []
    def get_top_anime(y):
        try:
            top_anime = api.top(type = 'anime', page = y)
            for x in range(0, 500):
                top_anime_list.append([top_anime['top'][x]['mal_id'], top_anime['top'][x]['title'], top_anime['top'][x]['members']])
            time.sleep(2)
        except:
            e = sys.exc_info()[0]
    for y in range(1, 3120):
        print((y / 3120) * 100)
        get_top_anime(y)
    top_anime_df = pd \
        .DataFrame(data=top_anime_list, columns=['mal_id', 'title', 'members']) \
        .sort_values(['mal_id'], ascending=True)
    top_anime_df.to_csv("anime.csv", encoding='utf-8', index=False)

# get_anime_list()

## ------------------------------------------------------------------------------
## filter out clubs with less than 35 members
## ------------------------------------------------------------------------------

def filter_clubs():
    anime_valid = pd.read_csv("anime.csv").query('members>=35')
    anime_valid.to_csv("anime_valid.csv", encoding='utf-8', index=False)

# filter_clubs()

## ------------------------------------------------------------------------------
## get users from the clubs of most popular anime
## get 10 members from each club OR get 35 members from top n clubs
## ------------------------------------------------------------------------------

def get_club_members():
    search = pd.read_csv("anime_valid.csv")
    club = []
    member_list = []
    def get_single_club_members(y):
        try:
            club = api.club(y, 'members')
            for x in range(0, 100):
                if not club['members'][x]['username'] in member_list:
                    member_list.append(club['members'][x]['username'])
        except:
            e = sys.exc_info()[0]
    for y in range(1, 5001):
        get_club_members(y)
        print((y / 5001) * 100)
        time.sleep(2)
    username_df = pd.DataFrame(data=member_list, columns=['username'])
    username_df.to_csv("users.csv", encoding='utf-8', index=False)

# get_club_members()

## ------------------------------------------------------------------------------
## get list of rating + mal_id from each user
## ------------------------------------------------------------------------------

def get_ratings():
    search = pd.read_csv("./backup/users.csv")
    ratings = []
    ratings_list = []
    def get_ratings_from_user(y):
        try:
            ratings = api.user(username=y, request='animelist', argument='completed', page=1)
            for x in range(0, 400):
                ratings_list.append([y, ratings['anime'][x]['mal_id'], ratings['anime'][x]['score']])
        except:
            e = sys.exc_info()[0]
    rangelength = len(search) - 1
    print(rangelength)
    for i in range(0, rangelength):
        get_ratings(search.iloc[i]['username'])
        print((i / rangelength) * 100)
        time.sleep(2)
    ratings_df = pd.DataFrame(data=ratings_list, columns=['username', 'mal_id', 'score'])
    ratings_df.to_csv("ratings.csv", encoding='utf-8', index=False)

# get_ratings()

## ------------------------------------------------------------------------------
## remove ratings with 0 values
## ------------------------------------------------------------------------------

def clean_ratings():
    ratings_unclean = pd.read_csv("ratings.csv") 
    ratings_clean = ratings_unclean[ratings_unclean['score'] > 0]
    print(ratings_unclean.count())
    print(ratings_clean.count())
    ratings_clean.to_csv("ratings_valid.csv", encoding='utf-8', index=False)

# clean_ratings()













## ------------------------------------------------------------------------------
## get completed anime amount from user ?maybe? nox
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
