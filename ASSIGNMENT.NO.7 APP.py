# Experiment No. 7
# Regular Expressions - Email Pattern Matching

import re

# Regular expression for finding email addresses
email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

# Accept text from the user
text = input("Enter a text containing email addresses: ")

# Find all email addresses
emails = re.findall(email_pattern, text)

# Display the result
print("\n===== Email Addresses Found =====")

if emails:
    for email in emails:
        print(email)

    print("\nTotal Email Addresses:", len(emails))
else:
    print("No valid email addresses found.")