with open('emails.txt', 'r') as emails:  # looking for particular info in stack 
    emails = emails.readlines()

for email in emails:
    print("Looking for a hotmails account")
    if "hotmail" in email:
        print(email)  