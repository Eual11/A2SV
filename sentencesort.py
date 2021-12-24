class Solution:
    def sortSentence(self, s: str) -> str:
        listop=s.split()
        listhold=s.split()
        for char in listop:
            char2=char[::-1]
            cnst=int(char2[0])
            listhold[cnst-1]=char[0:len(char)-1]
        return " ".join(listhold)
        
