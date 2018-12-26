from dictionarycreation.py import syll_dict, char_dict

def P(syllable, N=sum(syll_dict.values())): 
    "Probability of `syllable`."
    return syll_dict[syllable] / N

def correction(syllable): 
    "Most probable spelling correction for syllable."
    return max(candidates(syllable), key=P)

def candidates(syllable): 
    "Generate possible spelling corrections for syllable."
    return (known([syllable]) or known(edits1(syllable)) or known(edits2(syllable)) or [syllable])

def known(syllables): 
    "The subset of `syllables` that appear in syll_dict."
    return set(s for s in syllables if s in syll_dict)

def edits1(syllable):
    "All edits that are one edit away from `syllable`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(syllable[:i], syllable[i:])    for i in range(len(syllable) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(syllable): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(syllable) for e2 in edits1(e1))