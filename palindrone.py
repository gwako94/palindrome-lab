import re
def isPalindrome(string):
  string1 = ''
  if isinstance(string, str):
    string = re.split(r"\W+",string.lower())
    for c in string:
      string1+=c
    if string1 == string1[::-1]:
      return True
    return False
  return False
    
print(isPalindrome("12a toyota's a toyota21"))