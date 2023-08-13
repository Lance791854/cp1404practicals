import wikipedia


user_search = " "
while user_search != "":
    user_search = input("What would you like to search for? ")
    try:
        searched_page = wikipedia.page(user_search, auto_suggest=False)
        print(searched_page.title)
        print(searched_page.summary)
        print(searched_page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)




