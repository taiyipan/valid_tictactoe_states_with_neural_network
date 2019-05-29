class data_manip:
    def load_states(self, fname = 'states.txt'):
        states = list()
        infile = open(fname, 'r')

        # read each line and add to states as a state
        for line in infile:
            state = list()
            line.strip()
            vals = line.split()
            for val in vals:
                state.append(int(val))
            states.append(state)

        infile.close()
        return states

    def create_labels(self, states):
        from valid_states_fc import valid_states_fc

        labels = list()
        # for each state, generate a label based on valid_states_fc
        for state in states:
            valid = valid_states_fc.valid(state)

            if valid:
                label = 1
            else:
                label = 0
            labels.append(label)

        fname = 'labels.txt'
        outfile = open(fname, 'w')

        for label in labels:
            outfile.write(str(label) + '\n')

        outfile.close()

    def load_labels(self, fname = 'labels.txt'):
        labels = list()
        infile = open(fname, 'r')

        for line in infile:
            line.strip()
            labels.append(int(line))

        infile.close()
        return labels


manip = data_manip()
states = manip.load_states()
manip.create_labels(states)
labels = manip.load_labels()
