def coin_toss():
    head_count = 0
    tail_count = 0
    import random
    for x in range(5000):
        random_num = round(random.random())
        if random_num == 1:
            head_count += 1
            print 'Throwing a coin...its a Head!... got {} head(s) so far'.format(head_count)
        else:
            tail_count += 1
            print 'Throwing a coin...its a Tail!... got {} tails(s) so far'.format(tail_count)

coin_toss()

