class valid_states_fc:
'''
This function determines whether a tictactoe state is valid or not
'''
    def valid(self, state):
        x = 1
        s = 0
        o = -1
        valid = True
        # check for numbers of x and o
        x_count = 0
        o_count = 0
        if len(state) != 9:
            valid = False
        for n in state:
            if n == x:
                x_count += 1
            elif n == o:
                o_count += 1
            elif n != x and n != o and n != s:
                valid = False
        # validate based on counts
        if o_count > x_count:
            valid = False
        elif x_count > o_count + 1:
            valid = False
        # check for win conditions
        xwin = False
        owin = False
        # horizontals
        if state[0] == state[1] and state[1] == state[2]:
            if state[0] == x:
                xwin = True
            elif state[0] == o:
                owin = True
        if state[3] == state[4] and state[4] == state[5]:
            if state[3] == x:
                xwin = True
            elif state[3] == o:
                owin = True
        if state[6] == state[7] and state[7] == state[8]:
            if state[6] == x:
                xwin = True
            elif state[6] == o:
                owin = True
        # verticals
        if state[0] == state[3] and state[3] == state[6]:
            if state[0] == x:
                xwin = True
            elif state[0] == o:
                owin = True
        if state[1] == state[4] and state[4] == state[7]:
            if state[1] == x:
                xwin = True
            elif state[1] == o:
                owin = True
        if state[2] == state[5] and state[5] == state[8]:
            if state[2] == x:
                xwin = True
            elif state[2] == o:
                owin = True
        # diagonals
        if state[0] == state[4] and state[4] == state[8]:
            if state[0] == x:
                xwin = True
            elif state[0] == o:
                owin = True
        if state[2] == state[4] and state[4] == state[6]:
            if state[2] == x:
                xwin = True
            elif state[2] == o:
                owin = True
        # validate on win conditions
        if xwin and owin:
            valid = False
        elif xwin and x_count == o_count:
            valid = False
        elif owin and x_count < o_count:
            valid = False
        elif owin and x_count > o_count:
            valid = False
        # result valid state flag
        return valid

valid_state = valid_states_fc()
state = [1, -1, 1, -1, -1, 1, 1, -1, 0]
print(valid_state.valid(state))
































#
