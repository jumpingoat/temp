def palindrom(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

print(palindrom("kajak"))  # True
print(palindrom("potop"))  # True
print(palindrom("Python"))  # False
