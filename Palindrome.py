#Filename: Palin.py

def reverse(text):
    return text[::-1]
    
def is_palin(text):
    return text==reverse(text)
    
test_text=input()
if is_palin(test_text):
    print('Yes')
