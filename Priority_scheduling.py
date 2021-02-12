

def findTurnAroundTime(processes, n, bt, wt, tat):
  for i in range(n):
    tat[i]=bt[i]+wt[i]


def findWaitingTime(processes,n,bt,wt):
  wt[0]=0
  for i in range(1,n):
    wt[i] =  bt[i-1] + wt[i-1];

def findavgTime(processes,n,b_t,p_n):

  # Apply Bubble short sorting burst time and process based on short of execution or burst time

 #  sorted burst time according to highest priority
 for i in range(0,n):
   possition=i
   for j in range(i+1,n):
     if(priority_num[j]<priority_num[possition]):
       possition=j
     temp=priority_num[i]
     priority_num[i]=priority_num[possition]
     priority_num[possition]=temp
     temp=b_t[i]
     b_t[i]=b_t[possition]
     b_t[possition]=temp
     temp=processes[i]
     processes[i]=processes[possition]
     processes[possition]=temp



 total_wt=0
 total_tat=0
 wt = [0] * n #initial waiting time
 tat = [0] * n
 findWaitingTime(processes,n,b_t,wt)
 findTurnAroundTime(processes,n,b_t,wt,tat)
 print( "Processes Burst time " + 
                  " priority  Waiting time " + 
                " Turn around time") 
  
    # Calculate total waiting time  
    # and total turn around time 
 for i in range(n): 
      
    total_wt = total_wt + wt[i] 
    total_tat = total_tat + tat[i] 
    print(" "+str(processes[i]) + "\t\t" + 
    str(b_t[i]) + "\t " + str(p_n[i])+ "\t\t"+
    str(wt[i]) + "\t\t " + 
    str(tat[i]))  
  # function of find waiting time around
 print( "Average waiting time = "+
                   str(total_wt / n)) 
  # function of find turn around
 print("Average turn around time = "+
                     str(total_tat / n)) 
  

#  print("Shown sortest burst time:")
#  for i in range(n):
#     print(b_t[i])
 
# main function
if __name__ =="__main__": 
    processes=[]
    n=int(input("Enter number process:"))
      
    for i in range(0,n):
      ele = int(input()) 
      processes.append(ele)
        
    burst_time = [] 
    print("Enter the burst time:")
    for i in range(0,n):
        ele = int(input()) 
        burst_time.append(ele)
   

    print("Enter the priority number:")
    priority_num=[]

    for i in range(0,n):
        ele = int(input()) 
        priority_num.append(ele)
    findavgTime(processes, n, burst_time,priority_num)  


