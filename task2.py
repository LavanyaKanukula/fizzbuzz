
def unique_words(book):
    text = book.read()

    #cleaning
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]"') for word in words]
    words = [word.replace("'s", '') for word in words]

    #finding unique
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)
            
    #sort
    unique.sort()

    #print
    print(unique)
    
book = open("c:\\Users\lavan\Python_Assignment_Midterm\openbook1-LavanyaKanukula\Book1.txt")
unique_words(book)