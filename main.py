import game_data
import random
import art


def add_points(score):
    score += 1
    return score


def check_answer(bigger_result, player_answer):
    if bigger_result == player_answer:
        return True
    else:
        return False


def correct_answer(random_data, player_score):
    del random_data[1]
    random_data.append(random.choice(game_data.data))
    print(f"You're right! Current score: {player_score}")


print(art.logo)
random_data = random.choices(game_data.data, k=2)
player_score = 0
is_correct = True
while is_correct:
    compare_a = random_data[0]["follower_count"]
    compare_b = random_data[1]["follower_count"]
    print(f"Compare A: {random_data[0]['name']}, {random_data[0]['description']}, from {random_data[0]['country']}")
    print(art.vs)
    print(f"Compare B: {random_data[1]['name']}, {random_data[1]['description']}, from {random_data[1]['country']}")
    player_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if compare_a > compare_b:
        bigger_result = compare_a
    else:
        bigger_result = compare_b

    if player_answer == "a":
        player_answer = compare_a
        is_correct = check_answer(bigger_result, player_answer)
        if is_correct:
            player_score = add_points(player_score)
            correct_answer(random_data, player_score)
        else:
            print(f"Sorry, that's wrong. Final score: {player_score}")
    elif player_answer == "b":
        player_answer = compare_b
        is_correct = check_answer(bigger_result, player_answer)
        if is_correct:
            random_data[0] = random_data[1]
            player_score = add_points(player_score)
            correct_answer(random_data, player_score)
        else:
            print(f"Sorry, that's wrong. Final score: {player_score}")
