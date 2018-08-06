import numpy as np
import jieba
import os

class KeyWrapper(object):
    '''
    The tool class for user keywords pre-process 
    '''
    def __init__(self, tau=4, delta=40):
        self.__tau = tau
        self.__delta = delta
        self.__root_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
        self.__loadDic()
        jieba.load_userdict(self.__root_dir + "data/goodwords_jian_final_freq.txt")
        self.noise = False


    def __loadDic(self):
        # Load TF-IDF 
        self.__tfidf = {}       
        fin = open(self.__root_dir + "data/tfidf.txt",'r')
        line = fin.readline()
        while line:
            para = line.strip().split(" ")
            self.__tfidf[para[0]] = float(para[1])
            line = fin.readline()
        fin.close()

        # Load word frequency
        self.__freq = {}
        fin = open(self.__root_dir + "data/wordsfreq.txt",'r')
        line = fin.readline()
        while line:
            para = line.strip().split(" ")
            self.__freq[para[0]] = int(para[1])
            line = fin.readline()
        fin.close()

        # Load function words
        self.__func = {}
        fin = open(self.__root_dir + "data/FunctionWords.txt",'r')
        lines1 = fin.readlines()
        fin.close()

        fin = open(self.__root_dir + "data/fchar.txt",'r')
        lines2 = fin.readlines()
        fin.close()

        lines = lines1 + lines2
        for line in lines:
            self.__func[line.strip()] = 1
        fin.close()


    def line2chars(self, line):
        """
        Split a line to a lits of characters
        Input: a Chinese sequence with utf-8
        Output: a lits of characters with utf-8
        """
        chars= []
        sen = line.decode("utf-8")
        for c in sen:
            chars.append(c.encode("utf-8"))
        return chars

    def __get_val(self, w, typ):
        if typ == 'tfidf':
            dic = self.__tfidf
        elif typ == 'freq':
            dic = self.__freq

        if w in dic:
            return dic[w]
        else:
            return 0.1


    def __my_split(self, w):
        #print ("***********")
        #print (w)
        seg_list = jieba.cut(w) 
        words = []
        for word in seg_list:
            word = word.encode("utf-8")
            words.append(word)

        #print (" ".join(words))
        #print ("***********")

        if len(words) == 1:
            return self.line2chars(words[0])
        else:
            return words


    def __do_split(self, ws):
        for w in ws:
            n = self.__get_val(w, 'freq')
            if len(w) > 6 or ( len(w) == 6 and n < self.__delta ):
                return True
        return False

    def __split_word(self, w):
        words = [w]
        while self.__do_split(words):
            newwords = []
            for w in words:
                n = self.__get_val(w,'freq')
                if len(w) >= 9 or ( len(w) == 6 and n < self.__delta ):
                    ws = self.__my_split(w)
                    ws = list(set(ws))
                    newwords.extend(ws)
                else:
                    newwords.append(w)

            words = list(set(newwords))
            if self.noise:
                print ("iter: %s" % (" ".join(words)))

        return words


    def __selectbytfidf(self, words):
        vals = []
        for w in words:
            vals.append(self.__get_val(w,'tfidf'))
        idxes = list(np.argsort(vals))
        idxes.reverse()
        newwords = [words[idx] for idx in idxes]
        newwords = newwords[0:self.__tau]
        return newwords

    def process(self, keywords):
        '''
        preprocess user keywords
        NOTE: the input keywords must be encoded by UTF-8
        Input: a list of keywords. No requirements on the number
                    of keywords or on the length of each keyword.
        Output: (recom, words)
                     recom: a  string, the recommended model to generate the poem, 'wm' or 'ks'
                     words: a list of strings, the processed new keywords list, where there are 4 keywords at most,
                     and each keyword consists of 2 characters at most.
        '''
        if self.noise:
            print ("ori words:" + " ".join(keywords))
        K = len(keywords)
        if K == 1 and len(keywords[0]) <= 9:
            return ('ks', keywords)

        if K == 1:
            newords = self.__split_word(keywords[0])
        else:
            newords = []
            for w in keywords:
                newords.extend(self.__split_word(w))

        newords = list(set(newords))
        filter_words = []
        if self.noise:
            print ("split words: " + " ".join(newords))
        for w in newords:
            if not w in self.__func:
                filter_words.append(w)

        if self.noise:
            print ("filter words: " + " ".join(filter_words))
        if len(filter_words) > self.__tau:
            filter_words= self.__selectbytfidf(filter_words)
        if self.noise:
            print ("select words:" + " ".join(filter_words))
        return ("wm", filter_words)