import datetime
import random
from tkinter import *
root = Tk()
root.geometry('450x500')
root.title('Bookie.py')
dates = [datetime.datetime.today().strftime ('%d-%m-%Y')]
for i in range(1,8):
   day = datetime.datetime.today() + datetime.timedelta(days=i)
   date = day.strftime ('%d-%m-%Y')
   dates.append(date)
def file(file_name):
    a = open(file_name,'r')
    drivers = []
    for line in a:
        drivers.extend([word.split(' ') for word in line.split(',')])
    return drivers
def city(filename):
    a = open(filename,'r')
    return ''.join(a.readlines()).split(' ')
class mainPage():
    def __init__(self):
        self.clearFrame()
        Label(root, text = 'The Bookie App',
        bg = 'deep sky blue',
        font = 'Times 30 bold italic').pack(fill = X)
        Label(root, text = 'What do you want to do:',
        font = ' Times 15 bold underline').pack(anchor = NW , padx = 15 , pady = 40)
        Button(root, text = 'Book a Ticket',
        bg = 'deep sky blue',
        font = 'Times 20 bold',
        command = BookingSection).pack(fill = X)
        Label(root, text = '     ',
        font = 'Times 20').pack()
        Button(root, text = 'Cancel a Ticket',
        bg = 'deep sky blue',
        font = 'Times 20 bold',
        command = CancelSection).pack(fill = X)
        Button(root, text = 'Exit',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =root.destroy).pack(side = BOTTOM)
        mainloop()
    def clearFrame(self):
        for widget in root.winfo_children():
            widget.destroy()
    def Random(self):
        a = ''
        for i in range(4):
            a += str(random.randint(0, 9))
        return a

class BookingSection(mainPage):
    def __init__(self):
        self.clearFrame()
        Label(root, text = 'Booking Section',
        bg = 'deep sky blue',
        font = 'Times 30 bold italic').pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =mainPage).pack(side = BOTTOM)
        Label(root, text = 'What would you like to book:',
        font = ' Times 15 bold underline').pack(anchor = NW , padx = 15 , pady = 40)
        Button(root, text = 'Transport Tickets',
        font = 'Times 20 bold',
        bg = 'deep sky blue',
        command = TransportSection).pack(fill =X)
        Button(root, text = 'Cinema Tickets',
        font = 'Times 20 bold',
        bg = 'deep sky blue',
        command =mainPage).pack(fill = X)
        Button(root, text = 'Technicians',
        font = 'Times 20 bold',
        bg = 'deep sky blue',
        command =mainPage).pack(fill = X)
        
class CancelSection(mainPage):
    def __init__(self):
        self.clearFrame()
        Label(root, text = 'Cancel Section',
        bg = 'deep sky blue',
        font = 'Times 30 bold italic').pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =mainPage).pack(side = BOTTOM)

class TransportSection(BookingSection):
    def __init__(self):
        self.clearFrame()
        Label(root, text = 'Transport Section',
        bg = 'deep sky blue',
        font = 'Times 30 bold italic').pack(fill = X)
        Label(root, text = 'What kind of ticket would you like to book:',
        font = ' Times 15 bold underline').pack(anchor = NW , padx = 15 , pady = 40)
        Button(root, text = 'Train',
        font = 'Times 20 bold',
        bg = 'deep sky blue',
        command =TrainSection).pack(fill = X)
        Button(root, text = 'Bus',
        font = 'Times 20 bold',
        bg = 'deep sky blue',
        command =mainPage).pack(fill = X)
        Button(root, text = 'Cars',
        font = 'Times 20 bold',
        bg = 'deep sky blue',
        command = CarSection).pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =BookingSection).pack(side = BOTTOM)
