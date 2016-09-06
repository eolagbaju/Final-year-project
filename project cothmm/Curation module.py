
# coding: utf-8

# In[ ]:

import matplotlib.pyplot as plt
import datetime
import csv
import numpy as np
import math
import tkinter 
import tkinter.messagebox
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import os

tl=np.arange(0,6.25,0.25) #x axis for logistic curve

normal_set=[]
abnormal_set=[]
borderline_set=[]
ODV=[] #list for the optical density values
t=[] #list for the time
typ=[] #list for the type
rep=[] #list for the repeat
day=[] #list for the day
plt_row=[] #list for the plate row
plt_col=[] # list for the plate column

with open('C:/Users/user/Documents/project cothmm/colonial_bacteria_data.csv', 'r') as f:#opens the excel document
    reader = csv.reader(f)
    for row in reader:
        typ.append(row[1]) #puts the type into the list typ
        plt_row.append(row[2]) #puts the plate rowinto the list plt_row
        plt_col.append(row[3]) #puts the plate column into the list plt_col
        t.append(row[4]) #puts the time column into the list t  
        day.append(row[5]) #puts day number into the list day
        rep.append(row[6]) #puts repeat number into the list rep
        ODV.append(row[7]) #puts the OD values into the list y

t.remove(t[0]) #removes the time column heading        
sorted_t=[] #list to store the different times listed
seen_times=set()

for i in t:
   if i not in seen_times:
       sorted_t.append(i)
       seen_times.add(i)



dec1=0 #variable to determine the assignment of day 1 repeat 1
dec2=0
dec3=0
dec4=0
dec5=0
dec6=0
dec7=0
dec8=0
dec9=0


        
def promoter_values(typ,rep,ODV,day,des_type): #function to plot the graphs for a specific promoter
    t=np.arange(0,6.25,0.25)
    ROI_ODVs=[] #Optical density values for the region of interest i.e. the promoter
    ROI_days=[]
    ROI_reps=[]
    
    day1_ODV=[]
    rep1=[]
    day2_ODV=[]
    rep2=[]
    day3_ODV=[]
    rep3=[]
    d1r1=[]
    d1r2=[]
    d1r3=[]
    d2r1=[]
    d2r2=[]
    d2r3=[]
    d3r1=[]
    d3r2=[]
    d3r3=[]
    
    indices = [i for i, x in enumerate(typ) if x == des_type] #gets the row index for every row corresponding to the promoter
    for spec in indices: 
        ROI_ODVs.append(ODV[spec]) #gets the corresponding OD value from the row that the promoter was "seen" in
        ROI_days.append(day[spec])
        ROI_reps.append(rep[spec])
    

    
    day1 = [i for i, y in enumerate( ROI_days) if y == '1'] #fills day 1 with the indices corresponding to day 1
    
    day2 = [i for i, z in enumerate( ROI_days) if z == '2']
    
    day3 = [i for i, e in enumerate( ROI_days) if e == '3']
    
    rep1 = [i for i, f in enumerate( ROI_reps) if f == '1']
    
    rep2 = [i for i, g in enumerate( ROI_days) if g == '2']

    rep3 = [i for i, h in enumerate( ROI_days) if h == '3']
   
    for i in day1:
           day1_ODV.append(ROI_ODVs[i])
    for i in day2:
        day2_ODV.append(ROI_ODVs[i])
    for i in day3:
        day3_ODV.append(ROI_ODVs[i])
    d1r1=day1_ODV[0:25]
    d1r2=day1_ODV[25:50]
    d1r3=day1_ODV[50:75]
    d2r1=day2_ODV[0:25]
    d2r2=day2_ODV[25:50]
    d2r3=day2_ODV[50:75]
    d3r1=day3_ODV[0:25]
    d3r2=day3_ODV[25:50]
    d3r3=day3_ODV[50:75]
    
    return (d1r1,d1r2,d1r3,d2r1,d2r2,d2r3,d3r1,d3r2,d3r3,des_type)
    
