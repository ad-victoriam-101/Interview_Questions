# A ternary search tree is a trie-like data structure where 
# each node may have up to three children. Here is an example 
# which represents the words code, cob, be, ax, war, and we.
# ************************************************************
#        c
#     /  |  \
#    b   o   w
#  / |   |   |
# a  e   d   a
# |    / |   | \ 
# x   b  e   r  e  

parent = ["code","cod","cob","bee","ax","war","we"]
# print(given_arr)

class TernaryTree:
    def __init__(self):
        self.char = None
        self.low = None
        self.mid = None
        self.rep = None
    def __repr__(self):
        return "{}->[{}-{}-{}]".format(
            self.char if self.char else "",
            self.mid if self.mid else "",
            self.low if self.low else "",
            self.rep if self.rep else ""
        )
    @staticmethod
    def add_tree_method(loc,word):
        if not loc:
            loc = TernaryTree()
        loc.add_word(word)
        return loc
    def add_word(self,word):
        if not word:
            return
        fch = word[0]
        # grabs the first letter of the word and assigns the remaining word to a placeholder
        rem_word = word[1:]
        if not self.char:
            self.char = fch
            self.mid = TernaryTree.add_tree_method(self.mid,rem_word)
        elif self.char == fch:
            sel.mid = TernaryTree.add_tree_method(self.mid,rem_word)
        elif self.char < fch:
            # remember that operators can check alphabetical placement of letters
            # (a>b) will return True.
            self.low = TernaryTree.add_tree_method(self.low,word)
        else:
            self.rep = TernaryTree.add_tree_method(self.low,word)
    def search_word(self,word):
        fch = word[0]
        rem_word = word[1:]

        if fch == self.char:
            if not rem_word and not self.mid.char:
                return True
        elif fch < self.char:
            if not self.low
                return False
            return self.low.search_word(word)
        else:
            if not self.rep:
                return False
            return self.rep.search_word(word)
