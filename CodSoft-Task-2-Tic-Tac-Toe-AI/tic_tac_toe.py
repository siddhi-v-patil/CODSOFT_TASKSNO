"""
============================================================
                TIC-TAC-TOE AI
============================================================

CodSoft AI Internship - Task 2

Features:
1. Human vs AI
2. Easy / Medium / Hard difficulty
3. Minimax Algorithm
4. Alpha-Beta Pruning
5. AI vs AI Battle Simulation
6. Battle Statistics
7. Win Rate Analysis
8. Replay Option

Author: Siddhi Patil
============================================================
"""

import random
import time


# ============================================================
# CONSTANTS
# ============================================================

EMPTY = " "
HUMAN = "X"
AI = "O"

BOARD_SIZE = 9

WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


# ============================================================
# BOARD FUNCTIONS
# ============================================================

def create_board():
    """Create an empty Tic-Tac-Toe board."""
    return [EMPTY] * BOARD_SIZE


def print_board(board):
    """Display the Tic-Tac-Toe board."""

    print()
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print()


def print_position_board():
    """Display board positions for the player."""

    print()
    print("     |     |")
    print("  1  |  2  |  3")
    print("_____|_____|_____")
    print("     |     |")
    print("  4  |  5  |  6")
    print("_____|_____|_____")
    print("     |     |")
    print("  7  |  8  |  9")
    print("     |     |")
    print()


def available_moves(board):
    """Return all empty positions."""

    return [i for i in range(BOARD_SIZE) if board[i] == EMPTY]


def make_move(board, position, player):
    """Place a player's mark on the board."""

    if position in available_moves(board):
        board[position] = player
        return True

    return False


# ============================================================
# GAME STATE FUNCTIONS
# ============================================================

