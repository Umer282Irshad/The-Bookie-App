from tkinter import *
root = Tk()
root.geometry('450x500')
root.title('Bookie.py')
class mainPage():
    def __init__(self):
        self.clearFrame()
        Label(root, text = 'The Bookie App',
        bg = 'grey',
        font = 'Times 30 bold italic').pack(fill = X)
        Label(root, text = 'What do you want to do:',
        font = ' Times 15 bold underline').pack(anchor = NW , padx = 15 , pady = 40)
        Button(root, text = 'Book a Ticket',
        bg = 'grey',
        font = 'Times 20 bold',
        command = BookingSection).pack()
        Label(root, text = '     ',
        font = 'Times 20').pack()
        Button(root, text = 'Cancel a Ticket',
        bg = 'grey',
        font = 'Times 20 bold',
        command = CancelSection).pack()
        Button(root, text = 'Exit',
        font = 'Times 15 bold',
        bg = 'grey',
        command =root.destroy).pack(side = BOTTOM)
        mainloop()
    def clearFrame(self):
        for widget in root.winfo_children():
            widget.destroy()

class BookingSection(mainPage):
    def __init__(self):
        self.clearFrame()
        Label(root, text = 'Booking Section',
        bg = 'grey',
        font = 'Times 30 bold italic').pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'grey',
        command =mainPage).pack(side = BOTTOM)
        Label(root, text = 'What would you like to book:',
        font = ' Times 15 bold underline').pack(anchor = NW , padx = 15 , pady = 40)
        Button(root, text = 'Transport Tickets',
        font = 'Times 20 bold',
        bg = 'grey',
        command = TransportSection).pack()
        Button(root, text = 'Cinema Tickets',
        font = 'Times 20 bold',
        bg = 'grey',
        command =mainPage).pack()
        Button(root, text = 'Technicians',
        font = 'Times 20 bold',
        bg = 'grey',
        command =mainPage).pack()
        
class CancelSection(mainPage):
    def __init__(self):
        self.clearFrame()
        Label(root, text = 'Cancel Section',
        bg = 'grey',
        font = 'Times 30 bold italic').pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'grey',
        command =mainPage).pack(side = BOTTOM)

class TransportSection(BookingSection):
    def __init__(self):
        self.clearFrame()
        Label(root, text = 'Transport Section',
        bg = 'grey',
        font = 'Times 30 bold italic').pack(fill = X)
        Label(root, text = 'What kind of ticket would you like to book:',
        font = ' Times 15 bold underline').pack(anchor = NW , padx = 15 , pady = 40)
        Button(root, text = 'Aeroplane',
        font = 'Times 20 bold',
        bg = 'grey',
        command =mainPage).pack()
        Button(root, text = 'Rickshaw',
        font = 'Times 20 bold',
        bg = 'grey',
        command =mainPage).pack()
        Button(root, text = 'Train',
        font = 'Times 20 bold',
        bg = 'grey',
        command =TrainSection).pack()
        Button(root, text = 'Bus',
        font = 'Times 20 bold',
        bg = 'grey',
        command =mainPage).pack()
        Button(root, text = 'Cars',
        font = 'Times 20 bold',
        bg = 'grey').pack()
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'grey',
        command =BookingSection).pack(side = BOTTOM)
class TrainSection(TransportSection):
    def __init__(self):
        self.clearFrame()
        Label(root, text = 'Train Section',
        bg = 'grey',
        font = 'Times 30 bold italic').pack(fill = X)
        Button(root, text = 'Back',
        font = 'Times 15 bold',
        bg = 'grey',
        command =TransportSection).pack(side = BOTTOM)
