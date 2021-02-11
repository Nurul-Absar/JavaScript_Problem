##For this FCFS Calculation  i take all arrival time are 0 or same

def findWaitingTime(processes,n,bt,wt):
  wt[0]=0
  for i in range(1,n):
    wt[i] =  bt[i-1] + wt[i-1];


def findTurnAroundTime(processes, n, bt, wt, tat):
  for i in range(n):
    tat[i]=bt[i]+wt[i]
 
#Calculate Average Waiting and Turn Arround Time
def findavgTime(processes,n,bt):
  total_wt=0
  total_tat=0
  wt = [0] * n #initial waiting time
  tat = [0] * n  #initial turn Arround time
  # function to find waiting time of all processes
  findWaitingTime(processes, n, bt, wt)

 
    # function to find turn around time for all processes
  findTurnAroundTime(processes, n, bt, wt, tat)
  # display processes along with all details
  print( "Processes Burst time " + 
                  " Waiting time " + 
                " Turn around time") 
  
    # Calculate total waiting time  
    # and total turn around time 
  for i in range(n): 
      
    total_wt = total_wt + wt[i] 
    total_tat = total_tat + tat[i] 
    print(" "+str(i + 1) + "\t\t" + 
    str(bt[i]) + "\t " + 
    str(wt[i]) + "\t\t " + 
    str(tat[i]))  
  
  print( "Average waiting time = "+
                   str(total_wt / n)) 
  print("Average turn around time = "+
                     str(total_tat / n)) 
  


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
    findavgTime(processes, n, burst_time)  