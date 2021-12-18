# A basic code for matrix input from user 

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

# Initialize matrix 
matrix = [] 
count =[]
# For user input 
for i in range(R):
    x=input().split()
    a =[]
    b=[]
    for j in range(C):	 
        a.append(int(x[j]))
        b.append(0)
    matrix.append(a)
    count.append(b)
n=int(input("enter the number of times:"))
# For printing the matrix
for x in range(n):
    print("Iteration:"+" "+str(x)+' ')
    
    for i in range(R):
        for j in range(C):
            count[i][j]=0
            if i>=1 and j>=1:
                if i<R-1 and j<C-1:
                    if(matrix[i+1][j]==1):
                        count[i][j]+=1#down
                    if(matrix[i-1][j]==1):
                        count[i][j]+=1#up^
                    if(matrix[i+1][j-1]==1):
                        count[i][j]+=1#leftdown
                    if(matrix[i-1][j+1]==1):
                        count[i][j]+=1#rightup
                    if(matrix[i-1][j-1]==1):
                        count[i][j]+=1#leftup
                    if(matrix[i+1][j+1]==1):
                        count[i][j]+=1#rytdown
                    if(matrix[i][j-1]==1):
                        count[i][j]+=1#left<-
                    if(matrix[i][j+1]==1):
                        count[i][j]+=1#ryt->
                    print('current postn:'+"("+str(i)+","+str(j)+")"+" "+str(matrix[i][j])+" "+" cost is "+str(count[i][j]))
            if i>=1 and j==0:
                if j==0 and i<R-1:
                    if(matrix[i-1][j]==1):
                        count[i][j]+=1#up^
                    if(matrix[i+1][j]==1):
                        count[i][j]+=1#down
                    if(matrix[i-1][j+1]==1):
                        count[i][j]+=1#rightup
                    if(matrix[i+1][j+1]==1):
                        count[i][j]+=1#rytdown
                    if(matrix[i][j+1]==1):
                        count[i][j]+=1#ryt->
                    print('current postn:'+"("+str(i)+","+str(j)+")"+" "+str(matrix[i][j])+" "+" cost is "+str(count[i][j]))

                        

            if i>=1 and j==C-1 and i<R-1:
                if(matrix[i-1][j]==1):
                    count[i][j]+=1#up^
                if(matrix[i][j-1]==1):
                    count[i][j]+=1#left<-
                if(matrix[i+1][j]==1):
                    count[i][j]+=1#down
                if(matrix[i+1][j-1]==1):
                    count[i][j]+=1#leftdown
                if(matrix[i-1][j-1]==1):
                    count[i][j]+=1#leftup
                print('current postn:'+"("+str(i)+","+str(j)+")"+" "+str(matrix[i][j])+" "+" cost is "+str(count[i][j]))
            if i==0 and j>=1 and j<C-1:
                if(matrix[i][j-1]==1):
                    count[i][j]+=1#left<-
                if(matrix[i][j+1]==1):
                    count[i][j]+=1#ryt->
                if(matrix[i+1][j]==1):
                    count[i][j]+=1#down
                if(matrix[i+1][j+1]==1):
                    count[i][j]+=1#rytdown
                if(matrix[i+1][j-1]==1):
                    count[i][j]+=1#leftdown
                print('current postn:'+"("+str(i)+","+str(j)+")"+" "+str(matrix[i][j])+" "+" cost is "+str(count[i][j]))
                
            if i==R-1 and j>=1 and j<C-1:
                if(matrix[i-1][j]==1):
                    count[i][j]+=1#up^
                if(matrix[i][j-1]==1):
                    count[i][j]+=1#left<-
                if(matrix[i][j+1]==1):
                    count[i][j]+=1#ryt->
                if(matrix[i-1][j+1]==1):
                    count[i][j]+=1#rightup
                if(matrix[i-1][j-1]==1):
                    count[i][j]+=1#leftup
                print('current postn:'+"("+str(i)+","+str(j)+")"+" "+str(matrix[i][j])+" "+" cost is "+str(count[i][j]))
            if i==0 and j==0:
                if(matrix[i][j+1]==1):
                   count[i][j]+=1#ryt->
                if(matrix[i+1][j]==1):
                   count[i][j]+=1#down
                if(matrix[i+1][j+1]==1):
                   count[i][j]+=1#rytdown
                print('current postn:'+"("+str(i)+","+str(j)+")"+" "+str(matrix[i][j])+" "+" cost is "+str(count[i][j]))
            
            if i==0 and j==C-1:
                if(matrix[i][j-1]==1):
                    count[i][j]+=1#left<-
                if(matrix[i+1][j]==1):
                    count[i][j]+=1#down
                if(matrix[i+1][j-1]==1):
                    count[i][j]+=1#leftdown
                print('current postn:'+"("+str(i)+","+str(j)+")"+" "+str(matrix[i][j])+" "+" cost is "+str(count[i][j]))
    
            if i==R-1 and j==C-1:
                if(matrix[i-1][j]==1):
                    count[i][j]+=1#up^
                if(matrix[i][j-1]==1):
                    count[i][j]+=1#left<-
                if(matrix[i-1][j-1]==1):
                    count[i][j]+=1#leftup
                print('current postn:'+"("+str(i)+","+str(j)+")"+" "+str(matrix[i][j])+" "+" cost is "+str(count[i][j]))
            if i==R-1 and j==0:
                if(matrix[i-1][j]==1):
                    count[i][j]+=1#up^
                if(matrix[i-1][j+1]==1):
                    count[i][j]+=1#rightup
                if(matrix[i][j+1]==1):
                    count[i][j]+=1#ryt->
                print('current postn:'+"("+str(i)+","+str(j)+")"+" "+str(matrix[i][j])+" "+" cost is "+str(count[i][j]))
    for i in range(R):
        for j in range(C):
            if(matrix[i][j]==0 and count[i][j]==3):
                matrix[i][j]=1
            if(matrix[i][j]==1 and count[i][j]>3):
                matrix[i][j]=0
            if(matrix[i][j]==1 and count[i][j]<2):
                matrix[i][j]=0
            if((matrix[i][j]==1 and count[i][j]==2) or (matrix[i][j]==1 and count[i][j]==3)):
                matrix[i][j]=1
               
            print(matrix[i][j], end = " ")
        print()