class TrainSection(TransportSection):
    nameValue = StringVar()                                
    phoneValue = StringVar()
    CNICValue = StringVar()
    variable0 = StringVar()
    variable0.set('Enter Departure')
    variable1 = StringVar()
    variable1.set('Enter Arrival')
    variable2 = StringVar()
    variable2.set('Date of Departure')
    variable3 = StringVar()
    variable3.set('Class')
    variable4 = StringVar()
    variable4.set('Available Timings')
    def __init__(self):
        self.cities0 = city('Cities.txt')
        self.cities1 = self.cities0.copy()
        self.now = datetime.datetime.now()
        self.trains = file('Train.txt')
        self.available = []
        self.pickedtrain = []
        self.clearFrame()
        Label(root, text = 'Train Section',
        bg = 'deep sky blue',
        font = 'Times 30 bold italic').pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =TransportSection).pack(side = BOTTOM)
        Label(root, text = 'Enter the required information:',
        font = ' Times 10 bold underline').pack(anchor = NW , padx = 15 , pady = 15)
        Label(root , text = 'Class', font = 'Times 10').pack(anchor= NW , padx = 20)
        departure = self.cities0
        OptionMenu(root,self.variable0,*departure).pack(fill = X)
        Label(root , text = 'Arrival:', font = 'Times 10').pack(anchor= NW , padx = 20)
        arrival = self.cities1
        OptionMenu(root,self.variable1,*arrival).pack(fill = X)
        Label(root , text = 'Date of Departure:', font = 'Times 10').pack(anchor= NW , padx = 20)
        OptionMenu(root,self.variable2,*dates).pack(fill = X)
        Label(root , text = 'Name:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.nameValue, width = 25).pack()
        Label(root , text = 'Phone no:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.phoneValue, width = 25).pack()
        Label(root , text = 'CNIC:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.CNICValue, width = 25).pack()
        Button(root, text = 'Confirm',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command  = self.confirm).pack()
        
    
    def confirm(self):
        if len(self.CNICValue.get()) == 0 or len(self.phoneValue.get()) == 0 or len(self.nameValue.get()) == 0 or self.variable0.get() == 'Enter Departure' or self.variable1.get() == 'Enter Arrival' or self.variable2.get() == 'Date of Departure':
            a = Tk()
            a.geometry('350x50')
            Label(a, text = 'Error',
            bg = 'deep sky blue',
            font = 'Times 20 bold italic').pack(fill = X)
            Label(a , text = 'Please fill the form completely and corectly.', font = 'Times 10').pack(anchor= NW , padx = 20)
            a.mainloop()
        else:
            m = self.variable0.get() + 'to' + self.variable1.get()
            for i in self.trains:
                if i[0] == m:
                    self.available.append(i)
            for i in self.available:
                if i[2][-2:] == 'am':
                    if self.now > self.now.replace(hour=int(i[2][:-2]), minute=0, second=0, microsecond=0):
                        self.avaiable.pop(self.available.index(i))
                if i[2][-2:] == 'pm':
                    if self.now > self.now.replace(hour=int(i[2][:-2])+11, minute=0, second=0, microsecond=0):
                        self.available.pop(self.available.index(i))
            
            
            available1 = [x[2] for x in self.available]
            if len(available1) == 0:
                available1.append('No timings available')
            self.clearFrame()
            Label(root, text = 'Train Section',
            bg = 'deep sky blue',
            font = 'Times 30 bold italic').pack(fill = X)
            Label(root, text = 'Select your preference:',
            font = ' Times 10 bold underline').pack(anchor = NW , padx = 15 , pady = 15)
            Label(root , text = 'Available Timings', font = 'Times 10').pack(anchor= NW , padx = 20)
            OptionMenu(root,self.variable4,*available1).pack(fill = X)
            Label(root , text = 'Class', font = 'Times 10').pack(anchor= NW , padx = 20)
            OptionMenu(root,self.variable3,*['Business Class','Economy Class','Commercial Class']).pack(fill = X)
            Button(root, text = 'Back',
            font = 'Times 15 bold',
            bg = 'deep sky blue',
            command =TrainSection).pack(side = BOTTOM)
            Button(root, text = 'Confirm',
            font = 'Times 15 bold',
            bg = 'deep sky blue',
            command  = self.confirm1).pack()
    def confirm1(self):
        for i in range(len(self.available)):
                if self.available[i][2] == self.variable4.get():
                    self.pickedtrain = self.available[i]
        if not(int(self.pickedtrain[4]) == 0 and int(self.pickedtrain[5]) == 0 and int(self.pickedtrain[6])) == 0:
            if self.variable3.get() == 'Business Class':
                if int(self.pickedtrain[4]) == 0:
                    a = Tk()
                    a.geometry('350x50')
                    Label(a, text = 'Error',
                    bg = 'deep sky blue',
                    font = 'Times 20 bold italic').pack(fill = X)
                    Label(a , text = 'Sorry.No seats available.', font = 'Times 10').pack(anchor= NW , padx = 20)
                    a.mainloop()
                elif int(self.pickedtrain[4]) > 0 :
                    
                    seat = int(self.pickedtrain[4])
                    self.pickedtrain[4] = str(int(self.pickedtrain[4])-1)
                    self.trains.append(self.pickedtrain)
                    t ='TB'+self.Random()
                    fil = open("Train.txt","r+")
                    fil.truncate(0)
                    fil.close()
                    w = open('Train.txt','a')
                    for i in self.tarins:
                        w.write(' '.join(i)+',')
                    a.geometry('350x350')
                    Label(a, text = 'Ticket',
                    bg = 'deep sky blue',
                    font = 'Times 20 bold italic').pack(fill = X)
                    Label(a , text = 'Route', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[0], font = 'Times 10').pack()
                    Label(a , text = 'Ticket No.', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = t, font = 'Times 10').pack()
                    Label(a , text = 'Seat no.', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = seat, font = 'Times 10').pack()
                    Label(a , text = 'Date', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[1], font = 'Times 10').pack()
                    Label(a , text = 'Timing', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[2], font = 'Times 10').pack()
                    Label(a , text = 'Platform', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[3], font = 'Times 10').pack()
                    Label(a , text = f'Reach {self.pickedtrain[3]} 10 minutes before {self.pickedtrain[2]}', font = 'Times 10').pack(anchor= NW , padx = 20)
                    w = open('Tickets.txt','a')
                    w.write(f'{t} {self.pickedtrain[0]} {self.pickedtrain[1]} {self.pickedtrain[2]} {self.pickedtrain[3]} {self.pickedtrain[4]} {self.pickedtrain[5]} {self.pickedtrain[6]},')
                    w.close()
                    a.mainloop()
                    
                    
            if self.variable3.get() == 'Economy Class':
                if int(self.pickedtrain[5]) == 0:
                    a = Tk()
                    a.geometry('350x50')
                    Label(a, text = 'Error',
                    bg = 'deep sky blue',
                    font = 'Times 20 bold italic').pack(fill = X)
                    Label(a , text = 'Sorry.No seats available.Please try other class.', font = 'Times 10').pack(anchor= NW , padx = 20)
                    a.mainloop()
                elif int(self.pickedtrain[5]) > 0:
                    seat = int(self.pickedtrain[5])
                    self.pickedtrain[5] = str(int(self.pickedtrain[5])-1)
                    self.trains.append(self.pickedtrain)
                    t ='TB'+self.Random()
                    fil = open("Train.txt","r+")
                    fil.truncate(0)
                    fil.close()
                    w = open('Train.txt','a')
                    for i in self.tarins:
                        w.write(' '.join(i)+',')
                    a.geometry('350x350')
                    Label(a, text = 'Ticket',
                    bg = 'deep sky blue',
                    font = 'Times 20 bold italic').pack(fill = X)
                    Label(a , text = 'Route', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[0], font = 'Times 10').pack()
                    Label(a , text = 'Ticket No.', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = t, font = 'Times 10').pack()
                    Label(a , text = 'Seat no.', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = seat, font = 'Times 10').pack()
                    Label(a , text = 'Date', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[1], font = 'Times 10').pack()
                    Label(a , text = 'Timing', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[2], font = 'Times 10').pack()
                    Label(a , text = 'Platform', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[3], font = 'Times 10').pack()
                    Label(a , text = f'Reach {self.pickedtrain[3]} 10 minutes before {self.pickedtrain[2]}', font = 'Times 10').pack(anchor= NW , padx = 20)
                    w = open('Tickets.txt','a')
                    w.write(f'{t} {self.pickedtrain[0]} {self.pickedtrain[1]} {self.pickedtrain[2]} {self.pickedtrain[3]} {self.pickedtrain[4]} {self.pickedtrain[5]} {self.pickedtrain[6]},')
                    w.close()
                    a.mainloop()
            if self.variable3.get() == 'Commercial Class':
                if int(self.pickedtrain[6]) == 0:
                    a = Tk()
                    a.geometry('350x50')
                    Label(a, text = 'Error',
                    bg = 'deep sky blue',
                    font = 'Times 20 bold italic').pack(fill = X)
                    Label(a , text = 'Sorry.No seats available.Please try other class.', font = 'Times 10').pack(anchor= NW , padx = 20)
                    a.mainloop()
                elif int(self.pickedtrain[6]) > 0:
                    seat = int(self.pickedtrain[6])
                    self.pickedtrain[6] = str(int(self.pickedtrain[6])-1)
                    self.trains.append(self.pickedtrain)
                    t ='TB'+self.Random()
                    fil = open("Train.txt","r+")
                    fil.truncate(0)
                    fil.close()
                    w = open('Train.txt','a')
                    for i in self.tarins:
                        w.write(' '.join(i)+',')
                    a.geometry('350x350')
                    Label(a, text = 'Ticket',
                    bg = 'deep sky blue',
                    font = 'Times 20 bold italic').pack(fill = X)
                    Label(a , text = 'Route', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[0], font = 'Times 10').pack()
                    Label(a , text = 'Ticket No.', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = t, font = 'Times 10').pack()
                    Label(a , text = 'Seat no.', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = seat, font = 'Times 10').pack()
                    Label(a , text = 'Date', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[1], font = 'Times 10').pack()
                    Label(a , text = 'Timing', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[2], font = 'Times 10').pack()
                    Label(a , text = 'Platform', font = 'Times 10').pack(anchor= NW , padx = 20)
                    Label(a , text = self.pickedtrain[3], font = 'Times 10').pack()
                    Label(a , text = f'Reach {self.pickedtrain[3]} 10 minutes before {self.pickedtrain[2]}', font = 'Times 10').pack(anchor= NW , padx = 20)
                    w = open('Tickets.txt','a')
                    w.write(f'{t} {self.pickedtrain[0]} {self.pickedtrain[1]} {self.pickedtrain[2]} {self.pickedtrain[3]} {self.pickedtrain[4]} {self.pickedtrain[5]} {self.pickedtrain[6]},')
                    w.close()
                    a.mainloop()
        elif int(self.pickedtrain[4]) == 0 and int(self.pickedtrain[5]) == 0 and int(self.pickedtrain[6]) == 0:
            fil = open('Train.txt','r+')   
            fil.truncate(0)
            fil.close()
            w = open('Train.txt','a')
            for i in self.tarins:
                w.write(' '.join(i)+',')
            a = Tk()
            a.geometry('350x50')
            Label(a, text = 'Error',
            bg = 'deep sky blue',
            font = 'Times 20 bold italic').pack(fill = X)
            Label(a , text = 'All seats have been booked please try another timing.', font = 'Times 10').pack(anchor= NW , padx = 20)
            a.mainloop() 
class CarSection(TransportSection):
    nameValue = StringVar()                                
    phoneValue = StringVar()
    CNICValue = StringVar()
    pickValue = StringVar()
    destValue = StringVar()
    
    def __init__(self):
        self.drivers = file('driver data.txt')
        self.driver = self.drivers.copy()
        
        self.clearFrame()
        Label(root, text = 'Car Section',
        bg = 'deep sky blue',
        font = 'Times 30 bold italic').pack(fill = X)
        Label(root, text = 'What kind of car would you like to book:',
        font = ' Times 15 bold underline').pack(anchor = NW , padx = 15 , pady = 40)
        Button(root, text = 'Mini',
        font = 'Times 20 bold',
        bg = 'deep sky blue',
        command =self.Mini).pack(fill = X)
        Button(root, text = 'GO',
        font = 'Times 20 bold',
        bg = 'deep sky blue',
        command =self.Go).pack(fill = X)
        Button(root, text = 'GO Plus',
        font = 'Times 20 bold',
        bg = 'deep sky blue',
        command =self.GOPlus).pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =TransportSection).pack(side = BOTTOM)
    def Mini(self):
        self.clearFrame()
        Label(root, text = 'Mini Car',
        bg = 'deep sky blue',
        font = 'Times 30 bold italic').pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =CarSection).pack(side = BOTTOM)
        Label(root, text = 'Enter the required information:',
        font = ' Times 10 bold underline').pack(anchor = NW , padx = 15 , pady = 15)
        Label(root , text = 'Name:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.nameValue, width = 25).pack()
        Label(root , text = 'Phone no:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.phoneValue, width = 25).pack()
        Label(root , text = 'CNIC:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.CNICValue, width = 25).pack()
        Label(root , text = 'Pickup Point:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.pickValue, width = 50).pack()
        Label(root , text = 'Destination:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.destValue, width = 50).pack()
        Button(root, text = 'Confirm',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =self.confirm0).pack()
    
    
    def Go(self):
        self.clearFrame()
        Label(root, text = 'GO Car',
        bg = 'deep sky blue',
        font = 'Times 30 bold italic').pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =CarSection).pack(side = BOTTOM)
        Label(root, text = 'Enter the required information:',
        font = ' Times 10 bold underline').pack(anchor = NW , padx = 15 , pady = 15)
        Label(root , text = 'Name:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.nameValue, width = 25).pack()
        Label(root , text = 'Phone no:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.phoneValue, width = 25).pack()
        Label(root , text = 'CNIC:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.CNICValue, width = 25).pack()
        Label(root , text = 'Pickup Point:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.pickValue, width = 50).pack()
        Label(root , text = 'Destination:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.destValue, width = 50).pack()
        Button(root, text = 'Confirm',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =self.confirm0).pack()
    
    def GOPlus(self):
        self.clearFrame()
        Label(root, text = 'GOPlus',
        bg = 'deep sky blue',
        font = 'Times 30 bold italic').pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =CarSection).pack(side = BOTTOM)
        Label(root, text = 'Enter the required information:',
        font = ' Times 10 bold underline').pack(anchor = NW , padx = 15 , pady = 15)
        Label(root , text = 'Name:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.nameValue, width = 25).pack()
        Label(root , text = 'Phone no:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.phoneValue, width = 25).pack()
        Label(root , text = 'CNIC:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.CNICValue, width = 25).pack()
        Label(root , text = 'Pickup Point:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.pickValue, width = 50).pack()
        Label(root , text = 'Destination:', font = 'Times 10').pack(anchor= NW , padx = 20)
        Entry(root, textvariable= self.destValue, width = 50).pack()
        Button(root, text = 'Confirm',
        font = 'Times 15 bold',
        bg = 'deep sky blue',
        command =self.confirm0).pack()
    
    
   
    def confirm0(self):
        if len(self.nameValue.get())==0 or len(self.phoneValue.get()) == 0 or len(self.CNICValue.get())==0 or len(self.destValue.get()) == 0 or len(self.pickValue.get()) ==0  :
            a = Tk()
            a.geometry('350x50')
            Label(a, text = 'Error',
            bg = 'deep sky blue',
            font = 'Times 20 bold italic').pack(fill = X)
            Label(a , text = 'Please fill the form completely and corectly.', font = 'Times 10').pack(anchor= NW , padx = 20)
            a.mainloop()
        elif self.destValue.get() == self.pickValue.get():
            a = Tk()
            a.geometry('350x50')
            Label(a, text = 'Error',
            bg = 'deep sky blue',
            font = 'Times 20 bold italic').pack(fill = X)
            Label(a , text = 'Please fill the form completely and corectly.', font = 'Times 10').pack(anchor= NW , padx = 20)
            a.mainloop() 
        
        elif len(self.driver) > 0 :
            t = 'C'+self.Random()
            j = len(self.driver) - 1
            i = random.randint(0, j)
            driv = self.driver[i]
            self.driver.pop(i)
            fil = open("driver data.txt","r+")
            fil.truncate(0)
            fil.close()
            w = open('driver data.txt','a')
            for i in range(len(self.driver)):
               w.write(' '.join(self.driver[i])+',')
            w.close()
            a = Tk()
            a.geometry('350x350')
            Label(a, text = 'Ticket',
            bg = 'deep sky blue',
            font = 'Times 20 bold italic').pack(fill = X)
            Label(a , text = 'Ticket No.', font = 'Times 10').pack(anchor= NW , padx = 20)
            Label(a , text = t, font = 'Times 10').pack()
            Label(a , text = 'Pickup Point:', font = 'Times 10').pack(anchor= NW , padx = 20)
            Label(a , text = self.pickValue.get(), font = 'Times 10').pack()
            Label(a , text = 'Destination:', font = 'Times 10').pack(anchor= NW , padx = 20)
            Label(a , text = self.destValue.get(), font = 'Times 10').pack()
            Label(a , text = 'Driver Name:', font = 'Times 10').pack(anchor= NW , padx = 20)
            Label(a , text = driv[0], font = 'Times 10').pack()
            Label(a , text = 'Drivers Phone no::', font = 'Times 10').pack(anchor= NW , padx = 20)
            Label(a , text = driv[1], font = 'Times 10').pack()
            Label(a , text = 'Number Plate', font = 'Times 10').pack(anchor= NW , padx = 20)
            Label(a , text = driv[2], font = 'Times 10').pack()
            Label(a , text = 'Driver will reach you in 10 to 20 minutes.', font = 'Times 10').pack(anchor= NW , padx = 20)
            w = open('Tickets.txt','a')
            w.write(f'{t} {driv[0]} {driv[1]} {driv[2]},')
            w.close()
            a.mainloop()
        else:
            a = Tk()
            a.geometry('350x100')
            Label(a, text = 'Error',
            bg = 'deep sky blue',
            font = 'Times 20 bold italic').pack(fill = X)
            Label(a , text = 'No drivers available.Please try later.', font = 'Times 10').pack(anchor= NW , padx = 20)
            a.mainloop()
        
b = mainPage()
