"""
Focus: Truthiness, modern formatting, and precision.
"""

def showcase_data_types():
    # 1. Strings & F-Strings (Modern formatting)
    name: str = "Developer"
    version: float = 3.12
    # Expression evaluation inside f-strings is a pro tip
    print(f"User: {name.upper()} | Python version: {version:.1f}")

    # 2. Booleans & Truthiness (Key interview concept)
    # In Python, empty containers and zero are 'Falsy'
    items = []
    if not items:
        print("Empty lists are Falsy - this is 'Pythonic' code.")

    # 3. Type Conversion with error safety
    raw_input = "100"
    try:
        converted = int(raw_input)
        print(f"Converted {type(raw_input)} to {type(converted)}")
    except ValueError as e:
        print(f"Always handle conversion errors: {e}")

if __name__ == "__main__":
    showcase_data_types()