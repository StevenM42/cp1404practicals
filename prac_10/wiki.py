import wikipedia

title = input('>>>')
page = wikipedia.page(title, auto_suggest=False)
print(page.title, page.summary, page.url)
