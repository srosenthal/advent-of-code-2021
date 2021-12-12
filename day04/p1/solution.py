# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

# First line is the order
order = [int(n) for n in lines[0].split(',')]

# Load the boards, which are each 5x5
def parse_board(lines):
    board = []
    for line in lines:
        board.append([int(n) for n in line.split()])
    return board

lines = [line for line in lines[1:] if line != '']
num_boards = int(len(lines) / 5)
boards = []
for i in range(num_boards):
    boards.append(parse_board(lines[i*5:(i+1)*5]))

def is_winner(board, called_numbers):
    for row in board:
        # check row
        if all([c in called_numbers for c in row]):
            return True
    for i in range(5):
        # check col
        col = [row[i] for row in board]
        if all([c in called_numbers for c in col]):
            return True
    return False

def score_board(board, called_numbers):
    uncalled_sum = 0
    for row in board:
        for num in row:
            if not num in called_numbers:
                uncalled_sum += num
    return uncalled_sum

def simulate_game(order, boards):
    called_numbers = set()
    for num in order:
        print('calling number: ', num)
        called_numbers.add(num)
        for board in boards:
            if is_winner(board, called_numbers):
                board_score = score_board(board, called_numbers)
                score = board_score * num
                print("found a winner, board_score: {}, score: {}, board: {}".format(board_score, score, board))
                return score

simulate_game(order, boards)
