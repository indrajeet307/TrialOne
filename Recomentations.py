# A dictionary of movie critics and their ratings of a small
# A blank line
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

#Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,p1,p2):
    #get the list of shared items
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    #if they have no ratings in common, return 0
    if len(si) == 0 : return 0

    #addup the squares of all the differences
    sum_of_squares=sum([pow(prefs[p1][item]-prefs[p2][item],2)
                        for item in prefs[p1] if item in prefs[p2]])

    return 1/(1+sum_of_squares)

#return a pearsons coreelation
def sim_pearson(prefs,p1,p2):
    #get list of shared items
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    #number of shared items
    n=len(si)

    #return if number is zero
    if n == 0 : return 0

    #Add up all the preferences
    sum1 = sum([prefs[p1][i] for i in si])
    sum2 = sum([prefs[p2][i] for i in si])

    #sum up the squares
    sum1Sq = sum([pow(prefs[p1][i],2) for i in si])
    sum2Sq = sum([pow(prefs[p2][i],2) for i in si])

    #sum up the products
    pSum = sum([prefs[p1][i]*prefs[p2][i] for i in si])

    #calculate the pearson score
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den == 0 : return 0

    return num/den

#Return the best matches for the person from prefs dictionary
#Number of results and similarity functions are optional params
def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
            for other in prefs if other != person]

    #sort the list so the highest scores appear at top
    scores.sort()
    scores.reverse()
    return scores[0:n]

# Gets recommendations for a person by using a weighted average
# of every other users rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for others in prefs:
            #dont compare me to myself
            if others==person : continue
            sim=similarity(prefs,person,others)

            #ignore scores of zero or lower
            if sim<=0 : continue
            for item in prefs[others]:
                    # only score movies That I have not seen
                    if item not in prefs[person] or prefs[person][item]==0:
                            #similarity * score
                            totals.setdefault(item,0)
                            totals[item]+=prefs[others][item]*sim
                            #Sum of similarities
                            simSums.setdefault(item,0)
                            simSums[item]+=sim

    #create the normalized list
    rankings=[(total/simSums[item],item)for item,total in totals.items()]

    # return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings

# suggesting item item similarity
def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})

            #Flip item and person
            result[item][person]=prefs[person][item]

    return result

#display critics properly
def showPrefs(prefs):
    for name in prefs:
        print (name)
        for item in prefs[name]:
            print (item, ':' , prefs[name][item])
    return 0
