class CharacterAnalyser():
    def __init__(self):
        self.Dict={}
        
    def __str__(self):
        for key,value in self.Dict.items():
            if key in self.seq:
                print('The count of {} is :{}'.format(key,value))
        print('-------------------------------------------------------------')
        return '' 
         
        
    def analyse_characters(self,decoded_sequence):
        self.seq=decoded_sequence
        
        for i in self.seq:
            if (i==' ' or i==',' or i=='.' or i=='?'):
                continue
            
            elif i in self.Dict:
                self.Dict[i]+=1
                
            else:
                self.Dict[i]=1