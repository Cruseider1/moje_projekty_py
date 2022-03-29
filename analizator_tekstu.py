from textblob import TextBlob

# poniżej wrzucamy konkretny tekst do analizy - słowa - rzeczowniki/ przymiotniki pozytywne dadzą wyniki na plusie a negatywne na minusie

text = '''
I was very gratefull for my life
'''

blob = TextBlob(text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', unlike, ...])

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)

#----------------------------------------
blob = TextBlob("Buongiorno!") # ta część kodu pozwala na tłumaczenie tekstu 
print(blob.translate(to='pl'))