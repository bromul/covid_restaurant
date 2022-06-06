# Define function to ensure each word is lemmatized as the proper part of speech
def lemma_pos(text):
    
    # Dependencies
    from nltk.corpus import wordnet as wn
    from nltk.stem.wordnet import WordNetLemmatizer
    from nltk import word_tokenize, pos_tag
    from collections import defaultdict

    # Create tag map
    tag_map = defaultdict(lambda : wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV


    tokens = word_tokenize(text)
    lmtzr = WordNetLemmatizer()

    # Initialize list
    lemmas = []

    for token, tag in pos_tag(tokens):
        lemma = lmtzr.lemmatize(token, tag_map[tag[0]])
        lemmas.append(lemma)
    
    return lemmas

###########################################################################
###########################################################################

# Defining function to word tokenize and lemmatize each review, then check for sense words

def create_word_list(review):
    
    # Dependencies
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords

    # Define stop words
    stop_words = set(stopwords.words('english'))

    # Word tokenize review
    review_words = word_tokenize(review)

    # Filter words 
    filtered_words = []

    filtered_words = [
        word for word in review_words if word.casefold() not in stop_words
    ]

    # Lemmatize filtered words
    lemmas = lemmas_pos(filtered_words)
    
    # Check for sense words
    

    # If/Else - food/not
    

    # Return finalized list


###########################################################################
###########################################################################

# Define function to breakdown business categories and sort them
def business_categorizer(business):
    
    # Dependencies
    
    
    # Breakdown Category


    # Check for terms related to restaurants
    # Drop unrelated businesses


    # Return df
