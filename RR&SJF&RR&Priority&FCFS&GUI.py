import numpy
import  matplotlib
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import matplotlib
import matplotlib.pyplot as plt
from decimal import *
import math
import copy
getcontext().prec = 3
minimalResolution = Decimal(0.1)
waitingtime={}
HighestPrior = 9999999999999999999999999999999
ProccessNumber = -1
MinimumProcessArrivalTime = 99999999999999999999999999999
j = 0
Time=0
PAV = []
Position = 0
arrivaldict={}
durationdict={}
prioritydict = {}
#****** Mira's global variables *******
ProcessedProcess = []
ProcessedTime = []
ProcessStartTime=[]
max = 0
element = 0
global Emptive
from decimal import *
getcontext().prec = 3

minimalResolution = Decimal(0.1)


class Process:

    def __init__(self, name, arrival, remaining):
        self.name = name
        self.arrival = Decimal(arrival)
        self.remaining = Decimal(remaining)
        self.burst = Decimal(remaining)
    def do_process(self):
        if (round(self.remaining,1) == Decimal(0)):
            return None
        else:
            self.remaining -= Decimal(minimalResolution)
            if (round(self.remaining,1) == -Decimal(0)):
                return None
            else:
                return self.remaining

    def status(self):
        return "Name : {}, arrival: {}, remaining : {}".format(self.name, self.arrival, self.remaining)



def FCFS ():
    global Time
    global max
    global element
    global waitingtime
    max = float(arrivaldict[0])
    flag = 0

    for i in range(int(numberOfProcesses) ):
        if (float(arrivaldict[i]) > max):
                max = float(arrivaldict[i])

    while 1 :
        for i in range(int(numberOfProcesses)):
            if (float(arrivaldict[i]) <= Time) and (float(durationdict[i]) != 0) and (
                        float(arrivaldict[i]) < int(max) + 1):
                ProcessStartTime.append(Time)
                Time = Time + float(durationdict[i])
                waitingtime[i]= Time-float(durationdict[i])-float(arrivaldict[i])
                ProcessedProcess.append('P'+str(i))
                ProcessedTime.append(durationdict[i])
                durationdict[i] = 0
                element = element + 1
                flag=1
            else :
                flag=0
        if (flag == 0):
            Time = Time + 0.01
        if element == int(numberOfProcesses) :
            break
    print(waitingtime)
def PR():

    if Emptive.get()=='Non-Preemptive':
            Scheduler()
    if Emptive.get()=='Pre-Emptive':
            PreScheduler()




def checkRR():
    global root5
    global Quantum
    flag = 1
    temp3 = Quantum.get()
    try:
        qq= float(temp3)
        if(qq==0):
            kinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
            return

    except:
        flag = 0
        tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
        return
    for i in range(int(numberOfProcesses)):
        temp = arrivaldict[i].get()
        temp2 = durationdict[i].get()
        try:
            float(temp)
            float(temp2)
            if float(temp2)==0 :
                flag=0
                tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
                break
        except:
            tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
            flag = 0
            break
        arrivaldict[i] = temp
        durationdict[i] = temp2

    if (flag == 1):
        RR(qq)
        Draw()
        #root5.destroy()
def checkFCFS():
    global root2
    flag = 1
    for i in range(int(numberOfProcesses)):
        temp = arrivaldict[i].get()
        temp2 =durationdict[i].get()
        try:
            float(temp)
            float(temp2)
            if float(temp2) == 0:
                flag = 0
                tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
                break
        except:
            tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
            flag =0
            break

        arrivaldict[i]=temp
        durationdict[i]=temp2
    if flag == 1:
        FCFS()
        Draw()
    #root2.destroy()
def checkPR():
    global root3
    global Emptive
    flag = 1
    for i in range(int(numberOfProcesses)):
        temp = arrivaldict[i].get()
        temp2 = durationdict[i].get()
        temp3 = prioritydict[i].get()
        try:
            float(temp)
            float(temp2)
            int(temp3)
            if float(temp2)==0:
                flag=0
                tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
                break


        except:
            tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
            flag =0
            break
        else:
            arrivaldict[i] = float(temp)
            durationdict[i] = float(temp2)
            prioritydict[i] = float(temp3)
    if (Emptive.get() == "Pre or Non"):
        flag = 0
    if(flag==1):
        PR()
        r#oot3.destroy()
        Draw()

