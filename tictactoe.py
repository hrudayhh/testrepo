theBoard={'top-L':' ','top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' '}

def printboard(board):
	print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
	print('-+-+-')
	print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
	print('-+-+-')
	print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
turn='X'
for i in range(10):
	print(printboard(theBoard))
	print(turn+' '+'want to place in')
	move=input()
	if move in theBoard.keys():
		theBoard[move]=turn
	else:
		continue
	if theBoard['top-L']!=' ':
		if theBoard['top-L']==theBoard['top-R']:
			if theBoard['top-L']==theBoard['top-M']:
				print('Winner is'+turn)
				break
	if theBoard['mid-L']!=' ':
                if theBoard['mid-L']==theBoard['mid-R']:
                        if theBoard['mid-L']==theBoard['mid-M']:
                                print('Winner is'+turn)
                                break
	if theBoard['low-L']!=' ':
                if theBoard['low-L']==theBoard['low-R']:
                        if theBoard['low-L']==theBoard['low-M']:
                                print('Winner is'+turn)
                                break
	if theBoard['top-L']!=' ':
                if theBoard['top-L']==theBoard['mid-L']:
                        if theBoard['top-L']==theBoard['low-L']:
                                print('Winner is'+turn)
                                break
	if theBoard['top-M']!=' ':
                if theBoard['top-M']==theBoard['mid-M']:
                        if theBoard['top-M']==theBoard['low-M']:
                                print('Winner is'+turn)
                                break
	if theBoard['top-R']!=' ':
                if theBoard['top-R']==theBoard['mid-R']:
                        if theBoard['top-R']==theBoard['low-R']:
                                print('Winner is'+turn)
                                break	
	if theBoard['top-L']!=' ':
                if theBoard['top-L']==theBoard['mid-M']:
                        if theBoard['top-L']==theBoard['low-R']:
                                print('Winner is'+turn)
                                break
	if theBoard['top-R']!=' ':
                if theBoard['top-R']==theBoard['mid-M']:
                        if theBoard['top-R']==theBoard['low-L']:
                                print('Winner is'+turn)
                                break


	if turn=='X':
		turn='O'
	else:
		turn='X'

			
print(printboard(theBoard))
