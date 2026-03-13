#FIX: Refactored logic into logic_utils.py using Claude Agent mode
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

#FIX: Refactored logic into logic_utils.py using Claude Agent mode
#FIX: Added low/high params to reject decimals, negatives, and out-of-range values
def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        # FIX: makes sure decimals aren't included 
        if "." in raw:
            return False, None, "Decimals are not allowed. Enter a whole number."
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # FIX: determines if value is out of range
    if value < low or value > high:
        return False, None, f"Out of range! Enter a number between {low} and {high}."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using Claude Agent mode
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    # FIX: the values were reversed, now if our number is too high, we get go lower and vice versa
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

#FIX: Refactored logic into logic_utils.py using Claude Agent mode
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
