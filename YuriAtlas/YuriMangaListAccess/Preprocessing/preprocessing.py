from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag


class TextPreprocessor:
    def __init__(self, text):
        self.text = text

    def normalize(self):
        self.text = self.text.lower()
        return self

    def tokenize(self):
        tokenizer = RegexpTokenizer(r'\w+')
        self.text = tokenizer.tokenize(self.text)
        return self

    def remove_stopwords(self):
        stop_words = set(stopwords.words('english'))
        self.text = [word for word in self.text if word not in stop_words]
        return self

    def lemmatize(self):
        tagged_words = pos_tag(self.text)
        self.text = [self._lemmatize_with_pos(w, t) for w, t in tagged_words]
        return self

    def _lemmatize_with_pos(self, word, treebank_tag):
        lemmatizer = WordNetLemmatizer()
        wordnet_tag = self._get_wordnet_pos(treebank_tag)

        print(word, wordnet_tag)
        if wordnet_tag in ('a', 'r') and word.endswith('er'):
            return word[:-2]  # Strip 'er' for comparatives
        elif wordnet_tag in ('a', 'r') and word.endswith('est'):
            return word[:-3]  # Strip 'est' for superlatives
        else:
            return lemmatizer.lemmatize(word, wordnet_tag)

    @staticmethod
    def _get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return 'a'  # Adjective
        elif treebank_tag.startswith('V'):
            return 'v'  # Verb
        elif treebank_tag.startswith('N'):
            return 'n'  # Noun
        elif treebank_tag.startswith('R'):
            return 'r'  # Adverb
        else:
            return 'n'  # Default to noun

    def process(self):
        return self.normalize().tokenize().remove_stopwords().lemmatize()
