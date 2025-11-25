# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        # Split by commas or spaces
        candidates = re.split(r'[\s,]+', self.emails.strip())
        # Filter only valid email addresses
        emails = [email for email in candidates if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)]
        # Remove duplicates and sort
        return sorted(set(emails))
