def grader():
    import random
    for x in range(20):
        score = random.randint(60,100)
        if score < 70:
            print "Score: {}; Grade - D".format(score)
        elif score >= 70 and score < 80:
            print "Score: {}; Grade - C".format(score)
        elif score >= 80 and score < 90:
            print "Score: {}; Grade - B".format(score)
        else:
            print "Score: {}; Grade - A".format(score)

grader()
