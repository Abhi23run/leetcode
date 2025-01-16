class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        word_list=[]
        i=0
        temp_word=''
        for i in range(len(s)):
            if s[i]!=' ':
                temp_word+=s[i]
            else:
                word_list.append(temp_word)
                temp_word=''

        if temp_word!='':
            word_list.append(temp_word)

        if len(pattern)!=len(word_list):
            return False
        else:
            let_word_map={}
            word_let_map={}

            for letter,word in zip(pattern,word_list):
                if letter in let_word_map:
                    if let_word_map[letter]!=word:
                        return False
                else:
                    let_word_map[letter]=word


            for word,letter in zip(word_list,pattern):
                if word in word_let_map:
                    if word_let_map[word]!=letter:
                        return False
                else:
                    word_let_map[word]=letter

            return True    
