class Decoder():
    
    def __init__(self):
        self.sample_dict={'01':'A','1000':'B','1010':'C','100':'D','0':'E','0010':'F','110':'G',
      '0000':'H','00':'I','0111':'J','101':'K','0100':'L','11':'M','10':'N',
      '111':'O','0110':'P','1101':'Q','010':'R','000':'S','1':'T','001':'U',
      '0001':'V','011':'W','1001':'X','1011':'Y','1100':'Z','11111':'0',
       '01111':'1','00111':'2','00011':'3','00001':'4','00000':'5','10000':'6','11000':'7',
      '11100':'8','11110':'9','001100':'?','010101':'.','110011':','}
        
    def __str__(self):
        for key,value in self.sample_dict.items():
            print('\nKey: {} ||  value: {}'.format(key,value))
        print('----------------------------------------------------')
        print('The decoded full morse code is:\n')
        return (self.final_ans)
            
    def decode(self, morse_code_sequence):
        #print('enterd decode func')
        self.code=morse_code_sequence
        self.final_ans = self.decode_sentences(self.code)
        return self.final_ans
        
        
    def decode_letters(self,letter):
        #print('enterd decoded_letters')
        self.opt=('001100','110011','010101')
        self.letters=letter.split('*')
        self.ind_letter=''
        if any((x in self.letters)for x in(self.opt)):
            for each in self.letters:
                self.ind_letter+=self.sample_dict[each]
        else:
            self.ind_letter+=' '
            for each in self.letters:
                self.ind_letter+=self.sample_dict[each]
                
        return self.ind_letter
    
    def decode_words(self,word):
        #print('enterd decoded_words')
        self.words=word.split('***')
        self.ind_word=''
        for each in self.words:
            self.ind_word+=self.decode_letters(each)
        return self.ind_word
    
    def decode_sentences(self,sent):
        self.sentence=sent.split(',')
        #print('enterd decoded_sentence')
        self.ind_sent=''
        for each in self.sentence:
            self.ind_sent+=self.decode_words(each)
        return self.ind_sent
    
    