def checkSJF():
    global root4
    global Emptive
    flag = 1
    for i in range(int(numberOfProcesses)):
        temp = arrivaldict[i].get()
        temp2 =durationdict[i].get()
        if (not(temp.isnumeric()) or not(temp2.isnumeric()) or  int(temp2)==0):
            flag =0
        else:
            arrivaldict[i]=temp
            durationdict[i]=temp2
    if(Emptive.get()=="Pre or Non"):
        flag = 0
    if flag == 0:
        tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
    if (flag==1):
        if(Emptive.get()=='Non-Preemptive'):
            SJF(0)
        if (Emptive.get() == 'Pre-Emptive'):
            SJF(1)
        Draw()
        #root4.destroy()






def SJF_page():
    global numberOfProcesses
    global entryq
    global arrivaldict
    global durationdict
    global emptive
    global checkk
    global root4
    global Emptive
    checkk= IntVar()
    arrivaldict = {}
    durationdict = {}
    root4 = Tk()
    root4.title("SJF Scheduler")
    root4.geometry("300x300")
    Plabel = Label(root4, text="Process Name", )
    Plabel.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

    arrival = Label(root4, text="Arrival Time")
    arrival.grid(row=0, column=4, columnspan=3, padx=10, pady=5)

    duration = Label(root4, text="Duration")
    duration.grid(row=0, column=8, columnspan=3, padx=10, pady=5)


    for i in range(int(numberOfProcesses)):
        label = Label(root4, text='P' + str(i))
        label.grid(row=i + 1, column=0, columnspan=3, padx=10, pady=5)
        arrivaldict[i] = Entry(root4, width=10)
        arrivaldict[i].grid(row=i + 1, column=4, columnspan=3, padx=20, pady=5)

        durationdict[i] = Entry(root4, width=10)
        durationdict[i].grid(row=i + 1, column=8, columnspan=3, padx=20, pady=5)

    Emptive = Combobox(root4, values=['Pre-Emptive', 'Non-Preemptive'], width=15)
    Emptive.set("Pre or Non")
    Emptive.grid(columnspan=12)

    buuton = Button(root4, text="OK", command=checkSJF)
    buuton.grid(columnspan=12)
def RR_Page():
    global numberOfProcesses
    global entryq
    global arrivaldict
    global durationdict
    global root5
    global Quantum
    arrivaldict = {}
    durationdict = {}
    root5 = Tk()
    root5.title("RR Scheduler")
    root5.geometry("300x300")
    Plabel = Label(root5, text="Process Name", )
    Plabel.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

    arrival = Label(root5, text="Arrival Time")
    arrival.grid(row=0, column=4, columnspan=3, padx=10, pady=5)

    duration = Label(root5, text="Duration")
    duration.grid(row=0, column=8, columnspan=3, padx=10, pady=5)

    for i in range(int(numberOfProcesses)):
        label = Label(root5, text='P' + str(i))
        label.grid(row=i + 1, column=0, columnspan=3, padx=10, pady=5)
        arrivaldict[i] = Entry(root5, width=10)
        arrivaldict[i].grid(row=i + 1, column=4, columnspan=3, padx=20, pady=5)

        durationdict[i] = Entry(root5, width=10)
        durationdict[i].grid(row=i + 1, column=8, columnspan=3, padx=20, pady=5)
    label8= Label(root5,text="Quantum Time:")
    label8.grid(row=i+2)
    Quantum = Entry(root5)
    Quantum.grid(row=i+2,column=2,columnspan=12)

    buuton = Button(root5, text="OK",command=checkRR)
    buuton.grid(columnspan=12)

