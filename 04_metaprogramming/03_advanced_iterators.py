class Countdown:
    """Custom iterator that counts down to zero."""
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

if __name__ == "__main__":
    for i in Countdown(3):
        print(i) # Output: 3, 2, 1