def promoter_names(typ): #function to check all the different promoters in the file
    promoter_names=[]
    seen_promoters=set()
    for promoter in typ:
        if promoter not in seen_promoters and promoter!="type": #checks if promoter/type had been added and excludes the column header
            promoter_names.append(promoter)
            seen_promoters.add(promoter)
        
    
    return promoter_names


       


def sel(): #function to tell the user what promoter they selected and to display their graphs
    def plot_values(d1r1,d1r2,d1r3,d2r1,d2r2,d2r3,d3r1,d3r2,d3r3,des_type): 
        
        selected_display=int(hours.get())
    
        displaymod=sorted_t
        if selected_display==5:
            displaymod=displaymod[0:21]
          
         
        t=displaymod
        modlength=len(displaymod)
        
        d1r1=d1r1[0:modlength]
        d1r2=d1r2[0:modlength]
        d1r3=d1r3[0:modlength]
        d2r1=d2r1[0:modlength]
        d2r2=d2r2[0:modlength]
        d2r3=d2r3[0:modlength]
        d3r1=d3r1[0:modlength]
        d3r2=d3r2[0:modlength]
        d3r3=d3r3[0:modlength]
        
        f=plt.figure(1)
        f.clear()
        a1=plt.subplot2grid((3,2),(0,0))

        plt.title((des_type)+" : Day 1: Repeats 1-3")
        plt.ylabel('Optical density(OD)')
        a4=plt.subplot2grid((3,2),(1,0))
    
        plt.title((des_type)+" : Day 2: Repeats 1-3")
        plt.ylabel('Optical density(OD)') 
        a7=plt.subplot2grid((3,2),(2,0))
        plt.title((des_type)+ " : Day 3: Repeats 1-3")
        plt.ylabel('Optical density(OD)') 
        plt.xlabel("Time (hours)")
   
        a10=plt.subplot2grid((3,2),(0,1),rowspan=3)
        plt.title((des_type)+ " : Summary")
        plt.ylabel('Optical density(OD)') 
        plt.xlabel("Time (hours)")
        
        
        a1.plot(t,d1r1,'b-',label='repeat 1', linewidth=2)
        a1.legend(loc='upper left')
        
        a1.plot(t,d1r2,'r-',label='repeat 2', linewidth=2) #plots OD against time
       
        a1.legend(loc='upper left')
        
        a1.plot(t,d1r3,'k-',label='repeat 3', linewidth=2)
  
        a1.legend(loc='upper left')


       
        a4.plot(t,d2r1,'b-',label='repeat 1', linewidth=2) #plots OD against time

        a4.legend(loc='upper left')
        
        a4.plot(t,d2r2,'r-',label='repeat 2', linewidth=2)
        
        a4.legend(loc='upper left')  
        
        a4.plot(t,d2r3,'k-',label='repeat 3', linewidth=2)
 
        a4.legend(loc='upper left')


        
        a7.plot(t,d3r1,'b-',label='repeat 1', linewidth=2) #plots OD against time

        a7.legend(loc='upper left')
        
        a7.plot(t,d3r2,'r-',label='repeat 2', linewidth=2)
    
        a7.legend(loc='upper left')

        a7.plot(t,d3r3,'k-',label='repeat 3', linewidth=2)
       
        a7.legend(loc='upper left')
        
        a10.plot(t,d1r1,'b-',label='day 1', linewidth=3)
        a10.legend(loc='upper left')
        a10.plot(t,d1r2,'b-', linewidth=2)
        a10.plot(t,d1r3,'b-', linewidth=2)
        a10.plot(t,d2r1,'r-',label='day 2', linewidth=3)
        a10.legend(loc='upper left')
        a10.plot(t,d2r2,'r-', linewidth=2)
        a10.plot(t,d2r3,'r-', linewidth=2)
        a10.plot(t,d3r1,'k-',label='day 3', linewidth=3)
        a10.legend(loc='upper left')
        a10.plot(t,d3r2,'k-', linewidth=2)
        a10.plot(t,d3r3,'k-', linewidth=2)

        
        
        
        def Training_set_build():

          
            
            def opt11():
                global dec1
                dec1=1
            def opt12():
                global dec1
                dec1=2
            def opt13():
                global dec1
                dec1=3
                
            def opt21():
                global dec2
                dec2=1
            def opt22():
                global dec2
                dec2=2
            def opt23():
                global dec2
                dec2=3
                
            def opt31():
                global dec3
                dec3=1
            def opt32():
                global dec3
                dec3=2
            def opt33():
                global dec3
                dec3=3
        
            def opt41():
                global dec4
                dec4=1
            def opt42():
                global dec4
                dec4=2
            def opt43():
                global dec4
                dec4=3
                
            def opt51():
                global dec5
                dec5=1
            def opt52():
                global dec5
                dec5=2
            def opt53():
                global dec5
                dec5=3
                
            def opt61():
                global dec6
                dec6=1
            def opt62():
                global dec6
                dec6=2
            def opt63():
                global dec6
                dec6=3
                
            def opt71():
                global dec7
                dec7=1
            def opt72():
                global dec7
                dec7=2
            def opt73():
                global dec7
                dec7=3
                
            def opt81():
                global dec8
                dec8=1
            def opt82():
                global dec8
                dec8=2
            def opt83():
                global dec8
                dec8=3
                
            def opt91():
                global dec9
                dec9=1
            def opt92():
                global dec9
                dec9=2
            def opt93():
                global dec9
                dec9=3

                
            
            var1=IntVar()
            var2=IntVar()
            var3=IntVar()
            var4=IntVar()
            var5=IntVar()
            var6=IntVar()
            var7=IntVar()
            var8=IntVar()
            var9=IntVar()

            Label(Assign_frame,text="Assign Day 1 : repeat 1",fg='green',pady=2).grid(row=0,column=0,columnspan=3)
            normal_button1= Radiobutton(Assign_frame, text="normal", selectcolor='yellow',  indicatoron=FALSE,command=opt11, variable=var1,value=1,padx=2,pady=2).grid(row=1,column=0)
            abnormal_button1= Radiobutton(Assign_frame, text="abnormal",selectcolor='yellow',indicatoron=FALSE,command=opt12,variable=var1,value=2,padx=2,pady=2).grid(row=1,column=1)
            borderline_button1= Radiobutton(Assign_frame, text="borderline",selectcolor='yellow',indicatoron=FALSE,command=opt13,variable=var1,value=3,padx=2,pady=2).grid(row=1,column=2)

            Label(Assign_frame,text="Assign Day 1 : repeat 2",fg='green').grid(row=2,column=0,columnspan=3)
            normal_button2= Radiobutton(Assign_frame, text="normal",selectcolor='yellow',indicatoron=FALSE,command=opt21,variable=var2,value=1,padx=2,pady=2).grid(row=3,column=0)
            abnormal_button2= Radiobutton(Assign_frame, text="abnormal",selectcolor='yellow',indicatoron=FALSE,command=opt22,variable=var2,value=2,padx=2,pady=2).grid(row=3,column=1)
            borderline_button2= Radiobutton(Assign_frame, text="borderline",selectcolor='yellow',indicatoron=FALSE,command=opt23,variable=var2,value=3,padx=2,pady=2).grid(row=3,column=2)

            Label(Assign_frame,text="Assign Day 1 : repeat 3",fg='green').grid(row=4,column=0,columnspan=3)
            normal_button3= Radiobutton(Assign_frame, text="normal",selectcolor='yellow',indicatoron=FALSE,command=opt31, variable=var3,value=1,padx=2,pady=2).grid(row=5,column=0)
            abnormal_button3=Radiobutton(Assign_frame, text="abnormal",selectcolor='yellow',indicatoron=FALSE,command=opt32,variable=var3,value=2,padx=2,pady=2).grid(row=5,column=1)
            borderline_button3=Radiobutton(Assign_frame, text="borderline",selectcolor='yellow',indicatoron=FALSE,command=opt33,variable=var3,value=3,padx=2,pady=2).grid(row=5,column=2)

            Label(Assign_frame,text="Assign Day 2 : repeat 1",fg='green').grid(row=6,column=0,columnspan=3)
            normal_button1= Radiobutton(Assign_frame, text="normal",selectcolor='yellow',indicatoron=FALSE,command=opt41,variable=var4,value=1,padx=2,pady=2).grid(row=7,column=0)
            abnormal_button1= Radiobutton(Assign_frame, text="abnormal",selectcolor='yellow',indicatoron=FALSE,command=opt42,variable=var4,value=2,padx=2,pady=2).grid(row=7,column=1)
            borderline_button1= Radiobutton(Assign_frame, text="borderline",selectcolor='yellow',indicatoron=FALSE,command=opt43,variable=var4,value=3,padx=2,pady=2).grid(row=7,column=2)

            Label(Assign_frame,text="Assign Day 2 : repeat 2",fg='green').grid(row=8,column=0,columnspan=3)
            normal_button2= Radiobutton(Assign_frame, text="normal",selectcolor='yellow',indicatoron=FALSE,command=opt51,variable=var5,value=1,padx=2,pady=2).grid(row=9,column=0)
            abnormal_button2= Radiobutton(Assign_frame, text="abnormal",selectcolor='yellow',indicatoron=FALSE,command=opt52,variable=var5,value=2,padx=2,pady=2).grid(row=9,column=1)
            borderline_button2= Radiobutton(Assign_frame, text="borderline",selectcolor='yellow',indicatoron=FALSE,command=opt53,variable=var5,value=3,padx=2,pady=2).grid(row=9,column=2)

            Label(Assign_frame,text="Assign Day 2 : repeat 3",fg='green').grid(row=10,column=0,columnspan=3)
            normal_button3= Radiobutton(Assign_frame, text="normal",selectcolor='yellow',indicatoron=FALSE,command=opt61,variable=var6,value=1,padx=2,pady=2).grid(row=11,column=0)
            abnormal_button3=Radiobutton(Assign_frame, text="abnormal",selectcolor='yellow',indicatoron=FALSE,command=opt62,variable=var6,value=2,padx=2,pady=2).grid(row=11,column=1)
            borderline_button3=Radiobutton(Assign_frame, text="borderline",selectcolor='yellow',indicatoron=FALSE,command=opt63,variable=var6,value=3,padx=2,pady=2).grid(row=11,column=2)

            Label(Assign_frame,text="Assign Day 3 : repeat 1",fg='green').grid(row=13,column=0,columnspan=3)
            normal_button1= Radiobutton(Assign_frame, text="normal",selectcolor='yellow',indicatoron=FALSE,command=opt71,variable=var7,value=1,padx=2,pady=2).grid(row=14,column=0)
            abnormal_button1= Radiobutton(Assign_frame, text="abnormal",selectcolor='yellow',indicatoron=FALSE,command=opt72,variable=var7,value=2,padx=2,pady=2).grid(row=14,column=1)
            borderline_button1= Radiobutton(Assign_frame, text="borderline",selectcolor='yellow',indicatoron=FALSE,command=opt73,variable=var7,value=3,padx=2,pady=2).grid(row=14,column=2)

            Label(Assign_frame,text="Assign Day 3 : repeat 2",fg='green').grid(row=15,column=0,columnspan=3)
            normal_button2= Radiobutton(Assign_frame, text="normal",selectcolor='yellow',indicatoron=FALSE,command=opt81,variable=var8,value=1,padx=2,pady=2).grid(row=16,column=0)
            abnormal_button2= Radiobutton(Assign_frame, text="abnormal",selectcolor='yellow',indicatoron=FALSE,command=opt82,variable=var8,value=2,padx=2,pady=2).grid(row=16,column=1)
            borderline_button2= Radiobutton(Assign_frame, text="borderline",selectcolor='yellow',indicatoron=FALSE,command=opt83,variable=var8,value=3,padx=2,pady=2).grid(row=16,column=2)

            Label(Assign_frame,text="Assign Day 3 : repeat 3",fg='green').grid(row=17,column=0,columnspan=3)
            normal_button3= Radiobutton(Assign_frame, text="normal",selectcolor='yellow',indicatoron=FALSE,command=opt91,variable=var9,value=1,padx=2,pady=2).grid(row=18,column=0)
            abnormal_button3=Radiobutton(Assign_frame, text="abnormal",selectcolor='yellow',indicatoron=FALSE,command=opt92,variable=var9,value=2,padx=2,pady=2).grid(row=18,column=1)
            borderline_button3=Radiobutton(Assign_frame, text="borderline",selectcolor='yellow',indicatoron=FALSE,command=opt93,variable=var9,value=3,padx=2,pady=2).grid(row=18,column=2)

        def add_data():
            
            
           
            
        
            assignment1="Unassigned"
            label1="unlabeled"
            if dec1==1:
                assignment1="Normal"
                label1='Normal'
            if dec1==2:    
                assignment1="Abnormal"
                label1='Abnormal'
            if dec1==3:   
                assignment1="Borderline"
                label1='Borderline'
                
            assignment2="Unassigned"
            label2="unlabeled"
            if dec2==1:
                assignment2="Normal"
                label2='Normal'
            if dec2==2:    
                assignment2="Abnormal"
                label2='Abnormal'
            if dec2==3:   
                assignment2="Borderline"
                label2='Borderline'
                
            assignment3="Unassigned"
            label3="unlabeled"
            if dec3==1:
                assignment3="Normal"
                label3='Normal'
            if dec3==2:    
                assignment3="Abnormal"
                label3='Abnormal'
            if dec3==3:   
                assignment3="Borderline"
                label3='Borderline'
                
            assignment4="Unassigned"
            label4="unlabeled"
            if dec4==1:
                assignment4="Normal"
                label4='Normal'
            if dec4==2:    
                assignment4="Abnormal"
                label4='Abnormal'
            if dec4==3:   
                assignment4="Borderline"
                label4='Borderline'
                
            assignment5="Unassigned"
            label5="unlabeled"
            if dec5==1:
                assignment5="Normal"
                label5='Normal'
            if dec5==2:    
                assignment5="Abnormal"
                label5='Abnormal'
            if dec5==3:   
                assignment5="Borderline"
                label5='Borderline'
                
            assignment6="Unassigned"
            label6="unlabeled"
            if dec6==1:
                assignment6="Normal"
                label6='Normal'
            if dec6==2:    
                assignment6="Abnormal"
                label6='Abnormal'
            if dec6==3:   
                assignment6="Borderline"
                label6='Borderline'
                
            assignment7="Unassigned"
            label7="unlabeled"
            if dec7==1:
                assignment7="Normal"
                label7='Normal'
            if dec7==2:    
                assignment7="Abnormal"
                label7='Abnormal'
            if dec7==3:   
                assignment7="Borderline"
                label7='Borderline'
                
            assignment8="Unassigned"
            label8="unlabeled"
            if dec8==1:
                assignment8="Normal"
                label8='Normal'
            if dec8==2:    
                assignment8="Abnormal"
                label8='Abnormal'
            if dec8==3:   
                assignment8="Borderline"
                label8='Borderline'
                
            assignment9="Unassigned"
            label9="unlabeled"
            if dec9==1:
                assignment9="Normal"
                label9='Normal'
            if dec9==2:    
                assignment9="Abnormal"
                label9='Abnormal'
            if dec9==3:   
                assignment9="Borderline"
                label9='Borderline'
             
          

            Curator=name.get() 
            
            expo_next_line1=[Curator, "Emancoli Sorting software", str(now.day) +"/" + str(now.month) + "/" + str(now.year),
                              str(now.hour) +":" + str(now.minute) + ":" + str(now.second),des_type ]
            expo_next_line1.append(label1)
            expo_next_line1.append(1)
            expo_next_line1.append(1)
            
            expo_next_line2=[Curator, "Emancoli Sorting software", str(now.day) +"/" + str(now.month) + "/" + str(now.year),
                              str(now.hour) +":" + str(now.minute) + ":" + str(now.second),des_type ]
            expo_next_line2.append(label2)
            expo_next_line2.append(1)
            expo_next_line2.append(2)
            
            expo_next_line3=[Curator, "Emancoli Sorting software", str(now.day) +"/" + str(now.month) + "/" + str(now.year),
                              str(now.hour) +":" + str(now.minute) + ":" + str(now.second),des_type ]
            expo_next_line3.append(label3)
            expo_next_line3.append(1)
            expo_next_line3.append(3)
            
            expo_next_line4=[Curator, "Emancoli Sorting software", str(now.day) +"/" + str(now.month) + "/" + str(now.year),
                              str(now.hour) +":" + str(now.minute) + ":" + str(now.second),des_type ]
            expo_next_line4.append(label4)
            expo_next_line4.append(2)
            expo_next_line4.append(1)
            
            expo_next_line5=[Curator, "Emancoli Sorting software", str(now.day) +"/" + str(now.month) + "/" + str(now.year),
                              str(now.hour) +":" + str(now.minute) + ":" + str(now.second),des_type ]
            expo_next_line5.append(label5)
            expo_next_line5.append(2)
            expo_next_line5.append(2)
            
            expo_next_line6=[Curator, "Emancoli Sorting software", str(now.day) +"/" + str(now.month) + "/" + str(now.year),
                              str(now.hour) +":" + str(now.minute) + ":" + str(now.second),des_type ]
            expo_next_line6.append(label6)
            expo_next_line6.append(2)
            expo_next_line6.append(3)
            
            expo_next_line7=[Curator, "Emancoli Sorting software", str(now.day) +"/" + str(now.month) + "/" + str(now.year),
                              str(now.hour) +":" + str(now.minute) + ":" + str(now.second),des_type ]
            expo_next_line7.append(label7)
            expo_next_line7.append(3)
            expo_next_line7.append(1)
            
            expo_next_line8=[Curator, "Emancoli Sorting software", str(now.day) +"/" + str(now.month) + "/" + str(now.year),
                              str(now.hour) +":" + str(now.minute) + ":" + str(now.second),des_type ]
            expo_next_line8.append(label8)
            expo_next_line8.append(3)
            expo_next_line8.append(2)
            
            expo_next_line9=[Curator, "Emancoli Sorting software", str(now.day) +"/" + str(now.month) + "/" + str(now.year),
                              str(now.hour) +":" + str(now.minute) + ":" + str(now.second),des_type ]
            expo_next_line9.append(label9)
            expo_next_line9.append(3)
            expo_next_line9.append(3)
            
            print(expo_next_line2)
            
            for i in d1r1:
                expo_next_line1.append(i)
                
            for i in d1r2:
                expo_next_line2.append(i)
                
            for i in d1r3:
                expo_next_line3.append(i)
                
            for i in d2r1:
                expo_next_line4.append(i)
            
            for i in d2r2:
                expo_next_line5.append(i)
                
            for i in d2r3:
                expo_next_line6.append(i)
                
            for i in d3r1:
                expo_next_line7.append(i)
                
            for i in d3r2:
                expo_next_line8.append(i)
                
            for i in d3r3:
                expo_next_line9.append(i)
                


            expodat.append(expo_next_line1)
            expodat.append(expo_next_line2)
            expodat.append(expo_next_line3)
            expodat.append(expo_next_line4)
            expodat.append(expo_next_line5)
            expodat.append(expo_next_line6)
            expodat.append(expo_next_line7)
            expodat.append(expo_next_line8)
            expodat.append(expo_next_line9)            
            
            
            
            
            
        def submit():
                if dec1==1:
                    normal_set.append(d1r1)
                if dec1==2:
                    abnormal_set.append(d1r1)
                if dec1==3:
                    borderline_set.append(d1r1)

                if dec2==1:
                    normal_set.append(d1r2)
                if dec2==2:
                    abnormal_set.append(d1r2)
                if dec2==3:
                    borderline_set.append(d1r2)

                if dec3==1:
                    normal_set.append(d1r3)
                if dec3==2:
                    abnormal_set.append(d1r3)
                if dec3==3:
                    borderline_set.append(d1r3)

                if dec4==1:
                    normal_set.append(d2r1)
                if dec4==2:
                    abnormal_set.append(d2r1)
                if dec4==3:
                    borderline_set.append(d2r1)

                if dec5==1:
                    normal_set.append(d2r2)
                if dec5==2:
                    abnormal_set.append(d2r2)
                if dec5==3:
                    borderline_set.append(d2r2)

                if dec6==1:
                    normal_set.append(d2r3)
                if dec6==2:
                    abnormal_set.append(d2r3)
                if dec6==3:
                    borderline_set.append(d2r3)

                if dec7==1:
                    normal_set.append(d3r1)
                if dec7==2:
                    abnormal_set.append(d3r1)
                if dec7==3:
                    borderline_set.append(d3r1)

                if dec8==1:
                    normal_set.append(d3r2)
                if dec8==2:
                    abnormal_set.append(d3r2)
                if dec8==3:
                    borderline_set.append(d3r2)

                if dec9==1:
                    normal_set.append(d3r3)
                if dec9==2:
                    abnormal_set.append(d3r3)
                if dec9==3:
                    borderline_set.append(d3r3)
                    
                
                
        def clear_canvas():
             canvas.get_tk_widget().destroy()
             canvas.get_tk_widget().delete("all")
             canvas.tkcanvas.destroy()
             canvas.tkcanvas.delete("all")   
             
        
        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func


        submit= Button(Assign_frame, text="Submit results",command=combine_funcs(submit,add_data,clear_canvas),pady=5,bd=4, bg='red').grid(row=19,column=1)
    

        canvas = FigureCanvasTkAgg(f,master=Graph_frame)
        canvas.show()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        build=Training_set_build()

    

    
    d1r1,d1r2,d1r3,d2r1,d2r2,d2r3,d3r1,d3r2,d3r3,des_type=promoter_values(typ,rep,ODV,day,var.get())
    plot_values(d1r1,d1r2,d1r3,d2r1,d2r2,d2r3,d3r1,d3r2,d3r3,des_type)