def PR_page():
    global numberOfProcesses
    global entryq
    global arrivaldict
    global durationdict
    global prioritydict
    global root3
    global Emptive
    arrivaldict = {}
    durationdict = {}
    prioritydict = {}
    root3 = Tk()
    root3.title("PR Scheduler")
    root3.geometry("450x400")
    Plabel = Label(root3, text="Process Name", )
    Plabel.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
    arrival = Label(root3, text="Arrival Time")
    arrival.grid(row=0, column=4, columnspan=3, padx=10, pady=5)
    duration = Label(root3, text="Duration")
    duration.grid(row=0, column=8, columnspan=3, padx=10, pady=5)
    priority = Label(root3,text="Priority")
    priority.grid(row=0, column=12, columnspan=3 , padx=10,pady=5)
    for i in range(int(numberOfProcesses)):
        label = Label(root3, text='P' + str(i))
        label.grid(row=i + 1, column=0, columnspan=3, padx=10, pady=5)
        arrivaldict[i] = Entry(root3, width=10)
        arrivaldict[i].grid(row=i + 1, column=4, columnspan=3, padx=20, pady=5)

        durationdict[i] = Entry(root3, width=10)
        durationdict[i].grid(row=i + 1, column=8, columnspan=3, padx=20, pady=5)

        prioritydict[i] = Entry(root3, width=10)
        prioritydict[i].grid(row=i + 1, column=12, columnspan=3, padx=20, pady=5)

    Emptive = Combobox(root3, values=['Pre-Emptive', 'Non-Preemptive'], width=15)
    Emptive.set("Pre or Non")
    Emptive.grid(columnspan=16)
    buuton = Button(root3, text="OK", command=checkPR)
    buuton.grid(columnspan=18)
def FCFCS_page():
    global numberOfProcesses
    global entryq
    global arrivaldict
    global durationdict
    global root2
    arrivaldict = {}
    durationdict = {}
    root2 = Tk()
    root2.title("FCFS Scheduler")
    root2.geometry("300x300")
    Plabel = Label(root2, text="Process Name",)
    Plabel.grid(row=0, column=0,columnspan= 3, padx=10,pady=5)
    arrival = Label(root2,text="Arrival Time")
    arrival.grid(row=0, column=4 ,columnspan=3,padx=10,pady=5)
    duration = Label(root2, text="Duration")
    duration.grid(row=0, column=8,columnspan=3,padx=10,pady=5)



    for i in range(int(numberOfProcesses)):
        label = Label(root2, text='P' + str(i))
        label.grid(row=i+1, column=0,columnspan= 3, padx=10,pady=5)
        arrivaldict[i] = Entry(root2, width=10)
        arrivaldict[i].grid(row=i+1, column=4,columnspan= 3, padx=20,pady=5)


        durationdict[i] = Entry(root2, width=10)
        durationdict[i].grid(row=i+1, column=8,columnspan= 3, padx=20,pady=5)

    buuton = Button(root2,text="OK",command=checkFCFS)
    buuton.grid(columnspan=12)






def mainpage():
    global root
    global technique
    global number
    global NumberOfProcesses
    root = Tk()
    root.title("Scheduler")
    root.geometry("300x300")

    upperframe = Frame()
    upperframe.pack()
    lowerframe = Frame()
    lowerframe.pack(side=BOTTOM)

    choices=["FCFS","SJF","PR","RR"]
    technique = Combobox(root, values=choices, width=15)
    technique.set("Choose..")



    label_1 = Label(upperframe, text="No. of processes")
    label_2 = Label(root, text="Select a technique",width=200)
    button_1 = Button(root, text="OK" ,command=showtype)
    number = Entry(upperframe)
    menu = Menu(root)
    label_1.pack(side=LEFT)
    number.pack(side=RIGHT)
    label_2.pack()
    technique.pack()
    button_1.pack()

def showtype():
    global numberOfProcesses
    global number
    global root
    global Time
    global HighestPrior
    global ProccessNumber
    global MinimumProcessArrivalTime
    global max
    global element
    global j
    if(not((number.get()).isnumeric()) or int(number.get())==0 or technique.get()=="Choose.."):
        tkinter.messagebox.showerror("Error","ERROR:Please enter a valid input")
    else:
        numberOfProcesses = int(number.get())
        Time =0
        j=0
        durationdict.clear()
        arrivaldict.clear()
        prioritydict.clear()
        PAV.clear()
        ProcessedProcess.clear()
        ProcessedTime.clear()
        ProcessStartTime.clear()
        HighestPrior = 9999999999999999999999999999999
        ProccessNumber = -1
        MinimumProcessArrivalTime = 99999999999999999999999999999
        max = 0
        element = 0
        if(technique.get() == "FCFS"):
            FCFCS_page()

        if(technique.get() == "PR"):
            PR_page()

        if (technique.get() == "SJF"):
            SJF_page()
        if(technique.get() == "RR"):
            RR_Page()

        #root.withdraw()