def check_winner(board):
    """
    Check the current game state.

    Returns:
        'X'    -> X wins
        'O'    -> O wins
        'Draw' -> board is full
        None   -> game continues
    """

    for a, b, c in WINNING_COMBINATIONS:

        if (
            board[a] != EMPTY
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            return board[a]

    if EMPTY not in board:
        return "Draw"

    return None


def game_over(board):
    """Return True if the game has ended."""

    return check_winner(board) is not None


# ============================================================
# HUMAN MOVE
# ============================================================

def get_human_move(board):
    """Get a valid move from the human player."""

    while True:

        try:
            move = int(input("Enter your move (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            position = move - 1

            if board[position] != EMPTY:
                print("That position is already occupied.")
                continue

            return position

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")


# ============================================================
# RANDOM AI
# ============================================================

def random_move(board):
    """Easy AI chooses a random available position."""

    moves = available_moves(board)

    if not moves:
        return None

    return random.choice(moves)


# ============================================================
# WINNING MOVE DETECTION
# ============================================================

def find_winning_move(board, player):
    """
    Find a move that allows the given player to win immediately.
    """

    for move in available_moves(board):

        board[move] = player

        if check_winner(board) == player:
            board[move] = EMPTY
            return move

        board[move] = EMPTY

    return None


# ============================================================
# MEDIUM AI
# ============================================================

def medium_move(board):
    """
    Medium AI strategy:

    1. Try to win
    2. Block opponent
    3. Take center
    4. Take a corner
    5. Take any remaining position
    """

    # Step 1: Try to win
    winning_move = find_winning_move(board, AI)

    if winning_move is not None:
        return winning_move

    # Step 2: Block human
    blocking_move = find_winning_move(board, HUMAN)

    if blocking_move is not None:
        return blocking_move

    # Step 3: Take center
    if board[4] == EMPTY:
        return 4

    # Step 4: Take corner
    corners = [0, 2, 6, 8]

    empty_corners = [
        move for move in corners
        if board[move] == EMPTY
    ]

    if empty_corners:
        return random.choice(empty_corners)

    # Step 5: Any available position
    return random_move(board)


# ============================================================
# MINIMAX ALGORITHM
# ============================================================

def minimax(board, depth, is_maximizing, alpha, beta):
    """
    Minimax algorithm with Alpha-Beta pruning.

    AI  -> maximizing player
    HUMAN -> minimizing player
    """

    result = check_winner(board)

    # Terminal states
    if result == AI:
        return 10 - depth

    if result == HUMAN:
        return depth - 10

    if result == "Draw":
        return 0

    # Maximizing player - AI
    if is_maximizing:

        best_score = float("-inf")

        for move in available_moves(board):

            board[move] = AI

            score = minimax(
                board,
                depth + 1,
                False,
                alpha,
                beta
            )

            board[move] = EMPTY

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best_score

    # Minimizing player - Human
    else:

        best_score = float("inf")

        for move in available_moves(board):

            board[move] = HUMAN

            score = minimax(
                board,
                depth + 1,
                True,
                alpha,
                beta
            )

            board[move] = EMPTY

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best_score


# ============================================================
# HARD AI
# ============================================================

def hard_move(board):
    """
    Hard AI uses Minimax with Alpha-Beta pruning.
    """

    best_score = float("-inf")
    best_move = None

    for move in available_moves(board):

        board[move] = AI

        score = minimax(
            board,
            0,
            False,
            float("-inf"),
            float("inf")
        )

        board[move] = EMPTY

        if score > best_score:

            best_score = score
            best_move = move

    return best_move


# ============================================================
# AI MOVE SELECTOR
# ============================================================

def get_ai_move(board, difficulty):
    """Select AI strategy based on difficulty."""

    if difficulty == "easy":
        return random_move(board)

    if difficulty == "medium":
        return medium_move(board)

    if difficulty == "hard":
        return hard_move(board)

    return hard_move(board)


# ============================================================
# HUMAN VS AI GAME
# ============================================================

def play_human_game(difficulty):
    """Run a Human vs AI game."""

    board = create_board()

    print()
    print("=" * 60)
    print("                 HUMAN vs AI")
    print("=" * 60)

    print(f"Difficulty: {difficulty.upper()}")

    print()
    print("You are X")
    print("AI is O")

    print_position_board()

    current_player = HUMAN

    while True:

        print_board(board)

        # Human turn
        if current_player == HUMAN:

            move = get_human_move(board)

            board[move] = HUMAN

        # AI turn
        else:

            print("AI is thinking...")

            start_time = time.time()

            move = get_ai_move(
                board,
                difficulty
            )

            thinking_time = time.time() - start_time

            board[move] = AI

            print(
                f"AI selected position {move + 1}"
            )

            print(
                f"Thinking time: {thinking_time:.4f} seconds"
            )

        # Check game result
        result = check_winner(board)

        if result is not None:

            print_board(board)

            print("=" * 60)

            if result == HUMAN:

                print("Congratulations! You won!")

            elif result == AI:

                print("AI wins! Better luck next time.")

            else:

                print("It's a draw!")

            print("=" * 60)

            return result

        # Switch player
        if current_player == HUMAN:
            current_player = AI

        else:
            current_player = HUMAN


# ============================================================
# AI VS AI GAME
# ============================================================

def play_ai_vs_ai_game(
    ai_x="medium",
    ai_o="hard",
    display=False
):
    """
    Run one AI vs AI game.

    X and O can use different AI strategies.
    """

    board = create_board()

    current_player = HUMAN

    move_number = 0

    while True:

        move_number += 1

        # Select current AI
        if current_player == HUMAN:

            difficulty = ai_x
            player = HUMAN

        else:

            difficulty = ai_o
            player = AI

        # Get move
        move = get_ai_move(
            board,
            difficulty
        )

        # Safety check
        if move is None:
            return "Draw"

        board[move] = player

        # Display game if requested
        if display:

            print()
            print(
                f"Move {move_number}: "
                f"{player} ({difficulty})"
            )

            print_board(board)

            time.sleep(0.3)

        # Check result
        result = check_winner(board)

        if result is not None:

            return result

        # Switch player
        if current_player == HUMAN:
            current_player = AI

        else:
            current_player = HUMAN


# ============================================================
# AI BATTLE
# ============================================================

def run_ai_battle():
    """
    Run multiple AI vs AI games and display statistics.
    """

    print()
    print("=" * 60)
    print("                  AI vs AI BATTLE")
    print("=" * 60)

    print()
    print("Select AI for Player X:")
    print("1. Random AI")
    print("2. Medium AI")
    print("3. Minimax + Alpha-Beta AI")

    while True:

        try:
            x_choice = int(input("Enter choice (1-3): "))

            if x_choice not in [1, 2, 3]:
                print("Please select 1, 2, or 3.")
                continue

            break

        except ValueError:
            print("Please enter a number.")

    print()
    print("Select AI for Player O:")
    print("1. Random AI")
    print("2. Medium AI")
    print("3. Minimax + Alpha-Beta AI")

    while True:

        try:
            o_choice = int(input("Enter choice (1-3): "))

            if o_choice not in [1, 2, 3]:
                print("Please select 1, 2, or 3.")
                continue

            break

        except ValueError:
            print("Please enter a number.")

    ai_names = {
        1: "Random AI",
        2: "Medium AI",
        3: "Minimax + Alpha-Beta AI"
    }

    ai_difficulties = {
        1: "easy",
        2: "medium",
        3: "hard"
    }

    ai_x_name = ai_names[x_choice]
    ai_o_name = ai_names[o_choice]

    ai_x = ai_difficulties[x_choice]
    ai_o = ai_difficulties[o_choice]

    print()
    print(f"Player X: {ai_x_name}")
    print(f"Player O: {ai_o_name}")

    # Number of games
    while True:

        try:
            games = int(
                input(
                    "\nHow many games should be simulated? "
                )
            )

            if games <= 0:
                print("Enter a number greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    print()
    print("=" * 60)
    print("Starting AI battle...")
    print("=" * 60)

    # IMPORTANT:
    # Use exactly the same result key returned
    # by check_winner().
    results = {
        "X": 0,
        "O": 0,
        "Draw": 0
    }

    start_time = time.time()

    # Run games
    for game_number in range(1, games + 1):

        result = play_ai_vs_ai_game(
            ai_x=ai_x,
            ai_o=ai_o,
            display=False
        )

        # Update statistics
        if result == "X":
            results["X"] += 1

        elif result == "O":
            results["O"] += 1

        elif result == "Draw":
            results["Draw"] += 1

        # Progress display
        if games <= 20:

            print(
                f"Game {game_number:>3}: "
                f"{result}"
            )

        elif game_number % max(1, games // 10) == 0:

            progress = (
                game_number / games
            ) * 100

            print(
                f"Progress: {progress:.0f}%"
            )

    total_time = time.time() - start_time

    # ========================================================
    # CALCULATE STATISTICS
    # ========================================================

    x_wins = results["X"]
    o_wins = results["O"]
    draws = results["Draw"]

    x_rate = (
        x_wins / games
    ) * 100

    o_rate = (
        o_wins / games
    ) * 100

    draw_rate = (
        draws / games
    ) * 100

    # ========================================================
    # DISPLAY RESULTS
    # ========================================================

    print()
    print("=" * 60)
    print("                  BATTLE RESULTS")
    print("=" * 60)

    print()
    print(f"Player X - {ai_x_name}")
    print(f"Wins                 : {x_wins}")
    print(f"Win Rate             : {x_rate:.2f}%")

    print()

    print(f"Player O - {ai_o_name}")
    print(f"Wins                 : {o_wins}")
    print(f"Win Rate             : {o_rate:.2f}%")

    print()

    print(f"Draws                : {draws}")
    print(f"Draw Rate            : {draw_rate:.2f}%")

    print()

    print(f"Total Games          : {games}")
    print(f"Total Simulation Time: {total_time:.4f} seconds")

    if games > 0:

        average_time = total_time / games

        print(
            f"Average Time/Game   : "
            f"{average_time:.6f} seconds"
        )

    print()
    print("-" * 60)

    # ========================================================
    # DETERMINE OVERALL WINNER
    # ========================================================

    if x_wins > o_wins:

        print(
            f"Winner: {ai_x_name}"
        )

    elif o_wins > x_wins:

        print(
            f"Winner: {ai_o_name}"
        )

    else:

        print("Overall Result: Tie")

    print("=" * 60)


# ============================================================
# DEMO GAME
# ============================================================

def run_demo():
    """
    Demonstrate Hard AI vs Medium AI.

    This is useful for showing the AI's behavior
    without requiring human input.
    """

    print()
    print("=" * 60)
    print("                  AI DEMONSTRATION")
    print("=" * 60)

    print()
    print("Player X: Medium AI")
    print("Player O: Minimax + Alpha-Beta AI")

    print()
    print("Starting demonstration...")

    result = play_ai_vs_ai_game(
        ai_x="medium",
        ai_o="hard",
        display=True
    )

    print()
    print("=" * 60)

    if result == "X":
        print("Medium AI wins!")

    elif result == "O":
        print("Minimax + Alpha-Beta AI wins!")

    else:
        print("The demonstration ended in a draw.")

    print("=" * 60)


# ============================================================
# MAIN MENU
# ============================================================

def main():
    """Main program menu."""

    while True:

        print()
        print("=" * 60)
        print("                 TIC-TAC-TOE AI")
        print("=" * 60)

        print()
        print("1. Human vs AI")
        print("2. AI vs AI Battle")
        print("3. AI Demonstration")
        print("4. Exit")

        print()

        try:
            choice = int(
                input("Enter your choice (1-4): ")
            )

        except ValueError:

            print(
                "Invalid input. "
                "Please enter a number from 1 to 4."
            )

            continue

        # ====================================================
        # HUMAN VS AI
        # ====================================================

        if choice == 1:

            print()
            print("Select difficulty:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")

            while True:

                try:
                    difficulty_choice = int(
                        input(
                            "Enter difficulty (1-3): "
                        )
                    )

                    if difficulty_choice == 1:
                        difficulty = "easy"
                        break

                    elif difficulty_choice == 2:
                        difficulty = "medium"
                        break

                    elif difficulty_choice == 3:
                        difficulty = "hard"
                        break

                    else:
                        print(
                            "Please choose 1, 2, or 3."
                        )

                except ValueError:

                    print(
                        "Please enter a valid number."
                    )

            play_human_game(difficulty)

        # ====================================================
        # AI VS AI
        # ====================================================

        elif choice == 2:

            run_ai_battle()

        # ====================================================
        # DEMO
        # ====================================================

        elif choice == 3:

            run_demo()

        # ====================================================
        # EXIT
        # ====================================================

        elif choice == 4:

            print()
            print(
                "Thanks for playing Tic-Tac-Toe AI!"
            )

            print(
                "This is task-2 of CodSoft internship!"
            )

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1, 2, 3, or 4."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()