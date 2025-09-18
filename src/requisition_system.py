class RequisitionSystem:

    def  __init__(self,):
        """
        Initializes all attributes for the requisition system.
        Design Principle: Encapsulation : all related data is stored inside the class.
        Improvement: Could make attributes private (e.g., self._total_cost) and use getters/setters.
        """
        self.Total_cost=0
        self.Date=""
        self.Staff_ID=""
        self.Staff_name=""
        self.Status=""
        self.Requisition_ID=""
        self.Total_requisition=0
        self.Total_approved=0
        self.Total_pending=0
        self.Total_not_approved=0
        self.unique_id=0
        self.Reference_NO=""

    def staff_info(self):
        """
        Collects and validates staff information.
        Design Principle: Single Responsibility Principle (SRP) – this method only handles staff info input.
        Improvement: Input validation could be moved to a helper method to follow DRY.
        """
        print("------------")
        while True:
                self.Date=input("Enter the date in this format 00/00/0000:")
                if self.Date=="":
                    print("Date cannot be empty. Please re-enter.")
                else:
                    break
        while True:        
                self.Staff_ID=input("Enter your staff id:")
                if self.Staff_ID=="":
                    print ("Staff id cannot be empty. Please re-enter.")
                else:
                    break
        while True:        
                self.Staff_name=input("Enter your full name:")
                if self.Staff_name=="":
                    print("Staff name cannot be empty. Please re-enter.")
                else:
                    break
        # Generate a unique requisition ID
        self.unique_id += 1
        self.Requisition_ID=str(1000+self.unique_id)
        self.second=self.Requisition_ID[-3:]
        # Display collected info
        print("Printing Staff Information:")
        print(f"Date: {self.Date}")
        print(f"Staff ID: {self.Staff_ID}")
        print(f"Staff Name: {self.Staff_name}")
        print(f"Requisition ID: {self.Requisition_ID}")
        print("------------")
        return self.Date, self.Staff_ID,self.Staff_name,self.Requisition_ID,self.second

    def requisitions_total(self):
        """
        Collects item details and calculates total cost.
        Design Principle: SRP : focuses only on requisition item entry and cost calculation.
        Improvement: Could reuse validation logic from staff_info() to follow DRY.
        """
        print("------------")
        self.Total_cost=0
        try:
            Items=int(input("how many items are your buying?"))
        except ValueError:
            Items=1
        #collects item name and price
        for i in range(1,Items+1):
            while True:
                Item_name=input(f"Enter the name of the items{i}:")
                if Item_name=="":
                    print("item name cannot be empty.Enter again")
                else:
                    break
            Item_cost =""
            while Item_cost == "":
                Item_cost=float(input(f"Enter the cost of the items{i}:"))
            self.Total_cost+= Item_cost
            print(f"{Item_name}  {Item_cost}")
        print(self.Total_cost)
        self.Total_requisition+=1
        #- Returns all info including total cost.
        print("------------")
        return  self.Total_cost

    def requisition_approval(self):
        """
        Determines approval status based on total cost.
        Design Principle: Open/Closed Principle : approval rules can be extended without changing method structure.
        """
        print("------------")
        if self.Total_cost<499:
            self.Status="Approved"
            print(f"Status:{self.Status}")
            self.Total_approved+=1
            self.Reference_NO=self.Staff_ID+self.second
            print(f"Reference Number:{self.Reference_NO}")
        else:
            self.Status="Pending"
            print(f"Status:{self.Status}")
            self.Total_pending+=1
            print(f"Reference Number:-----")
        print("------------")
        return self.Total_cost,self.Reference_NO

    def respond_requisition(self):
        """
        Handles pending requisition responses from staff.
        Design Principle: Separation of Concerns : this method only deals with responding to pending requests.
        """

        print("------------")
        if self.Status.lower() == "pending":
            Respond=input("Do you want to accept the pending requisition?Yes or No:")
            if Respond.lower()=="yes":
                self.Status="Approved"
                print(f"Status:{self.Status}")
                self.Total_approved+=1
                self.Reference_NO=self.Staff_ID+self.second
                print(f"Reference Number:{self.Reference_NO}")
            else:
                self.Status="Not approved"
                print(f"Status:{self.Status}")
                self.Total_not_approved+=1
                self.Reference_NO="-----"
                print(f"Reference Number:{self.Reference_NO}")
        print("------------")
        return self.Status,self.Reference_NO

    def display_requisition(self):
        """
        Displays the details of the current requisition.
        Design Principle: SRP :only responsible for outputting requisition details.
        """

        print("------------")
        print("Printing Requisitions:")
        print(f"Date:{self.Date}")
        print(f"Requisition ID:{self.Requisition_ID}")
        print(f"Staff ID:{self.Staff_ID}")
        print(F"Staff Name:{self.Staff_name}")
        print(f"Total: ${self.Total_cost}")
        print(f"Status:{self.Status}")
        print(f"Approval Reference Number:{self.Reference_NO}")
        print("------------")

    def requisition_statistic(self):  
        """
        Displays statistics of all requisitions processed.
        Design Principle: Information Expert : the class holds and reports its own statistics.
        """
        print("------------")
        print(f"The total number of requisitions submitted: {self.Total_requisition}")
        print(f"The total number of approved requisitions: {self.Total_approved}")
        print(f"The total number of pending requisitions: {self.Total_pending}")
        print(f"The total number of not approved requisitions: {self.Total_not_approved}")
        print("------------")
        # Create a single instance of the system


display = RequisitionSystem()
def main():

    """
    Main workflow for processing a requisition.
    Design Principle: High Cohesion : groups related steps together in a logical sequence.
    """

    display.staff_info()
    display.requisitions_total()
    display.requisition_approval()
    display.respond_requisition()
    display.display_requisition()

# Menu loop for user interaction

while True:
    print("press 1 to add customer")
    print("press  2 to end")
    print("press 3 to display requisition statistics")
    try:
        decision=int(input("Enter: "))
        if decision==1:
            main()
        elif decision==2:
                break
        elif decision==3:
            display.requisition_statistic()
    except ValueError:
        print("wrong input try again")
    print("-------")
