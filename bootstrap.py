#Importing Libraries
from random import seed
from random import random
from random import randrange

#Create Random Subsample from A Dataset With Replacement
def subsample (dataset, ratio):
    sample=list()
    n_sample=round(len(dataset)*ratio)
    while len(sample) < n_sample:
        index=randrange(len(dataset))
        sample.append(dataset[index])
    return sample

#Calculate Mean
def mean(numbers):
    return sum(numbers)/float(len(numbers))

#Generate Same Random Number
seed(1)

#True Mean
dataset=list()
for i in range(20):
    randomnum=randrange(10)
    dataset.append(randomnum)
print (mean(dataset))

#Estimated Means
ratio=0.5
for size in [1,10,100]:
    sample_means=list()
    for i in range(size):
        sample=subsample(dataset,ratio)
        sample_mean=mean(sample)
        sample_means.append(sample_mean)
    print ('Sample Size: %d , Estimated Mean: %.3f' % (size, mean(sample_means)))