test = [1,2,2,5,7,2,1]

while test:
    target = min(test)
    counter = 0
    while target in test:
        for i in test:
            if i == target:
                counter += 1
                test.remove(target)
    
    print(str(target) + ":" + str(counter))
