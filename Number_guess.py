import random
l=[]
def checker():
        computer = random.randint(1, 5)
        print(computer)
        num = int(input('Enter a Number'))



 
        for i in range (1,computer+1):
                if computer == num :
                        print('Well Done')
                        print(f'You required {len(l)} Steps to guess the correct number')
                        break
                elif computer> num :
                        print('Enter Higher Value')
                        l.append(num) 
                        checker()
                        break 
                elif computer < num:
                        print('Enter Lower Value') 
                        l.append(num) 
                        checker() 
                        break

                                          
        

checker()