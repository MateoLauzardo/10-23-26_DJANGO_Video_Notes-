

import re 

def parse_query_string(url):
    
    pattern = r"\w+|[^\w\s]"
    
    result = re.findall(pattern, url) # ['?', 'item', '=', 'tea', '&', 'size', '=', 'large']
    
    flag = False
    values = [] # ['item', 'tea', 'size', 'large']
    
    for char in result:
        
        if char == "?":
            flag = True 
        
        if flag:
            if isinstance(char, str) and char.isalpha():
                values.append(char)
                
    
    answer = {}
    
    for x in range(0, len(values), 2):
        
        key = x 
        value = x + 1
        answer[values[key]] = values[value]
        
    return answer 
    


print(parse_query_string("menu/?item=tea&size=large"))
print(parse_query_string("menu/"))


#example output:
# {'item': 'tea', 'size': 'large'}
# {}