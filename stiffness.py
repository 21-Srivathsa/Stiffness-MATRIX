import numpy as np

print("@srivathsa")
print("Hello, I will find your total stiffness matrix!!!!\n")

#1

print("What are the labels for first matrix????\n")
label_1=[1,2,3,4]
for i in range(4):
    label_1[i]=(int(input()))
    
print("I am taking EI as a constant, if there is any coefficient for I, then multiply that matrix with the coefficient and feed here!\n")  
print("Enter Matrix 1 elements according to row-wise!\n")   
matrix_1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):           
    for j in range(4):      
         matrix_1[i][j]=float(input())
print(matrix_1)       
       
#1 finished

  


print("What are the labels for second matrix????\n")
label_2=[1,2,3,4]
for i in range(4):
    label_2[i]=(int(input()))

print("Enter Matrix 2 elements according to row-wise!\n")
matrix_2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print("Enter the matrix row-wise:\n")
for i in range(4):           
    for j in range(4):      
         matrix_2[i][j]=float(input()) 
print(matrix_2)  




print("What are the labels for third matrix????\n")
label_3=[1,2,3,4]
for i in range(4):
    label_3[i]=(int(input()))

print("Enter Matrix 3 elements according to row-wise!\n")
matrix_3=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print("Enter the matrix row-wise:\n")
for i in range(4):           
    for j in range(4):      
         matrix_3[i][j]=float(input()) 
print(matrix_3)  





print("What are the labels for fourth matrix????\n")
label_4=[1,2,3,4]
for i in range(4):
    label_4[i]=(int(input()))

print("Enter Matrix 4 elements according to row-wise!\n")
matrix_4=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print("Enter the matrix row-wise:\n")
for i in range(4):           
    for j in range(4):      
         matrix_4[i][j]=float(input()) 
print(matrix_4)  



print("What are the labels for fifth matrix????\n")
label_5=[1,2,3,4]
for i in range(4):
    label_5[i]=(int(input()))

print("Enter Matrix 5 elements according to row-wise!\n")
matrix_5=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print("Enter the matrix row-wise:\n")
for i in range(4):           
    for j in range(4):      
         matrix_5[i][j]=float(input()) 
print(matrix_5)  





print("What are the labels for sixth matrix????\n")
label_6=[1,2,3,4]
for i in range(4):
    label_6[i]=(int(input()))

print("Enter Matrix 6 elements according to row-wise!\n")
matrix_6=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print("Enter the matrix row-wise:\n")
for i in range(4):           
    for j in range(4):      
         matrix_6[i][j]=float(input()) 
print(matrix_6)  




print("What is the size of final matrix?\n")
print("please enter n+1 if the size of the final matrix is n\n")
print("For example, if the order is 8x8, then feed 9\n")  
f=int(input())
final_matrix=np.zeros((f,f))
for i in range(4):
    for j in range(4):
        final_matrix[label_1[i]][label_1[j]]=matrix_1[i][j]            
 #2        
for i in range(4):
    for j in range(4):
        final_matrix[label_2[i]][label_2[j]]=final_matrix[label_2[i]][label_2[j]]+matrix_2[i][j]         
 #2 finished

for i in range(4):
    for j in range(4):
        final_matrix[label_3[i]][label_3[j]]=final_matrix[label_3[i]][label_3[j]]+matrix_3[i][j]   
 
for i in range(4):
    for j in range(4):
        final_matrix[label_4[i]][label_4[j]]=final_matrix[label_4[i]][label_4[j]]+matrix_4[i][j]   


for i in range(4):
    for j in range(4):
        final_matrix[label_5[i]][label_5[j]]=final_matrix[label_5[i]][label_5[j]]+matrix_5[i][j]   


for i in range(4):
    for j in range(4):
        final_matrix[label_6[i]][label_6[j]]=final_matrix[label_6[i]][label_6[j]]+matrix_6[i][j]   










#IF WE NEED MORE MINI-MATRICES THEN COPY THE ABOVE CODE #1 AGAIN AND RENAME 
 #        ELEMENTS AS Matrix_3 AND COPY THE FOR LOOP #2 AGAIN REPLACING WITH Matrix_3
            
 

 # print(final_matrix)       
         
z=f-1

new_matrix=np.zeros((z,z))
for i in range(z):
	for j in range(z):
		new_matrix[i][j]=final_matrix[i+1][j+1]

print("Here we go!!! THE FINAL MATRIX [K]!!\n")
print(new_matrix)
		
#abba sairam pani mugisindi
print("How many un-restrained degrees of freedom are there??\n")
uu=int(input())


Kuu=np.zeros((uu,uu))  
for i in range(uu):
	for j in range(uu):
		Kuu[i][j]=new_matrix[i][j]  

print("The below big matrix is [Kuu] matrix!!!!!!!\n")
print(Kuu)
         
         
         
         
         
         
         
         
         
         
         
         
         