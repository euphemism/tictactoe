import math

def eratosthenes():
	'''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
	D = {}  # map composite integers to primes witnessing their compositeness
	q = 2   # first integer to test for primality
	while 1:
		if q not in D:
			yield q        # not marked composite, must be prime
			D[q*q] = [q]   # first multiple of q not already marked
		else:
			for p in D[q]: # move each witness to its next multiple
				D.setdefault(p+q,[]).append(p)
			del D[q]       # no longer need D[q], free memory
		q += 1

"""Board representation code"""
def generate_empty_output_row(board_size):
    FILL_CHARACTER = ' '
    SEPERATOR_CHARACTER = ' '
    return ''.join([' ' + SEPERATOR_CHARACTER if (i + 1) % (board_size + 1) == 0 else ' ' + FILL_CHARACTER \
                    for i in range(board_size - 1 + (board_size * board_size))])

def generate_output_row_seperator(board_size):
    SEPERATOR_CHARACTER = ' '
    return SEPERATOR_CHARACTER * (board_size * 2 * board_size + ((board_size - 1) * 2))

def generate_board_representation(cell_occupants):
    board_size = len(cell_occupants[0])
    half_rounded_up = math.ceil(board_size / 2)
    board = []
    empty_row = generate_empty_output_row(board_size)
    row_seperator = generate_output_row_seperator(board_size)
    for row in cell_occupants:
        board.extend([empty_row] * board_size)
        board[-half_rounded_up] = list(board[-half_rounded_up])
        for i, occupant in enumerate(row):
            if not occupant is None:
                board[-half_rounded_up][(half_rounded_up * 2 - 1) + (i * ((board_size + 1) * 2))] = occupant
        board[-half_rounded_up] = ''.join(board[-half_rounded_up])
        board.append(row_seperator)
    return '\n'.join(board[:-1])

if __name__ == '__main__':
    board_size = None
    minimum_board_size = 2
    maximum_board_size = 10
    while not board_size:
        try:
            board_size = int(input('Please input board size, a valid integer in ' + \
                                   'the range [{min}, {max}).'.format( \
                                       min=minimum_board_size, \
                                       max=maximum_board_size + 1)))
        except:
            print('Input a valid integer.')
        else:
            if not minimum_board_size <= board_size <= maximum_board_size:
                print('Input out of range [{min}, {max}).'.format( \
                    min=minimum_board_size, max=maximum_board_size + 1))
                board_size = None
    primes = eratosthenes()
    cell_primes = [next(primes) for i in range(board_size ** 2)]
