# Text-Web-and-Media-Analytics
Algorithms for information analytics by Python
# Notes for self
```Python
    term_number = {}  
    for term in query.split(): #if nothing in it, split space, \n, \t. 默认为所有空字符
        try:
            term_number[term] += 1
        except KeyError:
            term_number[term] = 1
