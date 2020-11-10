import random
import matplotlib.pyplot as plt
from collections import defaultdict

def sample(numbers, count):
    result = numbers[:count]
    for i in range(count, len(numbers)):
        pos = random.randint(0, i)
        if pos < count:
            result[pos] = numbers[i]
    return result

def sampleMean(numbers, count):
    s = sample(numbers, count)
    return sum(map(float, s)) / count

def sampleMeanError(numbers, count):
    return sampleMean(numbers, count) - sum(map(float, numbers)) / len(numbers)

def plotSampleErrors(numbers, count, runs):
    errors = []
    for i in range(runs):
        errors.append(sampleMeanError(numbers, count))

    minError = min(errors)
    maxError = max(errors)

    foldsCount = 1000
    foldsMap = defaultdict(int)

    for e in errors:
        fold = int((e - minError) / (maxError - minError) * foldsCount)
        foldsMap[fold] += 1

    x = []
    y = []
    labels = []
    for i in range(foldsCount):
        value = minError + float(i) / foldsCount * (maxError - minError)
        x.append(value)
        y.append(foldsMap[i])
        labels.append(minError + float(i) / foldsCount * (maxError - minError))

    fig = plt.figure()
    fig.set_size_inches(10, 5)
    plt.plot(x, y)
    plt.show()
        
numbers = []
for i in range(1000):
    numbers.append(random.randint(0, 10))

plotSampleErrors(numbers, 100, 1000)

