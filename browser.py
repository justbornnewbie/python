import webbrowser
import urllib.request
#webbrowser.open('http://latkibhai.tk')
def print_some_url():
    try:
        with urllib.request.urlopen('http://latkibhai.tk/') as f:
           a_variable = f.read().decode('utf-8')
           print(a_variable)
           file = open("sample.txt", "w")
           str_dictionary = repr(a_variable)
           file.write(str_dictionary)
           string1 = 'Niki'
           file1 = open("sample.txt", "r") 
           readfile = file1.read()
           if string1 in readfile: 
             print('String', string1, 'Found In File')
           else: 
             print('String', string1 , 'Not Found') 
           file1.close() 
    except urllib.error.URLError as e:
       print(e.reason)
print_some_url()   