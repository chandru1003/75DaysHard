
def get_user_info():
    name=input("Enter Your name: ")
    email=input("Enter your Email ID: ")
    habitscount=int(input("How many habits do want to follow?"))
    daycount=int(input("number of day you want to follow :"))
    habits=[]
    timings=[]
    
    for i in range(habitscount):
        habit=input(f"Enter the habit {i+1}: ")
        timestr=input(f"Enter Timing for habit {i+1} (e.g., 07:00 Am) : ")
        timings.append(timestr)
        habits.append(habit)
        
  
    return name, email, habits, timings, daycount

def main():
    print("Welcome to 75 Days Hard!")
    name,email,habits, Timing, daycount=get_user_info()
    print(name)
    print(email)
    daycounter=1
    while daycounter<=daycount:
        print(f"List of habits to follow , Day-{daycount}")
        for  i,habit in enumerate(habits):
            print(f"-{habit}: do it at {Timing[i]}")
        daycounter +=1
        print("---------------------------------------------------")
        print("\n")
    
if __name__=="__main__":
    main()