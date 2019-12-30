from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()
from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()
word = "multiplying" 
lem.lemmatize(word, "v")
>> "multiply" 
stem.stem(word)
>> "multipli"

