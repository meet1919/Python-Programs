class Display:
    def __init__(self):
        self.Solved_Tower = {0: '|'.rjust(6), 1: '●1●'.rjust(7), 2: '●●2●●'.rjust(8), 3: '●●●3●●●'.rjust(9), 4: '●●●●4●●●●'.rjust(10), 5: '●●●●●5●●●●●'}
        self.Empty_Tower = {0: '|'.rjust(18), 1: '|'.rjust(17), 2: '|'.rjust(16), 3: '|'.rjust(15), 4: '|'.rjust(14), 5: '|'.rjust(13)}
        self.Empty_Tower1 = {0: '|'.rjust(18), 1: '|'.rjust(18), 2: '|'.rjust(18), 3: '|'.rjust(18), 4: '|'.rjust(18), 5: '|'.rjust(18)}

    def HanoiTower(self):
        print('\nTower of Hanoi\n\n'
              'Move the tower of disks, one disk at a time, to another tower.\n'
              'Larger disks cannot rest on top of a smaller disk.\n')

        #display_solved = '''%s\n%s\n%s\n%s\n%s\n%s
        #''' % (solved_tower[0].rjust(6), solved_tower[1].rjust(7), solved_tower[2].rjust(8), solved_tower[3].rjust(9), solved_tower[4].rjust(10), solved_tower[5])
        #display_empty = '''%s\n%s\n%s\n%s\n%s\n%s
        #''' % (empty_tower[0].rjust(6), empty_tower[1].rjust(6), empty_tower[2].rjust(6), empty_tower[3].rjust(6), empty_tower[4].rjust(6), empty_tower[5].rjust(6))

        for i in range(6):
            print(self.Solved_Tower[i] + self.Empty_Tower[i] + self.Empty_Tower1[i])

        print()
        print('A'.rjust(6) + 'B'.rjust(18) + 'C'.rjust(18))
        print('\nEnter the letters of "from" and "to" towers, or QUIT.\n'
              '(e.g., AB to moves a disk from tower A to tower B.)')

    def GamePlay(self, tower):
        self.move = input('Enter your MOVE: ')
        for i in range(100):
            if self.move == 'AB':
                if self.Solved_Tower.values() != '|':
                    self.Empty_Tower[5] = self.Solved_Tower[1]
                    self.Solved_Tower[1] = self.Solved_Tower[0]
            for i in range(6):
                print(self.Solved_Tower[i] + self.Empty_Tower[i] + self.Empty_Tower1[i])
            self.move = input('Enter your MOVE: ')

