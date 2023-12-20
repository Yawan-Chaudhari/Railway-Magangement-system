class Train():

    def printer(self):
        print("Name of destination must be in SMALL LETTERS")
    @staticmethod
    def destinations():
        print("Destinations are shown below\n1.Agra\n2.Mathura\n3.Palwal\n4.Faridabad\n5.Delhi\n6.Hardoi\n7.Lucknow\n8.Bihar")


    def __init__(self,name,age,gender,destination,seats_in_R,seats_in_S,seats_in_GR):
        self.seats_in_GR = seats_in_GR
        self.seats_in_S = seats_in_S
        self.seats_in_R = seats_in_R
        self.name = name
        self.age  = age
        self.gender = gender
        self.destination = destination
        destination = destination.lower()

    def details_of_passenger(self):
        print(f"Name of Passenger is {self.name}")
        print(f"Age of Passenger is {self.age}")
        print(f"Gender of Passenger is {self.gender}")
        print(f"Destination of Passenger is {self.destination}")
        

    def Trains_Available(self):
        if (self.destination == "agra" or self.destination == 'mathura'):
            print("Rajdhani Express is Available")
        elif(self.destination == "palwal" or self.destination =="faridabad" or self.destination == "delhi"):
            print("Satavdi Express is Available")
        elif(self.destination == "hardoi" or self.destination == "lucknow" or self.destination == "bihar"):
            print("Gareeb Rath is Available")
        else:
            print("Sorry, No Train for your destination!!")


    def seats_available_in_Rajdhani_Express(self):
        print(f"Seats available: {self.seats_in_R}")

    def book_ticket_in_R(self):
        if(self.seats_in_R>0):
            print(f"Your ticket is Booked!!\nTrain:Rajdhani Express\nSeat No : {self.seats_in_R}")
            self.seats_in_R = self.seats_in_R - 1
        else:
            print("Sorry, Try In TatKal") 


    def seats_available_in_Satavdi_Express(self):
        print(f"Seats available: {self.seats_in_S}") 

    def book_ticket_in_S(self):
        if(self.seats_in_S>0):
            print("Your ticket is Booked!!\nTrain:Satavdi Express\nSeat No : {self.seats_in_S}")
            self.seats_in_S = self.seats_in_S - 1
        else:
            print("Sorry, Try In TatKal")  


    def seats_available_in_Gareeb_Rath(self):
        print(f"Seats available: {self.seats_in_GR}") 

    def book_ticket_in_GR(self):
        if(self.seats_in_GR>0):
            print("Your ticket is Booked!!\nTrain:Gareeb Rath\nSeat No : {self.seats_in_GR}")
            self.seats_in_GR = self.seats_in_GR - 1
        else:
            print("Sorry, Try In TatKal") 

    def cancel_ticket_in_R(self):
        print(f"Your Ticket of {self.destination} in Rajdhani Express in cancelled Successfully!!")
        self.seats_in_R = self.seats_in_R + 1


    def cancel_ticket_in_S(self):
        print(f"Your Ticket of {self.destination} in Satavdi Express in cancelled Successfully!!")
        self.seats_in_S = self.seats_in_S + 1


    def cancel_ticket_in_GR(self):
        print(f"Your Ticket of {self.destination} in Gareeb Rath in cancelled Successfully!!")
        self.seats_in_GR = self.seats_in_GR + 1

       
a = Train("Varshu",22,"Female","Agra",6,7,8)
a.destinations()

a.details_of_passenger()
a.Trains_Available()
a.seats_available_in_Rajdhani_Express()
a.book_ticket_in_R()
a.seats_available_in_Rajdhani_Express()
a.book_ticket_in_R()
a.seats_available_in_Rajdhani_Express()
a.book_ticket_in_R()
a.seats_available_in_Rajdhani_Express()
a.cancel_ticket_in_R()
a.seats_available_in_Rajdhani_Express()