def main ():
    #activate the bookList
    bookList = []
    
    
    choice = 0
    while choice !=5:
        print("***Books library***")
        print("1) Add a book")
        print("2) Search for a book")
        print("3) Display books")
        print ("4) Delete a book")
        print("5) Quit")
        choice = int(input())
        
        if choice == 1:
            print ("Adding a book...")
            nBook = input("Enter the name of the book_")
            nAuthor = input ("Enter the name of the author_")
            nPages = input ("Enter the number of pages_")
            nGenre = input ("Enter the type of genre_")
            nPublication = input ("Enter the publication date_")
            bookList.append([nBook,nAuthor,nPages,nGenre,nPublication])
            
            
if __name__ == "__main__":
    main()    
    
