board_row1 = ['1','2','3']
board_row2 = ['4','5','6']
board_row3 = ['7','8','9']

def print_board():
	print board_row1
	print board_row2
	print board_row3

print '>>> Welcome!'
print 'First, what is your name?'
player_one = raw_input()
print 'Ok %s, you are Player 1' % (player_one)
print 'Next person, what is your name?'
player_two = raw_input()
print 'Great. %s you will be Player 2' % (player_two)
print 'Now %s do you want to be X or O?' % (player_one)
player_one_marker = raw_input()
print "Good choice %s" % (player_one)
print "And %s, that means you'll be...?" % (player_two)
player_two_marker = raw_input()
print 'Ok so there we have it. %s will be %s and %s will be %s' % (player_one, player_one_marker, player_two, player_two_marker)
print 'Ready to see the board?'
raw_input()
print 'ok here it is'
print
print_board()
print
print "I know I know. Let\'s just go with it alright"
print 'So each turn you will choose a position on the board, 1-9.\nThen, the computer will place an %s for %s and an %s for %s' % (player_one_marker, player_one, player_two_marker, player_two)
