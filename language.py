import json
from textblob import TextBlob

from googletrans import Translator

# from translate import Translator

from tkinter import *

langdata = json.load(open("language.json")) #Json file with all the languages
fromlang = ""
tolang = []

master = Tk()

master.title("Language Translator")

fromlanglist = langdata["language"]

for key in fromlanglist:
    fromlang = fromlang + "," + key

fromlang = fromlang.strip(",").split(",")

fromvariable = StringVar(master)
fromvariable.set("Select From Language: ")

tovariable = StringVar(master)
tovariable.set("Select To Language: ")

# print(fromlang)

fromlangoptions = OptionMenu(master, fromvariable, *fromlang)
fromlangoptions.pack()

fromframe = Frame(master, borderwidth=1, relief=SUNKEN)

fromlanginput = Entry(fromframe)

# fromlanginput = Text(master, height=2, width=20)
fromlanginput.pack()
fromframe.pack()

tolangptions = OptionMenu(master, tovariable, *fromlang)
tolangptions.pack()

toframe = Frame(master, borderwidth=1, relief=SUNKEN)
# tolangoutput = Text(master, height=2, width=20)
tolangoutput = Entry(toframe)
tolangoutput.pack()
toframe.pack()


def langtranslate():

    fromlanguage = langdata["language"][fromvariable.get()]
    tolanguage = langdata["language"][tovariable.get()]

    langinput = TextBlob(fromlanginput.get())

    translatedlang = langinput.translate(from_lang=fromlanguage, to=tolanguage)

    tolangoutput.insert(END, translatedlang)


translatebutton = Button(master, text='Translate', command=langtranslate)
exitbutton = Button(master, text='Quit', command=master.quit)

exitbutton.pack()
translatebutton.pack()

mainloop()
