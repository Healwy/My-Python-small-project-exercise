#-*-coding:utf-8-*-#
#use python 3.7

import curses
from random import randrange,choice
from collections import defaultdict

letter_code =[ord(ch) for ch in "WASDRQwasdrq"]
action = ['Up','Left','Down','Right','Reset','Exit']
action_dict = dict(zip(letter_code, action*2))

def get_user_action(keyboard):
    char = 'N'
    while char not in action_dict:
        char = keyboard.getch()
    return action_dict[char]
def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::-1] for row in field]

class gamefield(object):

    def __init__(self,height = 4,width = 4, win = 2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset()

    def reset(self):
        if self.score >self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for y in range(self.height)]
        self.spawn()
        self.spawn()

    def move(self,direction):
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i!=0]
                new_row += [0 for i in range(len(row)-len(new_row))]

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += row[i]
                        pair =False
                    else:
                        if i+1 < len(row) and row[i] == row[i+1]
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) ==  len(row)
                return new_row
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: \
            [move_row_left(row) for row in field]
        moves['Right'] = lambda field:\
            invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: \
            transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field:\
            transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field )
    def is_gameover(self):
        return not any(self.move_ispossible(move) for move in actions)

    def draw(self,screen):
        help_string = "(W)Up (S)Down (A)Left (Right)"
        help_string2 = "     (R)reset (Q)Exit"
        gameover_string = "   Game Over"
        win_string = "   Your Win"
        def cast (string):
            screen.addstr(string + '\n')

        def draw_hor_separator():
            line  = '+' + ('+----------'*self.width + '+')[1:]
            separator = defaultdict(lambda:line)
            if not hasattr(draw_hor_separator, 'counter'):
                draw_hor_separator .counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1


