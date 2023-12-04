
def find_winning_nums_have(winning_nums: list, nums_have: list):
    # Intersect lists to find our winners
    winning_nums_have = [num for num in winning_nums if num in nums_have]
    return winning_nums_have

def calc_card_score(winning_nums_have: list):
    score = 0
    for num in winning_nums_have:
        if score == 0:
            # 1 point for first win
            score = 1
        else:
            # double points for each subsequent win
            score *= 2    
    return score

def update_copies_won(card_id: int, copies_won: dict, winning_nums_have: list, card_count: int):
    # initialise or increment for original card
    if card_id not in copies_won:
        copies_won[card_id] = 1
    else:
        copies_won[card_id] += 1
    
    if len(winning_nums_have) == 0:
        return copies_won

    # initialise or increment for copies of following cards
    for i in range(1, min(len(winning_nums_have), card_count)+1):
        if (card_id+i not in copies_won):
            copies_won[card_id+i] = 0

        copies_won[card_id+i] += copies_won[card_id]

    return copies_won
    
def sum_copies_won(copies_won: dict):
    total_copies_won = 0
    for k, v in copies_won.items():
        total_copies_won += v

    return total_copies_won

test_cards = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

with open("day4\input.txt") as f:
    cards = f.readlines()

    total_score = 0
    copies_won = {}
    total_copies_won = 0
    total_multiplied_score = 0

    for card in cards:
        # parse input
        card_details = card.strip().split(":")
        card_id = int(card_details[0].split()[1])
        card_body = card_details[1].split("|")
        card_winning_nums = card_body[0].strip().split()
        card_nums_have = card_body[1].strip().split()

        winning_nums_have = find_winning_nums_have(card_winning_nums, card_nums_have)
        copies_won = update_copies_won(card_id, copies_won, winning_nums_have, len(cards))

        score = calc_card_score(winning_nums_have)

        multiplied_score = score * copies_won[card_id]

        print(f"Card {card_id} has a score of {score} and has won {copies_won[card_id]} copies. Multiplied score: {multiplied_score}")

        total_score += score
        total_multiplied_score += multiplied_score
    
    total_copies_won = sum_copies_won(copies_won)

    print(f"Total score: {total_score}")
    print(f"Total multiplied score: {total_multiplied_score}")
    print(f"Copies won: {total_copies_won}")

