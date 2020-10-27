class WordAnalyser():
    
    def __init__(self):
        self.Dict={}

    def __str__(self):
        
        for key,value in self.Dict.items():
            if key in self.seq:
                print('The count of {} is :{}'.format(key,value))
        print('-------------------------------------------------------------')
       
        
        return ''
    
    def analyse_words(self, decoded_sequence):
        self.rem=decoded_sequence
        self.a=self.rem.replace('?','')
        self.b=self.a.replace('.','')
        self.final=self.b.replace(',','')
        self.seq=self.final.split(' ')
        #print(self.seq)
        
        for i in self.seq:
            if (i==''  or i=='?' or i==',' or i=='.'):
                continue
            
            elif i in self.Dict:
                self.Dict[i]+=1
            
            else:
                self.Dict[i]=1