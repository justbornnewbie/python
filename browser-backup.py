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
    except urllib.error.URLError as e:
       print(e.reason)
print_some_url()   