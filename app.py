from io import RawIOBase
from ipaddress import collapse_addresses
from sqlite3 import Row
from string import hexdigits
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from typing import final
from unittest import TextTestResult
from urllib.request import urlopen
import spacy
nlp = spacy.load('en_core_web_sm')


from spacy_summarization import text_summarization, evaluate
from nltk_summarization import nltk_summarization
from gensim.summarization import summarize

from bs4 import BeautifulSoup
from urllib.request import urlopen


window = Tk()
window.title("Automatic Text Summarizer")
window.geometry("700x550")
style = ttk.Style(window)

tab_control = ttk.Notebook(window, style='lefttab.TNotebook')
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Home")
tab_control.add(tab2, text="File")
tab_control.add(tab3, text="URL")
tab_control.add(tab4, text="Comparer")
tab_control.add(tab5, text="About")

label1 = Label(tab1, text='Summarizer', padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text='File processing', padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text='URL', padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab4, text='Compare Summarizers', padx=5, pady=5)
label4.grid(column=0, row=0)

label5 = Label(tab5, text='About', padx=5, pady=5)
label5.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

# functions - HOME

def clear_text():
    entry.delete('1.0', END)


def getsummary():
    raw_text = str(entry.get('1.0', tk.END))
    final_text = text_summarization(raw_text)
    print(final_text)
    result = '{}'.format(final_text)
    tab1_display.insert(tk.END, result)
    results = evaluate(nlp,result)
    print(results)


def clear_display_result():
    tab1_display.delete('1.0', END)


#functions - File

def openFiles():
    file1 = tkinter.filedialog.askopenfilename(
        filetypes=(("Text Files", ".txt"), ("All files", "*")))
    read_text = open(file1).read()
    displayed_file.insert(tk.END, read_text)


def get_file_summary():
    raw_text = displayed_file.get('1.0', tk.END)
    final_text = text_summarization(raw_text)
    result = '{}'.format(final_text)
    tab2_display_text.insert(tk.END, result)


def clear_text_result():
    tab2_display_text.delete('1.0', END)


def clear_text_file():
    displayed_file.delete('1.0', END)


#functions - URL

def clear_url_entry():
    url_entry.delete(0, END)


def clear_url_display():
    tab3_display_text.delete('1.0', END)


def get_text():
    raw_text = str(url_entry.get())
    page = urlopen(raw_text)
    soup = BeautifulSoup(page, "html.parser")
    fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    url_display.insert(tk.END, fetched_text)


def get_url_summary():
    raw_text = url_display.get('1.0', tk.END)
    final_text = text_summarization(raw_text)
    result = '{}'.format(final_text)
    tab3_display_text.insert(tk.END, result)


#function - comparer

def clear_compare_display_result():
    tab4_display.delete('1.0', END)


def clear_compare_text():
    entry1.delete('1.0', END)


def use_spacy():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = text_summarization(raw_text)
    print(final_text)
    result = '{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_nltk():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = nltk_summarization(raw_text)
    print(final_text)
    result = '{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_gensim():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = summarize(raw_text)
    print(final_text)
    result = '{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_sumy():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = text_summarization(raw_text)
    print(final_text)
    result = '{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


# Home
l1 = Label(tab1, text="Enter Text to summarize: ")
l1.grid(row=1, column=0)
l2 = Label(tab1, text="Summary: ")
l2.grid(row=6, column=0)

entry = Text(tab1, height=10)
entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

button1 = Button(tab1, text="Reset", command=clear_text,
                 width=12, bg='crimson', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab1, text="Summarize", command=getsummary,
                 width=12, bg="cyan4", fg="#fff")
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab1, text="Clear Result",
                 command=clear_display_result, width=12, bg="#03A9F4", fg="#fff")
button3.grid(row=5, column=0, padx=10, pady=10)


tab1_display = Text(tab1, height=10)
tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# File
l1 = Label(tab2, text="Choose File to Summarize: ")
l1.grid(row=1, column=1)
l2 = Label(tab2, text="Summary: ")
l2.grid(row=6, column=1)

displayed_file = ScrolledText(tab2, height=7)
displayed_file.grid(row=2, column=2, columnspan=3, padx=5, pady=5)

b0 = Button(tab2, text="Open File", width=12, command=openFiles, bg='#c5cae9')
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="Reset", width=12,
            command=clear_text_file, bg='crimson')
b1.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(tab2, text="Summarize", width=12,
            command=get_file_summary, bg='cyan4', fg='#fff')
b2.grid(row=3, column=2, padx=10, pady=10)

b3 = Button(tab2, text="Clear Result", width=12, command=clear_text_result, bg='#03A9F4')
b3.grid(row=5, column=1, padx=10, pady=10)

b4 = Button(tab2, text="Close", width=12, command=window.destroy)
b4.grid(row=5, column=2, padx=10, pady=10)

tab2_display_text = ScrolledText(tab2, height=10)
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
# Allow edit
tab2_display_text.config(state=NORMAL)


# URL
l1 = Label(tab3, text="Enter URL to Summarize: ")
l1.grid(row=1, column=0)
l2 = Label(tab3, text="Summary: ")
l2.grid(row=9, column=0)

raw_entry = StringVar()
url_entry = Entry(tab3, textvariable=raw_entry, width=50)
url_entry.grid(row=1, column=1)

button1 = Button(tab3, text="Reset", command=clear_url_entry,
                 width=12, bg="crimson", fg="#fff")
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab3, text="Get text", command=get_text,
                 width=12, bg="#03A9F4", fg="#fff")
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab3, text="Clear Result",
                 command=clear_url_display, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab3, text="Summarize", command=get_url_summary,
                 width=12, bg='cyan4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

url_display = ScrolledText(tab3, height=10)
url_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

tab3_display_text = ScrolledText(tab3, height=10)
tab3_display_text.grid(row=10, column=0, columnspan=3, padx=5, pady=5)


# Comparer
l1 = Label(tab4, text="Enter text to summarize: ")
l1.grid(row=1, column=0)
l2 = Label(tab4, text="Summary: ")
l2.grid(row=6, column=0)

entry1 = ScrolledText(tab4, height=10)
entry1.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

button1 = Button(tab4, text="Reset", command=clear_compare_text,
                 width=12, bg='crimson', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab4, text="spaCy", command=use_spacy,
                 width=12, bg='firebrick4', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab4, text="Clear Result",
                 command=clear_compare_display_result, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab4, text='NLTK', command=use_nltk,
                 width=12, bg='firebrick4', fg='#fff')
button4.grid(row=4, column=2, padx=10, pady=10)

button5 = Button(tab4, text="Gensim", command=use_gensim,
                 width=12, bg='firebrick4', fg='#fff')
button5.grid(row=5, column=1, padx=10, pady=10)

button6 = Button(tab4, text='Sumy', command=use_sumy,
                 width=12, bg='firebrick4', fg='#fff')
button6.grid(row=5, column=2, padx=10, pady=10)


tab4_display = ScrolledText(tab4, height=15)
tab4_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)


#About
about_label=Label(tab5,text="This is a Graduation Project worked by Zenel Hila.\nIt is able to summarize different given texts starting from raw text, inputed file and even URL links. \nAlso a comparer between different NLP libraries is offered.\n NOTE: GENSIM library should be version 3.8.3.", padx=5,pady=5)

about_label.grid(column=0,row=1)

window.mainloop()
