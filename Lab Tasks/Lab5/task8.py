import re
text = """
Here are some dates: 12/09/2023, 2023-09-12, Sep 12, 2023, 09-12-2023, and some invalid dates like 2023-15-45.
We also have: December 5, 2021 and Mar 3, 1999.
"""

date_patterns = [
    r'\b\d{2}/\d{2}/\d{4}\b',
    r'\b\d{4}-\d{2}-\d{2}\b',
    r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{4}\b',
    r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}\b'  # Matches full month names like December 5, 2021
]

combined_pattern = "|".join(date_patterns)

dates = re.findall(combined_pattern, text)

print("Extracted Dates:")
for date in dates:
    print(date)
