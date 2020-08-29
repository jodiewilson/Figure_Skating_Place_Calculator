# GOLD, SILVER, AND BRONZE MEDALISTS
from statistics import median
print()
# INPUT SCORES FROM TXT FILE
scores = open ('input.txt')
# SAVE AS CONTENT
contents = scores.readlines()
# CONVERT TXT FILE TO FLOAT
player1_shortscore = float(contents[0])
#
player1_freescore = float(contents[1])
#
player2_shortscore = float(contents[2])
#
player2_freescore = float(contents[3])
#
player3_shortscore = float(contents[4])
#
player3_freescore = float(contents[5])
# GET SUM OF EACH PLAYERS SCORE
score_list = (player1_freescore + player1_shortscore), (player2_freescore + player2_shortscore), (player3_freescore + player3_shortscore)
# OUTPUT MEDALIST IN RANK ORDER
f = open('output.txt', 'w')
f.write('Gold: {}\n'.format(max(score_list)))
f.write('Silver: {}\n'.format(median(score_list)))
f.write('Bronze: {}\n'.format(min(score_list)))
f.close()



