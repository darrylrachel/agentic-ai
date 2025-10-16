# You're building a simple app that registers users.
# You want to separate concerns: getting input, validating it, and saving it
# Task:
#   * Write register_user() that calls
#   * get_input()
#   * validate_input()
#   * save_to_db()


def get_input():
    print(f"Gathering user data")

def validate_input():
    print(f"Validating user data")

def save_to_db():
    print(f"Saving user data to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()

register_user()