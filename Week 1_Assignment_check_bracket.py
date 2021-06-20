
text = input()

stack = []

reverse_brackets = []

wrong_index = []

brack_index = []

def checkbracket(text,stack,wrong_index,reverse_brackets,brack_index):
    
    s = text

    for i in range(len(s)):
        
        
        #print(s[i])
        
        if s[i] == "[" or s[i] =="{" or s[i] == "(":
            
            stack.append(s[i])
            
            brack_index.append(i)
            
           
                        
             
        elif s[i] == "]" or s[i] == ")" or s[i] == "}":
            
            reverse_brackets.append(s[i])
            
            
            if stack != []:
            
                top = stack.pop()
                
                popindex = brack_index.pop()
                
                popreverseindex = reverse_brackets.pop()
                
                #print(reverse_brackets)
                
               
                
            else:
                
                top = ""

            
            #match or not 
                
            if (s[i] == "]" and top != "["):
                
                wrong_index = i+1
                    
                
            elif (s[i] == ")" and top != "("):
                
                wrong_index = i+1
                
            elif (s[i] == "}" and top != "{"):
                
                wrong_index = i+1
                    
    
    
    if stack != [] and reverse_brackets == []:
        
        wrong_index = brack_index.pop() +1
        
    
    if wrong_index == []:
        
        print("Success")
        
    else:
        
        print(wrong_index)
    
    
checkbracket(text,stack,wrong_index,reverse_brackets,brack_index)    
    

            
            
            
            
            
                
                   
                    
                    
            