def SJF(preemptive): # 1 if preemptive,0 if non preemptive
    global number
    global  Time
    global durationdict
    global arrivaldict
    global ProcessStartTime
    global ProcessedProcess
    global ProcessedTime
    last_process_name = ''

    waitingTime = []
    responseTime = []
    number_of_done = 0
    time = Decimal(0)
    processes = []
    processes_queue = []
    last_appended = 0
    do_flag = 0
    done_flag = 0
    for index in range(int(number.get())):  # looping in the txt file,adding string in a list then splitting the strings then appending objects in a list
        processes.append(Process('P'+ str(index), arrivaldict[index], durationdict[index]))
    processes.sort(key=lambda x: x.arrival)  # sort proccesses according to arrival time
    while (1):
        for index in range(last_appended, len(processes)):
            if (time == processes[index].arrival):
                processes_queue.append(processes[index])
                last_appended = index
                # print(processes_queue[last_appended].status())
                if(do_flag == 0):
                    processes_queue.sort(key=lambda x: x.remaining)
            else:
                last_appended = index
                break

        if (len(processes_queue) == 0):
            if (do_flag == 0):
                time += Decimal(minimalResolution)
                continue
            elif (number_of_done != len(processes)):
                time += Decimal(minimalResolution)
                continue
            else:
                break
        if (processes_queue[0].name != last_process_name):  # process changed
            ProcessedProcess.append(processes_queue[0].name)
            ProcessStartTime.append(time)
            ProcessedTime.append(0)
        # print(processes_queue[0].status(),"time :",time)
        last_process_name = processes_queue[0].name
        if ((done_flag == 1) or (preemptive)):
            processes_queue.sort(key=lambda x: x.remaining)
            done_flag = 0
        if (round(processes_queue[0].remaining, 1) == 0):
            done_flag = 1
            # print("process", processes_queue[0].name, "is done")
            #waitingTime.append(time - processes_queue[0].burst - processes_queue[0].arrival)
            processes_queue.remove(processes_queue[0])
            number_of_done += 1
            if (len(processes_queue) != 0):
                processes_queue.sort(key=lambda x: x.remaining)
                last_process_name = processes_queue[0].name
                ProcessedProcess.append(processes_queue[0].name)
                ProcessStartTime.append(time)
                ProcessedTime.append(0)
                processes_queue[0].do_process()
                ProcessedTime[-1] += Decimal(minimalResolution)
                do_flag = 1
            # print(time, processes_queue[0].name, " ", end="")
        else:
            processes_queue[0].do_process()
            ProcessedTime[-1] += Decimal(minimalResolution)
            do_flag = 1
        #  print(time,processes_queue[0].name," ",end = "")
        time += Decimal(minimalResolution)
    for index in range(len(processes)):
        print(processes[index].name)
        name_index = ProcessedProcess.index(processes[index].name)
        responseTime.append(ProcessStartTime[name_index] - processes[index].arrival)
        ProcessedProcess.reverse()
        name_index = len(ProcessedProcess) - ProcessedProcess.index(processes[index].name) - 1
        ProcessedProcess.reverse()
        waitingTime.append(ProcessStartTime[name_index] + ProcessedTime[name_index] - processes[index].burst - processes[index].arrival)
    numberofprocess = len(ProcessedProcess)
    Time = time



