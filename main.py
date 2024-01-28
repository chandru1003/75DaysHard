import re
from datetime import datetime, timedelta
def get_user_info():
    email_pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    timings_pattern=r'^\d{1,2}:\d{2} (AM|PM)$'
    
    name=input("Enter Your name: ")
           
    while True:
        email=input("Enter your Email ID: ")
        if re.match(email_pattern, email):
            break
        else:
            print("Invalid email format. Please enter a valid email address")
                
    
    habitscount=int(input("How many habits do want to follow? "))
    daycount=int(input("number of day you want to follow :"))
    habits=[]
    timings=[]
    
    
    for i in range(habitscount):
        habit=input(f"Enter the habit {i+1}: ")
        while True:
            timestr=input(f"Enter Timing for habit {i+1} (e.g., 07:00 Am) : ")
            if re.match(timings_pattern, timestr):
                timings.append(timestr)
                habits.append(habit)
                break
            else:
                print("Invalide Time formate...")        
  
    return name, email, habits, timings, daycount

def main():
    print("Welcome to 75 Days Hard!")
    name,email,habits, Timing, daycount=get_user_info()
    print(name)
    print(email)
    daycounter=1
    
    start_date=datetime.now()+ timedelta(days=1)
    for day in range(1, daycount+1):
        print("\n")  
        print(f"List of habits to follow , Day-{day} ({start_date.strftime('%d-%m-%Y')}):") 
        for  i,habit in enumerate(habits):
            print(f"-{habit}: do it at {Timing[i]}")
        start_date +=timedelta(days=1)  
        print("---------------------------------------------------")
        print("\n")  
    
        
    
if __name__=="__main__":
    main()