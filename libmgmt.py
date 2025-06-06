admin=["admin"]
pswa=["admin"]
Library=[]
act=''
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
                if b_id in Library:
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
                break










            

        


