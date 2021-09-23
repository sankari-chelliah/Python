def isPalandrome(s):
    '''Cleans the string and check whether its a Palandrome'''

    def cleanString(s):
        s= s.lower()
        clean_str = ''
        for x in s:
            if x in 'abcdefghijklmnopoqrstuvwxyz':
                clean_str = clean_str + x
        return clean_str


    def isPal(s):
        if len(s) <=1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(cleanString(s))




str1 = str(input("Enter a string to check whether its a Palandrome "))
if (isPalandrome(str1)):
    print(f"Yes! {str1} is a Palandrome")
else:
    print(f"No! {str1} is not a Palandrome")
