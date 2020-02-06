# Do some cleaning to get the data in good order for analysis

import pandas as pd

df = pd.read_csv("AITA_posts.csv")

# Make verdicts all lower case
df['verdict'] = df['verdict'].str.lower()
# Replace some common alternate spellings
df['verdict'] = df['verdict'].str.replace("a--hole|a-hole","asshole")

# Write to file
df.to_csv("AITA_cleaned.csv")