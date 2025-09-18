
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


##  Folder Structure

Software design principles were used.

### 1. Single responsibilities The single responsibilities principle (SRP) means that each object focuses on a specific task(s).
- There is one purpose of every method in the `RequisitionSystem` class:
- `staff_info()` → Generates staff information.
- `requisition total()` → Gathering of item information and cost calculation.
- `requisition approval()` -->Status of approval.
- `respond_requisition()` → Responds to outstanding requisition requests.
- display requisition () - Displays requisition information.
- `requisition_statistic()` → Displays the total statistics.
- **Enhancement: Repetition of input validation logic in more than one way - may be consolidated in a helper function.
  

### 2. **Encapsulation**
- All the data concerning requisitions is agented in the form of attributes in the RequisitionSystem class.
- **Enhancement: Turn attributes private (i.e. self. total cost) and access them via getters/setters.


### 3. **DRY (Don't Repeat Yourself)**
- The program does not duplicate some areas unnecessarily, but:
- Checking of empty strings is redundantly executed in various ways.
- It may be re-written into one reusable validation.

### 4. **Open/Closed Principle**
- In requisition approval One can add additional approval levels to the approval logic in requisition approval without changing the structure of the method.
- This renders the system to changes.


### 5. **Separation of Concerns**
- Display methods (`display_requisition()` and `requisition statistic) are distinctly different to processing methods.
- This division enhances maintainability and readability.


### 6. **Information Expert**
- RequisitionSystem is the class that keeps and records its statistics.
- This maintains related information and behavior in a single code and makes the code more cohesive.


### 7. **High Cohesion**
- The main() method is used to cluster steps associated together in a logical order that enhances the business flow and program readability.


##  How to Run
1. Install Python 3.x
2. Clone this repository:
```bash
git clone https://github.com/your username/ requisition-system.git.

