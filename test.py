from better_dataclass import StrictList
import re

class EmailList(StrictList):
    
    def restriction(self, value):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(email_regex, str(value)))

# Create an instance of the EmailList
emails = EmailList()

# Add email values
emails.append('john@example.com')
emails.append('jane@example.com')
emails.append('invalid_email')

# Print the list
print(emails)
