
'''
        Stringi - wprowadzenie czy. 2
'''
#sklejanie plikow
drive = 'c:\\'
folder = 'script\\python\\'
file = 'myscript.py'
path = drive + folder + file
print(path)

# tekst jest traktowany jak surowy tekst
justText = 'text with\nnewline'
print(justText)

justText = r'text with\nnewline'
print(justText)
