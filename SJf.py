import sys
import random
import os


class Process:

    def __init__(self, name, arrival, remaining):
        self.name = name
        self.arrival = int(arrival)
        self.remaining = int(remaining)

    def do_process(self):
        self.remaining -= 1

    def remaining(self):
        return self.remaining

    def status(self):
        return "Name : {}, arrival: {}, remaining : {}".format(self.name, self.arrival, self.remaining)
time = 0
processes = []
process_file = open(r"/home/tho/PycharmProjects/SJF/processes","r")
processes_string = process_file.readlines()
processes_queue = []
last_appended = 0
do_flag = 0
done_flag = 0
for index in range(len(processes_string)): #looping in the txt file,adding string in a list then splitting the strings then appending objects in a list
    processes_string[index] = processes_string[index].rstrip('\n')
    name,arrival,remaining = processes_string[index].split()
    processes.append(Process(name,arrival,remaining))
processes.sort(key = lambda x : x.arrival)#sort proccesses according to arrival time
while(1):
    for index in range(last_appended,len(processes)):
        if(time == processes[index].arrival):
            processes_queue.append(processes[index])
            last_appended = index
            #print(processes_queue[last_appended].status())
        else:
            last_appended = index
            break
    if(len(processes_queue) == 0):
        if (do_flag == 0):
            time += 1
            continue
        else:
            break
    if(done_flag ==1):
        processes_queue.sort(key=lambda x: x.remaining)
        done_flag = 0
    if(processes_queue[0].remaining == 0):
        done_flag = 1
        print("process", processes_queue[0].name, "is done")
        processes_queue.remove(processes_queue[0])
        if(len(processes_queue) != 0):
            processes_queue[0].do_process()
            do_flag = 1
           # print(time, processes_queue[0].name, " ", end="")
    else:
        processes_queue[0].do_process()
        do_flag = 1
      #  print(time,processes_queue[0].name," ",end = "")
    time += 1


