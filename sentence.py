class SentenceAnalyser():
    
    def __init__(self):
        self.Dict={}

    def __str__(self):
        
        for key,value in self.Dict.items():
            if key in self.seq:
                print('The count of {} is :{}'.format(key,value))
        print('-------------------------------------------------------------')
        
        return ''
    
    def analyse_sentences(self, decoded_sequence):
        self.seq=decoded_sequence
        for i in self.seq:
            if (i=='?') and i in self.Dict:
                self.Dict[i]+=1
            elif (i=='?') and i not in self.Dict:
                self.Dict[i]=1
            elif (i==',')and i in self.Dict:
                self.Dict[i]+=1
            elif (i==',') and i not in self.Dict:
                self.Dict[i]=1
        
            elif (i=='.')and i in self.Dict:
                self.Dict[i]+=1
            elif (i=='.') and i not in self.Dict:
                self.Dict[i]=1
            else:
                continue
        #return self.Dict