def create_chain():
    import numpy as np
    series = []
    ones = []
    twos = []
    while True:
        tmp = input('Choose type: (0 or 1)')
        if (not tmp.isnumeric()):
            print('\nOnly integers are accepted\n')
            continue
        else:
            tmp = int(tmp)
        
        if tmp == 0:
            
            ones.append(tmp)
            if len(ones) == 45:
                print('\nYou have 5 zeros left\n')
            elif len(ones) == 50:
                print('\nYou have no zeros left\n')
            elif len(ones) > 50:
                raise ValueError('You cannot have more than 50 zeros')
        
        elif tmp == 1:
            
            twos.append(tmp)
            if len(twos) == 45:
                print('\nYou have 5 ones left\n')
            elif len(twos) == 50:
                print('\nYou have no ones left\n')
            elif len(twos) > 50:
                raise ValueError('You cannot have more than 50 ones')
            
        else:
            print('\nInput value can only be 0 or 1\n')
            continue
        
        series.append(tmp)
        if len(series)%10 == 0:
            print(f'{100-len(series)} beads left')
        if len(series) == 100:
            print('\nYou have successfully created your chain\n')
            break
        
    series = np.array(series)
    series += 1
    chain = [str(elem) for elem in series]
    with open('start.data', 'r+') as f:
            lines = f.readlines()

    changes = []
    for elem in lines[17:117]:
        changes.append(elem.split())

    for i in range(len(changes)):
        changes[i][2] = chain[i]
        changes[i] = ' '.join(changes[i])

    with open('start_new.data','w') as f:
        for elem in lines[:17]:
            f.write(elem)
        for elem in changes:
            f.write(elem + '\n')
        for elem in lines[117:]:
            f.write(elem)

    print('You have successfully created your chain')
