# helper file to quickly generate the start of an article
from datetime import datetime
import re

metadata = {}

metadata['Title'] = input('Title > ')

# metadata['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M')

# metadata['Category'] = input('Category > ')

# metadata['Tags'] = input('Tags (comma sep. list) > ')

metadata['Author'] = 'Freddie Larkins'

metadata['Summary'] = input('Summary > ')

metadata['Slug'] = re.sub(
    r'[^0-9a-zA-Z]', '-', metadata['Title'].lower().strip()
)

# stripping out the hyphen if the article slug ends in one
if metadata['Slug'].endswith('-'):
    metadata['Slug'] = metadata['Slug'][:-1]

with open(f'content/pages/{metadata["Slug"]}.md', 'w') as f:
    for k, v in metadata.items():
        f.write(f'{k}: {v}\n')