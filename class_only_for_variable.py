class ForVariable:
    #for SAMPLE
    number_of_sample = 100  # bez znaczenia, ale musi byc wiekszy niz liczba zdjec
    width = 70  # in pixels
    height = 400  # in pixels

    #for TRAINING
    positive_sample = 20  # less than number of positive sample
    negative_sample = 1000  # whatever
    number_stages = 13  # number of stages training
    maxFalseAlarmRate = 0.4
    minHitRate = 0.99

