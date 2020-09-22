from collections import Counter


class Stopwords:

    def __init__(self, sent, stop):
        self.sentence = sent
        self.stopwords = stop

    def remove_stopwords(self):

        list_of_words = self.sentence.split()
        # print(list_of_words)

        term_counter = Counter(list_of_words)
        # print(term_counter)

        get_max_count = 0
        result = []

        for val in term_counter:
            if get_max_count < term_counter[val] and val not in self.stopwords:
                get_max_count = term_counter[val]
                # print(term_counter[val],"\t", val)

        for ans in term_counter:
            if term_counter[ans] == get_max_count and ans not in self.stopwords:
                result.append(ans)

        return result


if __name__ == '__main__':
    sentence = "jack and jill went to the market           to to to to market to buy bread and cheese cheese is jack " \
               "favourite food"
    stopwords = ["and", "he", "the", "to", "is"]

    stopwords_obj = Stopwords(sentence, stopwords)
    print(stopwords_obj.remove_stopwords())
