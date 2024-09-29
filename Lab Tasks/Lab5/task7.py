import re

text = """
Here are some sample email addresses: layyana.junaid@example.com, alisha-zaidi123@domain.co.uk, 
invalid-email@domain, contact@company.net. You can also reach us at support@my-site.org or sales@business.com.
"""


email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern, text)

print("Extracted Email Addresses:")
for email in emails:
    print(email)
