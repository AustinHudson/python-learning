import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    score = 0
    tries = 0
    for n in xrange(numTrials):
        bucket = [0, 0, 0, 1, 1, 1]        
        sum_ = 0
        for i in range(3):
            choice = random.choice(range(len(bucket)))
            sum_ += bucket[choice]
            del bucket[choice]
        if sum_ in (0, 3):
            score += 1
        tries += 1
    return float(score)/tries 

print noReplacementSimulation(100000)
