import re
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

"""
clean_stem_lemmatize_tokens_column: full clean up for a column

arguments:
    dataframe:                pandas dataframe
    column:                   string
    more_stop_words:          string[]
    drop_unnecessary_columns: bool
"""
def clean_stem_lemmatize_tokens_column(dataframe, column, more_stop_words = [], drop_unnecessary_columns = False):
    clean_column(dataframe, column, more_stop_words)
    stem_column(dataframe, f"{column}_clean")
    lemmatize_column(dataframe, f"{column}_clean_stems")
    tokenize_column(dataframe, f"{column}_clean_stems_lemmas")
    if drop_unnecessary_columns is True:
        dataframe = dataframe.drop([f"{column}_clean", f"{column}_clean_stems"], axis=1)
    return dataframe

"""
clean_tokens_stem_lemmatize_column: full clean up for a column

arguments:
    dataframe:                pandas dataframe
    column:                   string
    more_stop_words:          string[]
    drop_unnecessary_columns: bool
"""
def clean_tokens_stem_lemmatize_column(dataframe, column, more_stop_words = [], drop_unnecessary_columns = False):
    clean_column(dataframe, column, more_stop_words)
    tokenize_column(dataframe, f"{column}_clean")
    stem_column_tokens(dataframe, f"{column}_clean_tokens")
    lemmatize_column_tokens(dataframe, f"{column}_clean_tokens_stems")
    tokens_to_sentence_column(dataframe, f"{column}_clean_tokens_stems_lemmas")
    if drop_unnecessary_columns is True:
        dataframe = dataframe.drop([f"{column}_clean", f"{column}_clean_tokens", f"{column}_clean_tokens_stems"], axis=1)
    return dataframe

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Tokenization

Tokenization is the process of demarcating and possibly classifying sections 
of a string of input characters. The resulting tokens are then passed on to 
some other form of processing. The process can be considered a sub-task of 
parsing input.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
tokenize_sentence: tokenizes a given sentence

arguments:
    sentence: string
"""
def tokenize_sentence(sentence):
    words = word_tokenize(sentence)
    return words

"""
tokenize_column: tokenizes a column of a dataframe and saves it as column_tokens

arguments:
    dataframe: pandas dataframe
    column:    string
"""
def tokenize_column(dataframe, column):
    tokens = list()
    # tokenize each element of the column
    for index, row in dataframe.iterrows():
        sentence_tokens = tokenize_sentence(dataframe.loc[index,column])
        tokens.append(sentence_tokens)
    # save tokens as a new column
    dataframe[f"{column}_tokens"] = pd.Series(tokens, index=dataframe.index)

"""
tokens_to_sentences: converts a list of tokens to a sentence

arguments:
    tokens: string[]
"""
def tokens_to_sentence(tokens):
    sentence = " ".join(tokens)
    return sentence

"""
tokens_to_sentence_column: converts a column of tokens to sentences and saves it as column_sentences

arguments:
    dataframe: pandas dataframe
    column:    string
"""
def tokens_to_sentence_column(dataframe, column):
    for index, row in dataframe.iterrows():
        dataframe.loc[index,f"{column}_sentences"] = tokens_to_sentence(dataframe.loc[index,column])

"""
clean_sentence: cleans a given sentence

arguments:
    sentence: string
"""
def clean_sentence(sentence):
    sentence = re.sub("[^a-zA-z\s]", "", sentence) # remove special characters
    sentence = re.sub("_", "", sentence)
    sentence = re.sub("\s+", " ",sentence)         # change any white space to one space
    sentence = sentence.strip()                    # remove start and end white spaces
    sentence = sentence.lower()                    # convert sentence into lower case
    return sentence

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Stop words

Stop words are the most common words in a language like "the", "is", "a". 
These words do not carry important meaning and are usually removed from texts.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
remove_stop_words_from_sentence: removes stop words fast using dictionary

arguments:
    sentence:        string[]
    more_stop_words: string
"""
def remove_stop_words_from_sentence(sentence, more_stop_words = []):
    stop_words = stopwords.words("english") + more_stop_words
    stopwords_dictionary = Counter(stop_words)
    sentence = " ".join([word for word in sentence.split() if word not in stopwords_dictionary])
    return sentence

"""
clean_column: cleans a dataframe column from symbols, removes stop words and saves it as column_clean

arguments:
    dataframe:       pandas dataframe
    column:          string
    more_stop_words: string[]
"""
def clean_column(dataframe, column, more_stop_words = []):
    # clean and remove each element of the column
    for index, row in dataframe.iterrows():
        dataframe.loc[index,f"{column}_clean"] = clean_sentence(dataframe.loc[index,column])
        dataframe.loc[index,f"{column}_clean"] = remove_stop_words_from_sentence(dataframe.loc[index,f"{column}_clean"], more_stop_words)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Stemming

Stemming is the process of reducing inflected (or sometimes derived) words 
to their word stem, base or root form—generally a written word form.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
"""
stem_sentence: stems a given sentence

arguments:
    sentence: string
"""
def stem_sentence(sentence):
    porter = PorterStemmer()
    words = word_tokenize(sentence)
    stems_tokens = list()
    for word in words:
        stems_tokens.append(porter.stem(word))
    return tokens_to_sentence(stems_tokens)

"""
stem_column: stems a column of a dataframe and saves it as column_stems

arguments:
    dataframe: pandas dataframe
    column:    string
"""
def stem_column(dataframe, column):
    for index, row in dataframe.iterrows():
        dataframe.loc[index,f"{column}_stems"] = stem_sentence(dataframe.loc[index,column])

"""
stem_column_tokens: stems a column of tokens of a dataframe and saves it as column_stems

arguments:
    dataframe: pandas dataframe
    column:    string
"""
def stem_column_tokens(dataframe, column):
    porter = PorterStemmer()
    stem_tokens = list()
    for index, row in dataframe.iterrows():
        stem = list()
        for token in dataframe.loc[index,column]:
            stem.append(porter.stem(token))
        stem_tokens.append(stem)
    # save stemmed tokens as a new column
    dataframe[f"{column}_stems"] = pd.Series(stem_tokens, index=dataframe.index)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Lemmatization

Lemmatisation (or lemmatization) in linguistics is the process of grouping together the 
inflected forms of a word so they can be analysed as a single item, identified by the 
word's lemma, or dictionary form.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
lemmatize_sentence: lemattizes a given sentence

arguments:
    sentence: string
"""
def lemmatize_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(sentence)
    lemmas_tokens = list()
    for word in words:
        lemmas_tokens.append(lemmatizer.lemmatize(word))
    return tokens_to_sentence(lemmas_tokens)

"""
lemmatize_sentence: lemattizes a column of a dataframe and saves it as column_lemmas

arguments:
    dataframe: pandas dataframe
    column:    string
"""
def lemmatize_column(dataframe, column):
    for index, row in dataframe.iterrows():
        dataframe.loc[index,f"{column}_lemmas"] = lemmatize_sentence(dataframe.loc[index,column])

"""
lemmatize_column_tokens: lemattizes a column of tokens of a dataframe and saves it as column_stems

arguments:
    dataframe: pandas dataframe
    column:    string
"""
def lemmatize_column_tokens(dataframe, column):
    lemmatizer = WordNetLemmatizer()
    lemma_tokens = list()
    for index, row in dataframe.iterrows():
        lemma = list()
        for token in dataframe.loc[index,column]:
            lemma.append(lemmatizer.lemmatize(token))
        lemma_tokens.append(lemma)
    # save lemmatized tokens as a new column
    dataframe[f"{column}_lemmas"] = pd.Series(lemma_tokens, index=dataframe.index)