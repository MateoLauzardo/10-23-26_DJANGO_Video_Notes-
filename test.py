# takes books
# takes author string, 
# and returns a dictionary with:

# 'author': the author’s name
# 'books': a list of that author’s book titles, sorted by year (oldest first)
# 'count': how many books they wrote

#{'author': 'Milne', 'books': ['Winnie-the-Pooh', 'The House at Pooh Corner'], 'count': 2}


def build_context(books, author):
    
    matching = []
    
    for book in books:
        if book["author"] == author:
            matching.append(book)

    # sorting the books by years
    matching = sorted(matching, key=lambda book: book["year"])
    
    titles = []
    for book in matching:
        titles.append(book["title"])
        
        
    return {
        "author": author,
        "books": titles,
        "count": len(titles)
    }
    
# loop thorugh books 
# create own hashmap, if author hasnt been seen yet create a new one 
# author, array in hashmap with all his books, and a count flag 



books = [
    {"title": "The House at Pooh Corner", "author": "Milne", "year": 1928},
    {"title": "Charlotte's Web", "author": "White", "year": 1952},
    {"title": "Winnie-the-Pooh", "author": "Milne", "year": 1926},
]
print(build_context(books, "Milne"))
print(build_context(books, "Seuss"))