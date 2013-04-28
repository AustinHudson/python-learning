# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b_precompiled_27 import *


#
# PROBLEM 1
#
def simulationWithDrugDelayed(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, delay):    
    viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in xrange(numViruses)]
    patient = TreatedPatient(viruses, maxPop)        
    for i in xrange(delay):
        patient.update()                                    
    patient.addPrescription("guttagonol")
    for i in xrange(150):
        patient.update()
    return patient.getTotalPop()

def simulationDelayedTreatmentDelay(numTrials, delay):    
    population = [0] * numTrials;
    for i in xrange(numTrials):
        population[i] = simulationWithDrugDelayed(100, 1000, .1, .05, {'guttagonol': False}, .005, delay)
    return population

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    p300 = simulationDelayedTreatmentDelay(numTrials, 300)
    p150 = simulationDelayedTreatmentDelay(numTrials, 150)
    p75 = simulationDelayedTreatmentDelay(numTrials, 75)
    p0 = simulationDelayedTreatmentDelay(numTrials, 0)
    minP = min([ min(p300), min(p150), min(p75), min(p0) ]) - 10
    maxP = max([ max(p300), max(p150), max(p75), max(p0) ]) + 10
    
    pylab.subplot(221)
    pylab.hist(p300, bins=101)
    pylab.xlim(minP, maxP)
    pylab.title('delay = 300')
    
    pylab.subplot(222)
    pylab.hist(p150, bins=101)
    pylab.xlim(minP, maxP)
    pylab.title('delay = 150')
    
    pylab.subplot(223)
    pylab.hist(p75, bins=101)
    pylab.xlim(minP, maxP)
    pylab.title('delay = 75')
    
    pylab.subplot(224)
    pylab.hist(p0, bins=101)
    pylab.xlim(minP, maxP)
    pylab.title('delay = 0')
    
    pylab.show()


#
# PROBLEM 2
#
def sim2drugs(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, delay):    
    viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in xrange(numViruses)]
    patient = TreatedPatient(viruses, maxPop)
    
    for i in xrange(150):
        patient.update()
        
    patient.addPrescription("guttagonol")    
    for i in xrange(delay):
        patient.update()                                    

    patient.addPrescription("grimpex")
    for i in xrange(150):
        patient.update()

    return patient.getTotalPop()


def sim2drugsNumTrials(numTrials, delay):    
    population = [0] * numTrials;
    for i in xrange(numTrials):
        population[i] = simulationWithDrugDelayed(100, 1000, .1, .05, {'guttagonol': False, 'grimpex': False}, .005, delay)
    return population

def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    print("simulation start...")
    p300 = sim2drugsNumTrials(numTrials, 300)
    print("simulation with delay 300 - DONE")
    p150 = sim2drugsNumTrials(numTrials, 150)
    print("simulation with delay 150 - DONE")
    p75 = sim2drugsNumTrials(numTrials, 75)
    print("simulation with delay 75 - DONE")
    p0 = sim2drugsNumTrials(numTrials, 0)
    print("simulation with delay 0 - DONE")
    minP = min([ min(p300), min(p150), min(p75), min(p0) ]) - 10
    maxP = max([ max(p300), max(p150), max(p75), max(p0) ]) + 10
    
    pylab.subplot(221)
    pylab.hist(p300, bins=101)
    pylab.xlim(minP, maxP)
    pylab.title('delay = 300')
    
    pylab.subplot(222)
    pylab.hist(p150, bins=101)
    pylab.xlim(minP, maxP)
    pylab.title('delay = 150')
    
    pylab.subplot(223)
    pylab.hist(p75, bins=101)
    pylab.xlim(minP, maxP)
    pylab.title('delay = 75')
    
    pylab.subplot(224)
    pylab.hist(p0, bins=101)
    pylab.xlim(minP, maxP)
    pylab.title('delay = 0')
    
    pylab.show()
