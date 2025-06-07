admin=["admin"]
pswa=["admin"]
Library=[]
User=[]
act=''
sel=''
ss=''
while True:
    print("1.Admin \n2.User")
    opt=int(input("Select user type:"))
    if opt == 1:
        uname=input("Enter the username: ")
        upsw=input("Enter the password: ")
        if uname in admin and upsw in pswa:
            print("Welcome Admin\n")
            while act != '5':
                print("1.Add book\n2.Update book\n3.Delete book\n4.Display all books\n5.Exit")
                act=input("Select an action:")
                if act == '1':
                    # bk=[]
                    b_id=int(input("Enter book id:"))
                    title=input("Enter book title:")   
                    athr=input("Enter book author:")
                    if any(book[0] == b_id for book in Library):
                        print("Book id already exists")
                    else:
                        qty=int(input("Enter quantity:"))
                        # bk.append(b_id)
                        # bk.append(title)
                        # bk.append(athr)
                        # bk.append(qty)
                        print("Book added successfully")
                        # Library.append(bk)
                        Library.append([b_id,title,athr,qty])

                elif act == '2':
                    b_id=int(input("Enter book id to update:"))

                    for j in Library:
                        
                        if j[0]==b_id:
                            j[1]=input("Enter new title:")
                            j[2]=input("Enter new author:")
                            j[3]=input("Enter new quantity:")
                            print("Book updated successfully!")
                            break
                        else:
                            print("Book not found.")
                
                elif act == '3':
                    b_id=int(input("Enter book id to delete:"))
                    for j in Library:
                        if j[0]==b_id:
                            Library.remove(j)
                            print("Book deleted successfully!")
                            break
                        else:
                            print("Book not found.")

                elif act == '4':
                    for j in Library:
                        print(j)
                    
                elif act == '5':
                    print("Exiting...")
                    continue
    elif opt == 2:
        
        while sel != 3:
            print("1.Register\n2.Login\n3.Exit")
            sel=int(input("Select an option:"))
            if sel == 1:
                namei=input("Name: ")
                agei=input("Age: ")
                addressi=input("Address: ")
                phonei=input("Phone: ")
                usernamei=input("Username: ")
                passwordi=input("Password: ")

                if usernamei in User:
                    print("Username already taken!")
                elif phonei in User:
                    print("This number is already registered to an account!")
                else:
                    User.append([namei,agei,addressi,phonei,usernamei,passwordi])
                    print("Account successfully created!")  

            elif sel == 2:
                loguname=input("Enter username:")
                logpass=input("Enter password:")
                if loguname == usernamei and logpass == passwordi:
                    print("Login successfull!")
                    while True:
                        print("1.Display all books\n2.Search book\n3.Exit")
                        ss=int(input("Select an action:"))
                        if ss == 1:
                            for i in Library:
                                print(i)
                        
                        elif ss == 2:
                            search = input("Enter name of book:")
                            book_found = False
                            
                            for i in Library:
                                if i[1] == search:
                                    print(i)
                                    book_found = True
                            
                            if not book_found:
                                print("Book not available")
                        
                        elif ss == 3:
                            print("Exiting...")
                            break

                else:
                    print("Incorrect username or password")
    else:
        print("Enter valid option!!")











                

            


