import re

# Sample text containing prices and storage capacities
text = """
Ultimate Performance Laptop - Power Meets Affordability!

Experience lightning-fast performance with a 6 GHz processor, ensuring seamless multitasking and high-speed computing.
With 500 GB of storage, you'll have ample space for all your files, applications, and media.

Equipped with 1.5 GB of RAM, this laptop delivers smooth and efficient performance for everyday tasks.

All of this comes at an unbeatable price of $899.
"""

# Regex to find both storage (GB) and price ($)
pattern = r'\b([0-9]+(?:\.[0-9]+)?) *(GB|[Gg]igabytes?)\b|(?:^|\W)\$([0-9]+(?:\.[0-9]{2})?)\b'

# Find all matches
matches = re.findall(pattern, text)

# Print the results
print("Matches found:")
for match in matches:
    if match[0]:  # Storage (GB)
        print(f"Storage: {match[0]}{match[1]}")
    elif match[2]:  # Price ($)
        print(f"Price: ${match[2]}")