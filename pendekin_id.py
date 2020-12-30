from RandomWordGenerator import RandomWord
import re

def shorten(my_link):
    if (my_link.find("short_path") == -1 ):
        short_path = rw.generate()
        link = my_link[my_link.index("url=") + 4 : ]
    else :
        short_path = my_link[my_link.index("short_path=") + 11 :]
        link = (re.search('url=(.+?)\&', my_link)).group(1)
    
    pair[short_path] = [link, 0]    
    print("https://pendekin.id/" + short_path)

def redirect(my_link):
    short_path = my_link[my_link.index(".id/") + 4 : ]
    try:
        print(pair[short_path][0])
        pair[short_path][1] += 1
    except:
        print("Error: " + short_path +  " not found in the service")

def delete(my_link):
    short_path = my_link[my_link.index(".id/") + 4 : ]
    try:
        del pair[short_path]
        print("OK")
    except:
        print("Error: " + short_path + " not found.")

def count(my_link):
    short_path = my_link[my_link.index(".id/") + 4 : ]
    try:
        print(pair[short_path][1])
    except:
        print("Error: " + short_path + " not found in the service")

pair = {}
rw = RandomWord(max_word_size=5)

while True :
    link = input()
    try:
        regx = re.search('/(.+?)\?', link)
        found = regx.group(1)
        if found == "shorten":
            shorten(link)
        elif found == "redirect":
            redirect(link)
        elif found == "delete":
            delete(link)
        elif found == "count":
            count(link)
    except:
        print("Harap masukkan input dengan benar")