#
# Structured with help from https://github.com/Vishal-Kancharla/Gale-Shapley-Algorithm
#

import random

def gale_shapley_match(malePreferences, femalePreferences):
    if len(malePreferences) != len(femalePreferences):
        exit("The number of males and females must match.")

    n = len(malePreferences)
    unmarriedMales = [i for i in range(n)]

    maleSpouse = [None] * n
    femaleSpouse = [None] * n

    nextMaleChoice = [0] * n

    iterations = 0

    while unmarriedMales:
        iterations += 1
        currentMale = unmarriedMales[0]
        currentMalePreferences = malePreferences[currentMale]
        currentFemale = currentMalePreferences[nextMaleChoice[currentMale]]
        currentFemalePreferences = femalePreferences[currentFemale]

        nextMaleChoice[currentMale] += 1

        if femaleSpouse[currentFemale] == None:
            # Tentative acceptance
            maleSpouse[currentMale] = currentFemale
            femaleSpouse[currentFemale] = currentMale

            unmarriedMales.pop(0)
            continue

        else:
            if (currentFemalePreferences.index(currentMale) < currentFemalePreferences.index(femaleSpouse[currentFemale])):
                # If she prefers the new proposal, tentatively accept
                unmarriedMales.pop(0)
                unmarriedMales.append(femaleSpouse[currentFemale])
                femaleSpouse[currentFemale] = currentMale
                maleSpouse[currentMale] = currentFemale
                continue

        # If she doesn't prefer new proposal to existing proposal, do nothing
    for male in range(n):
        print("Male %s matched with female %s" % (male, maleSpouse[male]))
    print("Iterations: %s" % iterations)
    
### Uncomment for fixed example:
# mp = [[0,1,2], [0,1,2], [1,2,0]]
# fp = [[2,1,0], [1,2,0], [2,1,0]]
# gale_shapley_match(mp, fp)

### Uncomment for randomly generated example:
# mp1 = [[i for i in range(50)] for j in range(50)]
# for i in range(50):
#     random.shuffle(mp1[i])
# fp1 = [[i for i in range(50)] for j in range(50)]
# for i in range(50):
#     random.shuffle(fp1[i])
# gale_shapley_match(mp1, fp1)