def Scheduler():
    global Time
    global HighestPrior
    global ProccessNumber
    global numberOfProcesses
    global MinimumProcessArrivalTime
    global j
    global waitingtime
    global ProcessedProcess
    while j < numberOfProcesses:
        for i in range(numberOfProcesses):
            if float(arrivaldict[i]) <= Time and float(durationdict[i]) != 0 and int(
                    prioritydict[i]) < HighestPrior:
                ProccessNumber = i
                HighestPrior = int(prioritydict[i])
            if (float(arrivaldict[i]) < MinimumProcessArrivalTime and float(durationdict[i]) != 0):
                MinimumProcessArrivalTime = float(arrivaldict[i])
        if ProccessNumber == -1:
            Time = MinimumProcessArrivalTime
        else:
            ProcessStartTime.append(Time)
            Time = Time + float(durationdict[ProccessNumber])
            waitingtime[ProccessNumber]= Time - float(durationdict[ProccessNumber]) - float(arrivaldict[ProccessNumber])
            ProcessedProcess.append("P"+str(ProccessNumber))
            ProcessedTime.append(float(durationdict[ProccessNumber]))
            durationdict[ProccessNumber] = 0
            HighestPrior = 99999999999999999999999999
            ProccessNumber = -1
            MinimumProcessArrivalTime = 99999999999999999999999999
            j = j + 1


def PreScheduler():
    global durationdict
    global Time
    global prioritydict
    global HighestPrior
    global ProccessNumber
    global numberOfProcesses
    global arrivaldict
    global MinimumProcessArrivalTime
    global j
    global PAV
    global Position
    global number
    global ProcessedProcess
    global ProcessStartTime
    global ProcessedTime
    global waitingtime
    PAV.clear()
    ProcessedProcess.clear()
    ProcessedTime.clear()
    ProcessStartTime.clear()
    Position=0
    HighestPrior=99999999999999999999999999
    Time=0
    ProccessNumber=-1
    x=int(number.get())
    for i in range(x):
        PAV.append(arrivaldict[i])
    PAV=sorted(PAV)
    PAV=list(dict.fromkeys(PAV))
    flag = 0
    durationdictcopy = copy.deepcopy(durationdict)
    if float(PAV[Position]) ==0:

        if (Position == (len(PAV) - 1)):
            flag = 1
        else:
            Position = Position+1
    while j < numberOfProcesses:
        for i in range(numberOfProcesses):
            if float(arrivaldict[i]) <= Time and float(durationdict[i]) != 0 and int(
                    prioritydict[i]) < HighestPrior:
                ProccessNumber = i
                HighestPrior = int(prioritydict[i])
            if (float(arrivaldict[i]) < MinimumProcessArrivalTime and float(durationdict[i]) != 0):
                MinimumProcessArrivalTime = float(arrivaldict[i])
        if ProccessNumber == -1:
            Time = float(PAV[Position])
            if (Position == (len(PAV) - 1)):
                flag = 1
            if (flag == 0):
                Position = Position + 1
                continue
        else:
            if(Time+float(durationdict[ProccessNumber])<float(PAV[Position]) or flag == 1):
                ProcessStartTime.append(Time)
                Time = Time + float(durationdict[ProccessNumber])
                waitingtime[ProccessNumber] = Time - float(durationdictcopy[ProccessNumber]) - float(
                    arrivaldict[ProccessNumber])

                ProcessedProcess.append("P" + str(ProccessNumber))
                ProcessedTime.append(float(durationdict[ProccessNumber]))
                durationdict[ProccessNumber] = 0
                HighestPrior = 99999999999999999999999999
                ProccessNumber = -1
                MinimumProcessArrivalTime = 99999999999999999999999999
                j = j + 1

            else:
                ProcessStartTime.append(Time)
                ProcessedTime.append(float(PAV[Position])-Time)
                durationdict[ProccessNumber] = str(float(durationdict[ProccessNumber]) -(float(PAV[Position])-Time))
                Time = float(PAV[Position])
                ProcessedProcess.append("P" + str(ProccessNumber))
                HighestPrior = 99999999999999999999999999
                ProccessNumber = -1
                MinimumProcessArrivalTime = 99999999999999999999999999
                if (Position == (len(PAV) - 1)):
                    flag = 1
                if (flag == 0):
                    Position = Position + 1

    print(waitingtime)




def RR(timeQuantum):
    global Time
    global ProcessedTime
    global ProcessedProcess
    global ProcessStartTime
    last_process_name = ''
    waitingTime = []
    responseTime = []
    processes = []
    processes_queue = []
    time = Decimal(0)
    last_appended = 0
    untilTime = Decimal(0)
    number_of_done = 0
    timeQuantum = round(Decimal(timeQuantum), 1)
    for index in range(int(number.get())):  # looping in the txt file,adding string in a list then splitting the strings then appending objects in a list
        processes.append(Process('P'+ str(index), arrivaldict[index], durationdict[index]))
    processes.sort(key=lambda x: x.arrival)  # sort proccesses according to arrival time
    while (1):

        for index in range(last_appended, len(processes)):
            # print('is',time,'=',processes[index].arrival)
            if (time == processes[index].arrival):
                processes_queue.append(processes[index])
                last_appended = index
                # print(processes_queue[last_appended].status())

            else:
                last_appended = index
                break
        # print('untilTime ', untilTime)
        if (len(processes_queue) != 0):  # process queue has something
           # print(untilTime, '=', timeQuantum)
            if (untilTime == timeQuantum):  # timeQuantum is reached
                processes_queue.append(processes_queue.pop(0))  # first goes last
                untilTime = Decimal(0)
            if (processes_queue[0].name != last_process_name):  # process changed
                ProcessedProcess.append(processes_queue[0].name)
                ProcessStartTime.append(time)
                ProcessedTime.append(0)
            # print(pDraw(gant)rocesses_queue[0].status(),"time :",time)
            last_process_name = processes_queue[0].name
            if (processes_queue[0].do_process() != None):  # top process still has remainnig BT
                ProcessedTime[-1] += Decimal(minimalResolution)
                # print(processes_queue[0].status(), ' time ', time)
            else:  # top process has finished
                # print("process", processes_queue[0].name, "is done")
                #waitingTime.append(time+minimalResolution - processes_queue[0].burst - processes_queue[0].arrival)
                ProcessedTime[-1] += Decimal(minimalResolution)
                processes_queue.pop(0)
                untilTime = - Decimal(minimalResolution)
                number_of_done += 1
        elif ((number_of_done == len(processes))):  # nothing in the process queue but all process were executed
            break
        else:  # gap
            untilTime = - Decimal(minimalResolution)
        untilTime += Decimal(minimalResolution)
        untilTime = (Decimal(untilTime) % (
                    Decimal(timeQuantum) + Decimal(minimalResolution)))  # untilTime goes 1..timeQuantum,1..

        time += Decimal(minimalResolution)


    for index in range(len(processes)):
        print(processes[index].name)
        name_index = ProcessedProcess.index(processes[index].name)
        responseTime.append(ProcessStartTime[name_index] - processes[index].arrival)
        ProcessedProcess.reverse()
        name_index = len(ProcessedProcess) - ProcessedProcess.index(processes[index].name) - 1
        ProcessedProcess.reverse()
        waitingTime.append(ProcessStartTime[name_index] + ProcessedTime[name_index] - processes[index].burst - processes[index].arrival)
    numberofprocess = len(ProcessedProcess)
    Time = time
   # print('waitint time',waitingTime)
    #print('response time',responseTime)







def Draw():
    ytick=[]
    ProcessesNames =[]

    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    # Setting Y-axis limits
    gnt.set_ylim(0, int(len(ProcessedProcess))+2)
    # Setting X-axis limits
    gnt.set_xlim(0, float(Time) * 1.25)
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('seconds since start')
    gnt.set_ylabel('Process Numbers ')
    # Labelling tickes of y-axis
    ProcessesNames.append(ProcessedProcess[0])
    for index in range(len(ProcessedProcess)):
        try:
            process_index = ProcessesNames.index(ProcessedProcess[index])
        except ValueError:
            ProcessesNames.append(ProcessedProcess[index])
    ProcessesNames.sort()
    for i in range(len(ProcessesNames)):
        ytick.append(i+1)
    gnt.set_yticklabels(ProcessesNames)
    gnt.set_yticks(ytick)
    # Setting graph attribute
    gnt.grid(True)

    # Declaring a bar in schedule
    for i in range(len(ProcessedProcess)):
        process_index = ProcessesNames.index(ProcessedProcess[i])
        gnt.broken_barh([(Decimal(ProcessStartTime[i]), Decimal(ProcessedTime[i]))], (process_index ,1 ), facecolors=('black'))
    plt.show()






mainpage()

root.mainloop()










































