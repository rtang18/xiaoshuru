# For working with the data
import pandas as pd
# For the wordcloud
import numpy as np
import matplotlib.pyplot as plt
# To get rid of tone marks
import unidecode

# Read in data
syllables = pd.read_csv("syllable frequencies.csv")
characters = pd.read_csv("character ranking reduced.csv", encoding = "utf-8").dropna()

# Function to create simple dictionary from dataframe
def simple_dict(df):
    # Takes in df, returns first column as keys, second column as values
    # Initialize dictionary
    simple = dict()
    # Iterate through df
    for i in range(len(df)):
        simple[df.iloc[i, 0]] = df.iloc[i, 1]
    # Return dictionary
    return simple


# Create syllable dictionary from dataframe, to prep for spelling corrector
syll_dict = simple_dict(syllables)

# Use unidecode to get rid of tone marks, add a new column without tone marks
toneless = np.array([])
for p in characters["pinyin"]:              
    toneless = np.append(toneless, unidecode.unidecode(p))
characters["toneless"] = toneless
characters.head()

# Function to create character dictionary from dataframe
def character_dict(df):
    # Takes in df containing 4 columns: frequency_rank, character, pinyin, toneless
    # Returns dictionary with toneless pinyin as the keys, list of corr. characters as values
    # Initialize dictionary
    chars = dict()
    # Get unique list of toneless pinyin
    unique_pinyin = df["toneless"].unique()
    for u in unique_pinyin:
        # Get all rows that have toneless pinyin u
        u_rows = df.loc[df["toneless"] == u, :]
        # Save u characters into a list, only save the unique characters
        u_list = list(u_rows["character"].unique())
        # Set u as key, the list as value
        chars[u] = u_list
    # Return dictionary
    return chars

# Create the character dictionary!
char_dict = character_dict(characters)