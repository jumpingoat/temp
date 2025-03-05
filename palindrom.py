def palindrom(text):
    text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return text == text[::-1]

print(palindrom("kajak"))
print(palindrom("potop")) 
print(palindrom("Python")) 
print(palindrom("Ala ma kota")) 
print(palindrom("A to kanapa pana Kota")) 
print(palindrom("Madam, I'm Adam"))  
