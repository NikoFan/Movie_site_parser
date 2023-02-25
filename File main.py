import requests
from bs4 import BeautifulSoup

import tkinter as tk

"""Создать экран"""
W = 515
H = 455

win = tk.Tk()
# title
win.title("Поисковик")
# икнока

photo = tk.PhotoImage(file="icon.png")
win.iconphoto(False, photo)
win.config(bg="#FFCCFF")
# Размер Окна
win.geometry(f"{W}x{H}")
win.resizable(False, False)
"""Зкран создан"""

"""Part 1"""
base = "/a-z/movies/2022"
text = 0

films = dict()
# concretic_Film = dict()

print()

"""САЙТ"""
url = "https://www.film.ru"

r = requests.get(url + base)
print(f"""Ссылка с которой работает программа:
| {url + base} |""")
print(base)

html = BeautifulSoup(r.content, 'html.parser')


def find():
    global films

    for el in html.select(".film_list_block > .film_list"):
        image = el.find("a", class_="film_list_link")
        element = el.find_all("div")
        link = (str(image["href"]))
        nameFilm = el.find("strong").text

        films[nameFilm] = link


def Preview(base, value_name):
    global url
    concretic_Film = dict()
    r = requests.get(url + base)
    print(f"""Ссылка с которой работает программа:
| {url + base} |""")

    html2 = BeautifulSoup(r.content, 'html.parser')

    for el in html2.select(".movies-center > .movies-center-table"):
        element = el.find_all("div", class_="h3")
        for i in element:
            concretic_Film[(i.text).upper()] = "None"

    actors(r, html2, value_name, concretic_Film)


def actors(r, html2, value_name, concretic_Film):
    html_2 = BeautifulSoup(r.content, 'html.parser')

    html_2 = html_2.find("div", class_="crew switch")

    txt = html_2.find_all("a")
    actor = []
    for el in txt:
        print(el["title"])
        actor.append(el["title"])
    inf(html2, value_name, concretic_Film, actor)
    # description(r, html2, value_name, concretic_Film, actor)


# если есть желание можете настроиь вывод Описания фильма, тут оно не всегда правильно форматируется
def description(r, html2, value_name, concretic_Film, actor):
    html_2 = BeautifulSoup(r.content, 'html.parser')

    html_2 = html_2.find("div", class_="synopsis", id="movies-1")

    txt = html_2.find_all("div", itemprop="description")

    des = []
    for el in txt:
        des = el.text.split(" ")

    word = "\n"
    ind = 8
    for i in range(4):
        try:
            des.insert(ind, word)
            ind += 8
        except IndexError:
            ind = -1
            des.insert(ind, word)

    second_window(des, html2, value_name, concretic_Film, actor)
    s = ["1", "\n", "2"]
    print(" ".join(s))


def second_window(des, html2, value_name, concretic_Film, actor):
    """Создать экран"""
    W = 480
    H = 455

    win2 = tk.Tk()
    # title
    win2.title("О фильме")
    # икнока

    win2.config(bg="#FFCCFF")
    # Размер Окна
    win2.geometry(f"{W}x{H}")
    win2.resizable(False, False)
    """Зкран создан"""
    tk.Label(win2, text=" ".join(des)).grid(row=1,
                                            column=0,
                                            ipadx=40,
                                            stick="nsew",
                                            )
    inf(html2, value_name, concretic_Film, actor)
    win2.mainloop()


def inf(html2, value_name, concretic_Film, actor):
    arr = []

    info2 = html2.find_all("div", class_="movies-center-table")
    for i in info2:
        item = i.find_all("strong")
        for j in item:
            element = (j.text).strip()
            print(element)
            arr.append(element)
    Dict(value_name, concretic_Film, arr, actor)


def Dict(value_name, concretic_Film, arr, actor):
    count = 0
    for key, value in concretic_Film.items():
        if count == 4:
            item = " ".join(arr[count].split())
            arr[count] = item
        if count == 5:
            item = " ".join(arr[count].split())
            arr[count] = item
        if key == "ССЫЛКИ":
            concretic_Film["ССЫЛКИ"] = url + base
        else:
            concretic_Film[key] = arr[count]
        count += 1
    concretic_Film["FILM NAME"] = value_name
    number = 1
    for act in actor:
        concretic_Film[f"ACTOR_{number}"] = act
        number += 1
    w(concretic_Film)


if base == "/a-z/movies/2022":
    find()
    for key, value in films.items():
        print(key, '|', value)
"""else:
    Preview()"""

print()

"""Part 2------------------------------------------------------"""

"""ЗАПРОС НА ФИЛЬМ"""


def get_entry():
    global films, base
    value_name = name.get()
    if value_name not in films:
        print("Not found! Please Repeat your search")
        tk.Label(win, text="Change the request").grid(row=0,
                                                      column=2,
                                                      stick="we",
                                                      ipadx=5,
                                                      )

    else:
        print("ELSE")
        base = films[value_name]
        print(films[value_name])
        tk.Label(win, text="Ready").grid(row=0,
                                         column=2,
                                         stick="we",
                                         ipadx=5,
                                         )
        Preview(base, value_name)


def delete():
    name.delete(0, "end")


def text(concretic_Film):
    # global concretic_Film
    for i in range(15):
        i += 2
        tk.Label(win, text="No information on site").grid(row=i,
                                                          column=0,
                                                          stick="we",
                                                          )
        tk.Label(win, text="Lost").grid(row=i,
                                        column=1,
                                        stick="we",
                                        )
        tk.Label(win, text="Lost").grid(row=i,
                                        column=2,
                                        stick="we",
                                        )
    for_CF(concretic_Film)


def for_CF(CF):
    concretic_Film = CF
    count = 2
    sl = []
    print("YEP", concretic_Film)
    for key, value in concretic_Film.items():
        print(key, ':', value)
        tk.Label(win, text=key).grid(row=count,
                                     column=0,
                                     ipady=3,
                                     stick="we")
        tk.Label(win, text=" : ").grid(row=count,
                                       column=1,
                                       ipady=3,
                                       stick="we")

        my_text = tk.Entry(win)
        my_text.insert(0, value)
        sl.append(value)

        my_text.config(state="readonly")
        my_text.grid(row=count,
                     column=2,
                     ipadx=50,
                     ipady=3,
                     stick="we")

        count += 1
        print(count)

    print("Конец?", concretic_Film)


tk.Label(win, text="Запрос").grid(row=0,
                                  column=0,
                                  columnspan=2,
                                  ipadx=50,
                                  stick="w")

name = tk.Entry(win)
name.grid(row=0,
          column=1,
          columnspan=2,
          ipadx=20,
          stick="w")

button = tk.Button(win,
                   text="Search",
                   command=get_entry,
                   bg="cyan").grid(row=1,
                                   column=0,
                                   stick="we")
print("after", url + base)
del_Button = tk.Button(win,
                       text="Delete",
                       command=delete,
                       bg="red").grid(row=1,
                                      column=1,
                                      ipadx=60,
                                      stick="we")


def w(c_Film):
    concretic_Film = c_Film
    print(concretic_Film)
    tk.Button(win,
              text="View information",
              command=text(concretic_Film),
              bg="green").grid(row=1,
                               column=2,
                               stick="we")


win.grid_columnconfigure(0,
                         minsize=100)

win.grid_columnconfigure(1,
                         minsize=100)
win.mainloop()
