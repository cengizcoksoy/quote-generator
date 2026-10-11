import random

quotes = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Success is not final, failure is not fatal.", "Winston Churchill"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("Your time is limited, so don't waste it living someone else's life.", "Steve Jobs")
]


def generate_quote():
    quote, author = random.choice(quotes)

    print("\n=== RANDOM INSPIRATIONAL QUOTE ===")
    print(f'\n"{quote}"')
    print(f"— {author}")
    print("\n================================")


if __name__ == "__main__":
    generate_quote()