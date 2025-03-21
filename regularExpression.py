import re


text = "Emails: user@test.com, admin@site.org"
emails = re.findall(r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b', text)
print(emails)


date = "2023-12-31"
is_valid = bool(re.match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', date))
print(is_valid)


text = "Replace cat with dog. Catapult."
new_text = re.sub(r'\bcat\b', 'dog', text, flags=re.IGNORECASE)
print(new_text)


text = "Hello! How are you?"
parts = re.split(r'[^a-zA-Z0-9]', text)
parts = [p for p in parts if p]
print(parts) 