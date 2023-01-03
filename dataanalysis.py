# importing all the required python libraries
import pandas as pd 
import matplotlib.pyplot as mpy
import numpy as np
df=pd.read_csv("C:\\Users\\Rakshit\\Desktop\\keya\\covi
d cases.csv")
print()
print()
#defining column names
st=df['STATES']
tc=df['TOTAL CASES']
ac=df['ACTIVE CASES']
d=df['DEATHS']
r=df['RECOVERED']
#submenu 2 for covid cases visualisation
def submenu2():
 ch=0
 while ch!=4:
 
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^")
 print(" DATA VISUALISATION MENU:- ")
 
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^")
 print("1.line graph")
 print("2.Bar graph")
 print("3. Histogram")
 print("4.Back to menu") 
 ch=int(input("choose the option:"))
 if ch==1:
 mpy.subplot(4,1,1)
 mpy.plot(st,tc,label="TOTAL 
CASES",color="yellow",linestyle="dashed")
 mpy.legend()
 mpy.grid()
 mpy.title("COVID CASES:-")
 mpy.subplots_adjust(hspace=0.75,wspace=0.50)
 
 mpy.subplot(4,1,2)
 mpy.plot(st,ac,label="ACTIVE 
CASES",color="k",linestyle="--")
 mpy.legend()
 mpy.grid()
 mpy.subplots_adjust(hspace=0.75,wspace=0.50)
 
 
 mpy.subplot(4,1,3)
 
mpy.plot(st,r,label="RECOVERD",color="magenta",linestyle="-
.")
 mpy.legend()
 mpy.grid()
 mpy.subplots_adjust(hspace=0.75,wspace=0.50)
 
 
 mpy.subplot(4,1,4)
 
mpy.plot(st,d,label="DEATHS",color="blue",linestyle=":")
 mpy.xticks(np.arange(0,36,1),fontsize=10,rotation=90)
 mpy.legend()
 mpy.grid()
 mpy.subplots_adjust(hspace=0.75,wspace=0.50)
 mpy.show()
 
 elif ch==2:
 mpy.bar(st,tc,color="pink",label="TOTAL CASES")
 mpy.bar(st,ac,label="ACTIVE CASES",color="blue")
 mpy.bar(st,r,label="RECOVERED",color="yellow")
 mpy.bar(st,d,label="DEATHS",color="brown")
 mpy.xlabel("STATES")
 mpy.ylabel=("CASES")
 mpy.xticks(np.arange(0,36,1),fontsize=12,rotation=90)
 
mpy.yticks(np.arange(500,100000,10000),fontsize=30,rotation=90
)
 mpy.title("CASES PER STATES:-")
 mpy.legend()
 mpy.show()
 elif ch==3:
 
mpy.hist([tc,ac],bins=4,histtype="barstacked",edgecolor="k")
 mpy.show()
 elif ch==4:
 print("Back to main menu")
 
# submenu3 for covid data analysis
def submenu3():
 ch1=0
 while ch1!=4:
 
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
")
 print(" DATA ANALYSIS MENU:- ")
 
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ")
 print("1. Find the Maximum, Minimum, Mean, Sum ofTOTAL CASES,ACTIVE CASES,DEATHS AND 
RECOVERIES:-")
 print("2. Display the details of state having highest cases:-")
 print("3. Display the details of state having lowest cases:-" )
 print("4. Back to the main menu:-")
 ch1=int(input("\nChoose a Option for Data Analysis:"))
 if ch1==1:
 print("Maximum, Minimum,Mean, Sum 0f tc,ac,d,r")
 print(df.aggregate({'TOTAL 
CASES':['max','min','mean','sum'],'ACTIVE 
CASES':['max','min','mean','sum'],'DEATHS':['max','min','mean',
'sum'],'RECOVERED':['max','min','mean','sum']}))
 if ch1==2:
 print("Details of state having highest cases")
 print(df.sort_values("TOTAL 
CASES",ascending=False).head(3))
 elif ch1==3:
 print("Details of state having lowest cases")
 print(df.sort_values("TOTAL 
CASES",ascending=False).tail(3))
 elif ch1==4:
 mainmenu()
 
# main menu conataining calls for submenu2 and
# submenu3 for visualisation and analysis respectively 
 
def mainmenu():
 choice=0
 while choice!=4:
 print("\n*******************************************")
 print(" COVID ANALYSIS:- ")
 print("\n********************************************")
 print(" 1. Covid Cases Data")
 print(" 2. Data Visualisation")
 print(" 3. Data Ananlysis")
 print(" 4. exit the program")
 choice=int(input("choose the option:"))
 if choice ==1:
 print("covid cases data:-")
 print()
 print()
 print(df)
 print()
 print()
 print("end of the data:-")
 elif choice==2:
 submenu2()
 elif choice==3:
 submenu3()
 else:
 print("bye")
 
 
mainmenu()
