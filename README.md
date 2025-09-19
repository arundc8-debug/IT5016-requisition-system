# Requisition System

##  Overview
This Python program simulates a requisition management system for staff purchases.  
It allows staff to:
- Enter personal and requisition details
- Add items and calculate total costs
- Determine approval status based on cost thresholds
- Respond to pending requisitions
- View requisition statistics

The program demonstrates **object-oriented programming** and applies several **software design principles**.


## Software design principles  used.

### 1. Single responsibilities : The single responsibilities principle (SRP) means that each object focuses on a specific task(s).

- There is one purpose of every method in the `RequisitionSystem` class:
- `staff_info()` - Generates staff information.
- `requisition total()` - Gathering of item information and cost calculation.
- `requisition approval()` -Status of approval.
- `respond_requisition()` - Responds to outstanding requisition requests.
- `display requisition ()` - Displays requisition information.
- `requisition_statistic()` - Displays the total statistics.
- Enhancement : Repetition of input validation logic in more than one way - may be consolidated in a helper function.
  

### 2. **Encapsulation -  keeping an object’s data and  methods that work on that data together, and controlling access to that data so it can’t be changed in unexpected ways.**

- All the data concerning requisitions is agented in the form of attributes in the RequisitionSystem class.
- Enhancement : Turn attributes private (i.e. self. total cost) and access them via getters/setters.


### 3. **DRY (Don't Repeat Yourself) - avoiding duplicate code by reusing methods or functions, so changes only need to be made in one place.**

- The program does not duplicate some areas unnecessarily, but:
- Checking of empty strings is redundantly executed in various ways.
- It may be re-written into one reusable validation.

### 4. **Open/Closed Principle - means code should be open to add new features but should be closed to changing existing code, so you can extend functionality without breaking what already works.**

- In requisition approval One can add additional approval levels to the approval logic in requisition approval without changing the structure of the method.
- This renders the system to changes.


### 5. **Separation of Concerns - Divides a program into different sections, where each section deals with a specific type of work, such as processing data or displaying results.**

- Display methods (`display_requisition()` and `requisition statistic) are distinctly different to processing methods.
- This division enhances maintainability and readability.


### 6. **Informations - This gives a task to the part of the program that already has the information needed to do it, so it can work without relying on other parts.**

- RequisitionSystem is the class that keeps and records its statistics.
- This maintains related information and behavior in a single code and makes the code more cohesive.


### 7. **High Cohesion - means keeping related tasks and data together in the same part of the program, so that part is focused and easy to understand.**

- The main() method is used to cluster steps associated together in a logical order that enhances the business flow and program readability.



