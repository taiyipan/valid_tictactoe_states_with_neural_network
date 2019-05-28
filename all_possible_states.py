'''
This class generates all possible tictactoe state permutations
in a 3x3 board
'''
class all_possible_states:
    def states(self):
        from random import randint

        options = [-1, 0, 1]

        count = 0
        max_count = 19683

        states = list()
        while count < max_count:
            new_state = list()
            for position in range(9):
                n = randint(0, 2)
                new_state.append(options[n])
            unique = True
            for state in states:
                if state == new_state:
                    unique = False
                    break
            if (unique):
                states.append(new_state)
                count += 1
                print('Count: {}'.format(count))

        fname = 'states.txt'
        outfile = open(fname, 'w')
        for state in states:
            for n in state:
                outfile.write(str(n) + ' ')
            outfile.write('\n')
        outfile.close()

all_states = all_possible_states()
all_states.states()
