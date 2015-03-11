#This file has code to load all the required data
MoviesDB={}
RatingsDB={}
import Recomentations
#funciton loads movies
def loadMovies():
    try:
        fh = open('y.item')
    except:
        print ('Error loading file ' + fh.name)
        exit()
        
    print('Loading ....')
    for line in fh:
        (mid,name)=line.split('|')[0:2]
        MoviesDB[mid]=name;

    
    
#funciton laods ratings for user,movies
def loadRatings():
    try:
        fh=open('a.base')
    except:
        print ('Error loading file ' + fh.name)
        exit()
        
    print('Loading Ratings ....')
    for line in fh:
        (uid,mid,rating,time)=line.split('\t')
        RatingsDB.setdefault(uid,{})
        RatingsDB[uid][MoviesDB[mid]]=float(rating)

        
            
