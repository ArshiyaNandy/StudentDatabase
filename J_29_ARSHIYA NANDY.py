#STUDENTdatabase
import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#import pandas as pd

def update1():
          file=open('student.csv', 'w', newline='') 
          writer = csv.writer(file)
          n=int(input("How many records "))
          for i in range(n):
                    sid=input("Enter Student ID ")
                    name=input("Enter name ");
                    roll=int(input("Class roll no "))
                    batch=input("Enter Batch name ")
                    marks=int(input("Input marks "))
                    writer.writerow([sid,name,roll,batch,marks])
          file.close()
def remove1():
             k=list()
             file=open('student.csv', 'r')
             reader = csv.reader(file)
             r=input("Enter Student ID to delete ")
             for row in reader:
                   k.append(row)

             file.close()     
             print("Before delete.......")
             print(k)
             for i in k:
                   if i[0]==r:
                        k.remove(i)

             file=open('student.csv', 'w', newline='') 
             writer = csv.writer(file)
             for i in k:
                    writer.writerow(i)
             file.close()
           
def report1():
      p=[]
      file=open('student.csv', 'r')
      reader = csv.reader(file)
      for i in reader:
                  m=int(i[4])
                  if m>=90:
                       g="A"
                  elif m>=80:
                       g="B"
                  elif m>=70:
                       g="C"
                  elif m>60:
                       g="D"
                  elif m>=50:
                       g="E"
                  elif m>=0 and m<50:
                       g="F"
                  else:
                       g="Invalid"
                  p.append([i[0],i[1],i[2],i[3],i[4],g])

      print (p)           
      f=open('report.txt', 'w')
      for i in p:
            f.writelines(i)
                     
      print("Student ID\tname\troll\tbatch\tmarks\tgrade")
      print("=============================================")
      for i in p:
                     print(i[0],"\t\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5])

def create2():
                     file=open('course.csv', 'w', newline='')
                     writer = csv.writer(file)
                     n=int(input("How many records "))
                     for i in range(n):
                           cid=input("Enter Course ID ")
                           cname=input("Course name ")
                           sname=input("Student name ")
                           roll=input("Class roll no ")
                           marks=int(input("Input marks "))
                           x=[sname,marks]
                           di[roll]=x
                           writer.writerow([cid,cname,roll,di[roll]])
def performance2():
      k=[]
      f=0
      file=open('course.csv', 'r') 
      reader = csv.reader(file)
      for row in reader:
                   k.append(row)

      a=b=c=d=e=f=0
      for i in k:
             print(i)
             marks=i[4]
             if marks>=90:
                                a=a+1
                                g="A"
             elif marks>=80:
                                b=b+1
                                g="B"
             elif m>=70:
                                 c=c+1
                                 g="C"
             elif m>=60:
                                 d=d+1
                                 g="D"
             elif m>=50:
                                 e=e+1
                                 g="E"
             elif m>=0 and m<50:
                                 f=f+1
                                 g="F"
             else:
                                print("Invalid")
             print(i[2]," ",i," ",m," ",g)
            
def statistics2():
           print("Show course statistics")
           stat = pd.read_csv("course.csv")
           stat.describe()
def histogram2():
       print("Histogram showing number of students in each grade...")

       marks= [62, 50,90, 55, 92, 80, 84, 88, 98, 54, 72, 60,68, 94, 77, 86, 92, 32, 65, 86, 95]

       bins=[30,40,50,60,70,80,90,100]

       plt.hist(marks, bins, histtype='bar', rwidth=0.8)

plt.show()


def create3():
      file=open('batch.csv', 'a', newline='') 
      writer = csv.writer(file)
      n=int(input("How many records "))
      for i in range(n):
                bid=input("Enter Batch ID ")
                bname=input("Enter Batch name ")
                dept=input("Enter Dept name ")
                course=input("Enter list of courses ")
                slist=input("Enter list of students ")
                writer.writerow([bid,bname,dept,course,slist])

def liststudents3():
      k=[]
      f=0
      file=open('batch.csv', 'r') 
      reader = csv.reader(file)
      b=input("Enter Batch name to display list of students ")
      for row in reader:
                   k.append(row)
                   
      for i in k:
            if i[1]==b:
                        print(i[4])
                        f=7
      if f==0:
                   print("Batch name not exists !!!!!!!!!")

def listcourses3():
      k=[]
      f=0
      file=open('batch.csv', 'r') 
      reader = csv.reader(file)
      b=input("Enter Batch name to display courses ")
      for row in reader:
                   k.append(row)
                   
      for i in k:
             if i[1]==b:
                        print(i[3])
                        f=7
             if f==0:
                   print("Batch name not exists !!!!!!!!!")
     
def performance3():
      k=[]
      print("Batch ID\tBatch name\tDepartment name\tList of Courses\tList of Students")
      print("===========================================================")
      with open('batch.csv', 'r') as file:
             reader = csv.reader(file)
             for row in reader:
                   k.append(row)
                   
             for i in k:
                   print(i[0],"\t",i[1],"\t",i[2],"\t\t",i[3],"\t",i[4])

def piechart3():
       print()
       y = np.array([3, 2, 4, 5,0,1])
       mylabels = ["A", "B", "C", "D","E","F"]
       plt.pie(y, labels = mylabels)
       plt.show() 


def create4():
     with open('department.csv', 'w', newline='') as file:
           writer = csv.writer(file)
           n=int(input("How many records "))
           for i in range(n):
                did=input("Enter Deparment ID ")
                dname=input("Enter Department name ")
                batches=input("Enter list of batches ")
                writer.writerow([did,dname,batches])

def viewbatches4():
      k=[]
      f=0
      with open('department.csv', 'r') as file:
             reader = csv.reader(file)
             d=input("Enter Department name to display batches.. ")
             for row in reader:
                   k.append(row)
                   
             for i in k:
                   if i[1]==d:
                        print(i[2])
                        f=7
             if f==0:
                   print("Department name not exists !!!!!!!!!")



def performance4():
      k=[]
      f=0
      with open('department.csv', 'r') as file:
             reader = csv.reader(file)
             d=input("Enter Department name to display average performance ")
             for row in reader:
                   k.append(row)
                   
             for i in k:
                   if i[1]==d:
                        print(i[2])
                        f=7
             if f==0:
                   print("Department name not exists !!!!!!!!!")

def create5():
     with open('examination.csv', 'a', newline='') as file:
           writer = csv.writer(file)
           n=int(input("How many records "))
           for i in range(n):
                bid=input("Enter Batch ID ")
                bname=input("Enter Batch name ")
                dept=input("Enter Dept name ")
                course=input("Enter list of courses ")
                slist=input("Enter list of students ")
                writer.writerow([bid,bname,dept,course,slist])

def performance5():
        file=open('batch.csv', 'r')
        reader = csv.reader(file)
        b=input("Enter Batch name to display courses ")
        for row in reader:
              print(row)

def scattered5():
     x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
     y = [99,86,87,88,86,100,87,94,78,77,85,86,0]
     plt.scatter(x, y)
     plt.show()
    

print("S T U D E N T  E X A M I N A T I O N  P O R T A L")
print("=========================================")

ch=0
while ch !=6:
               print()
               print("1. STUDENT MODULE...")
               print("2. COURSE MODULE...")
               print("3. BATCH MODULE..")
               print("4. DEPARTMENT MODULE...")
               print("5. EXAMINATION MODULE..")
               print("6. E x i t from Portal")
               print("--------------------------------")
               ch=int(input("Enter your choice "))
               if ch==1:
                     c=0
                     while c !=4:
                             print()
                             print("=================")
                             print("Student M e n u")
                             print("=================")
                             print("1. Update...")
                             print("2. Remove a student from database...")
                             print("3. Generate report card..")
                             print("4. E x i t from Student")
                             print("--------------------------------")
                             c=int(input("Enter your choice "))
                             if c==1:
                                  update1()
                             elif c==2:
                                  remove1()
                             elif c==3:
                                   report1()
                             elif c==4:
                                  break
                             else:
                                  print("Wrong choice !!!!")
               elif ch==2:
                     di={}
                     a=b=c=d=e=f=g=0
                     c=0
                     while c !=5:
                             print()
                             print("=================")
                             print("Create new course M e n u")
                             print("=================")
                             print("1. Create a new course ...")
                             print("2. View performance of all students...")
                             print("3. Show course Statistics")
                             print("4. Histogram")
                             print("5. E x i t from Course Module")
                             print("--------------------------------")
                             c=int(input("Enter your choice "))
                             if c==1:
                                  create2()
                             elif c==2:
                                   performance2()
                             elif c==3:
                                   statistics2()
                             elif c==4:
                                   histogram2()
                             elif c==5:
                                  break
                             else:
                                  print("Wrong choice !!!!")
                     

               elif ch==3:
                         c=0
                         while c !=6:
                                print()
                                print("=================")
                                print("Batch M e n u")
                                print("=================")
                                print("1. Create Batch...")
                                print("2. List all students of a batch...")
                                print("3. List of all courses in a batch..")
                                print("4. List complete performance off all students in a batch..")
                                print("5.Pie chart of performance of all students..");
                                print("6. E x i t from Batch module")
                                print("--------------------------------")
                                c=int(input("Enter your choice "))
                                if c==1:
                                     create3()
                                elif c==2:
                                     liststudents3()
                                elif c==3:
                                     listcourses3()
                                elif c==4:
                                     performance3()
                                elif c==5:
                                     piechart3()
                                elif c==6:
                                     break
                                else:
                                     print("Wrong choice !!!!")
               elif ch==4:
                             c=0
                             while c !=4:
                                    print()
                                    print("=================")
                                    print("Department M e n u")
                                    print("=================")
                                    print("1. Create Department...")
                                    print("2. View all batches in a department...")
                                    print("3. View average performance off all batches in a dept...")
                                    print("4. E x i t from Department module")
                                    print("--------------------------------")
                                    c=int(input("Enter your choice "))
                                    if c==1:
                                          create4()
                                    elif c==2:
                                         viewbatches4()
                                    elif c==3:
                                        performance4()
                                    elif c==4:
                                        break
                                    else:
                                        print("Wrong choice !!!!")
               elif ch==5:
                         c=0
                         while c !=5:
                                print()
                                print("=================")
                                print("Examination M e n u")
                                print("=================")
                                print("1. Enter marks of all students of a specific Examination...")
                                print("2. View performance of all students in the examination...")
                                print("3. Show examination statistics..")
                                print("4. Scattered Plot of all marks..")
                                print("5. E x i t from Examination module")
                                print("--------------------------------")
                                c=int(input("Enter your choice "))
                                if c==1:
                                     create5()
                                elif c==2:
                                     performance5()
                                elif c==3:
                                     examstat5()
                                elif c==4:
                                     scattered5()
                                elif c==5:
                                     break
                                else:
                                     print("Wrong choice !!!!")

               elif ch==6:
                   break
               else:
                   print("Wrong choice !!!!!!!")