def export_data():
    hrnb=hours.get()
    header= "Training_data_" +hrnb + "hrs" + ".csv"  
    with open(header, 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        data = expodat

        a.writerows(data)



root = Tk()
root.title("Build training data")
select_frame = Frame(root,padx=3,pady=3,bd=5,bg='grey')
Graph_frame=Frame(root)
select_frame.pack(side=LEFT,fill='y')
Graph_frame.pack(side=LEFT,fill=BOTH,expand=1)
Right_frame=Frame(root,padx=3,pady=5,bd=5,bg='grey')
Right_frame.pack(side='right',fill='y')
Assign_frame=Frame(Right_frame,padx=3,bd=5)
Assign_frame.pack(side='bottom')
Name_frame=Frame(select_frame)
Name_frame.pack(side=TOP)
Label(Name_frame,text="Enter your name:").pack(side=TOP)
Export_frame=Frame(select_frame)
Export_frame.pack(side=BOTTOM)
Export= Button(Export_frame, text="Export data as csv",command=export_data,pady=5,bd=4,fg='white', bg='black')
Export.pack(side=BOTTOM)
       
Hours_frame=Frame(Right_frame,padx=3,pady=5,bd=5)
Hours_frame.pack(side=TOP)
Label(Hours_frame,text="Choose the number of hours you wish to be displayed:\n Enter 5 for 0-5hrs\n Enter 6 for 0-6hrs\n This field must be filled in before selecting a promoter!").pack(side=TOP)
hours=Entry(Hours_frame)
hours.pack()
    


var = StringVar()

name=Entry(Name_frame)
name.pack(pady=10)
madeby= "Software:"

Curated_by="Curated by:  "
now = datetime.datetime.now()
date = "Date:  " 
time = "Time:  " 
column_heading=["Time(hrs)","Optical Density"]
Time_heading="Time(hrs)"
OD_heading="Optical Density"

expotit=[Curated_by, madeby,date, time,"Promoter: ","Assignment:" ,"Day:", "Repeat:" ]

title_addition=sorted_t
for i in sorted_t:
    i="OD at time: " +str(i)+"hrs"
    expotit.append(i)

expodat=[expotit]

promoter_list=promoter_names(typ) 
pri=0
for promoter in promoter_list:
    Radiobutton(select_frame, text=promoter, variable=var, command=sel, indicatoron=FALSE, value=promoter, justify=LEFT,padx=6,pady=6,bd=2, relief=RAISED).pack(side=TOP)  
    pri+=1



label = Label(root)
label.pack()
root.mainloop()



# In[ ]:




# In[ ]:



