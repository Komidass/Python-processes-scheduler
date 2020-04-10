import sys
import os
import numpy
import matplotlib
import matplotlib.pyplot as plt

class Process:

    def __init__(self, name, arrival, remaining):
        self.name = name
        self.arrival = int(arrival)
        self.remaining = int(remaining)

    def do_process(self):
        if (self.remaining == 0):
            return None
        else:
            self.remaining -= 1
            if (self.remaining == 0):
                return None
            else:
                return self.remaining

    def status(self):
        return "Name : {}, arrival: {}, remaining : {}".format(self.name, self.arrival, self.remaining)


def RR(timeQuantum):
    gant_names = []
    gant_beginning_time = []
    gant_working_time = []
    last_process_name = ''
    gant = []

    process_file = open(r"/home/tho/PycharmProjects/SJF/processes", "r")
    processes_string = process_file.readlines()
    processes = []
    processes_queue = []
    time = 0
    last_appended = 0
    untilTime = 0
    number_of_done = 0
    for index in range(len(processes_string)):  # looping in the txt file,adding string in a list then splitting the strings then appending objects in a list
        processes_string[index] = processes_string[index].rstrip('\n')
        name, arrival, remaining = processes_string[index].split()
        processes.append(Process(name, arrival, remaining))
    processes.sort(key=lambda x: x.arrival)  # sort proccesses according to arrival time
    while (1):
        for index in range(last_appended, len(processes)):
            if (time == processes[index].arrival):
                processes_queue.append(processes[index])
                last_appended = index
                # print(processes_queue[last_appended].status())
            else:
                last_appended = index
                break
        #print('untilTime ', untilTime)
        if (len(processes_queue) != 0):  # process queue has something

            if (untilTime == timeQuantum):  # timeQuantum is reached
                processes_queue.append(processes_queue.pop(0))  # first goes last
                untilTime = 0
            if (processes_queue[0].name != last_process_name):  # process changed
                gant_names.append(processes_queue[0].name)
                gant_beginning_time.append(time)
                gant_working_time.append(0)
            # print(processes_queue[0].status(),"time :",time)
            last_process_name = processes_queue[0].name
            if (processes_queue[0].do_process() != None):  # top process still has remainnig BT
                gant_working_time[-1] += 1
                #print(processes_queue[0].status(), ' time ', time)
            else:  # top process has finished
                #print("process", processes_queue[0].name, "is done")
                gant_working_time[-1] += 1
                processes_queue.pop(0)
                untilTime = -1
                number_of_done += 1
        elif ((number_of_done == len(processes))):  # nothing in the process queue but all process were executed
            break
        else:  # gap
            untilTime = -1
        untilTime += 1
        untilTime = (untilTime % (timeQuantum + 1))  # untilTime goes 1..timeQuantum,1..
        time += 1
    gant.append(gant_names)
    gant.append(gant_beginning_time)
    gant.append(gant_working_time)
    gant.append(len(gant_names))
    gant.append(time)
    return gant
def Draw(gant):
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    numberofprocess = gant[3]
    ProcessedPro = gant[0]
    ProcessStartTime = gant[1]
    ProcessedTime = gant[2]
    Time = gant[4]
    # Setting Y-axis limits
    gnt.set_ylim(0, numberofprocess + 10)
    # Setting X-axis limits
    gnt.set_xlim(0, int(Time) * 1.15)

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('seconds since start')
    gnt.set_ylabel('Process Numbers ')
    # Labelling tickes of y-axis
    gnt.set_yticklabels(ProcessedPro)

    # Setting graph attribute
    gnt.grid(True)

    # Declaring a bar in schedule
    for i in range(len(ProcessedPro)):
        gnt.broken_barh([(ProcessStartTime[i], ProcessedTime[i])], (i * 2, 1), facecolors=('black'))
    plt.show()
gant = []
gant = RR(3)
print('Names:',gant[0])#names
print('Start time:',gant[1])#start time
print('Duration:',gant[2])#duration
print('Number of processes:',gant[3])#number of process
print('Total time:',gant[4])#total time
Draw(gant)