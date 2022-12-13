sum=0 
while True:
    Price= input("Enter The Price Of Items: ")
    if Price!='q':
        sum=sum+int(Price)

    else:
        print(f"Thanks For Shopping. Your Bill Total Is {sum}")
        break

