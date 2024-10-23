#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #: w0457754    
#Student Name: William Wilson

def main():
    #welcome message
    print("Welcome to Geoff's Landscaping Company. My name is William and I am one of his contractors. To get you a quote, can I get you to enter your house number and your yard's length and width? ")

    #set base rate
    baseCharge = 1000.00

    #start gathering some user input
    houseNumber = input("Please enter your house number: ")
    length = float(input("Please enter the length of your yard: "))
    width = float(input("Please enter the width of your yard: "))

    #calculate square footage and any additional math for square feet
    squareFoot = length * width

    if squareFoot < 5000:
        squareFootcost = 500
    elif squareFoot >= 5000:
        squareFootcost = 0

    #gather grass type
    grassStyle = input("Please enter the type of grass you want to use (fescue, bentgrass, campus): ")
    fescue = 0.05
    bentgrass = 0.02
    campus = 0.01

    if grassStyle == "fescue":
        cost = fescue 
    elif grassStyle == "bentgrass": 
            cost = bentgrass   
    elif grassStyle == "campus":
            cost = campus

    #calculate grasscost with square feet
    grassCost = squareFoot * cost

    #collect number of trees wanted and calculate cost of trees
    numberOfTrees = int(input("Please the number of trees that you would like to have planted: "))

    if numberOfTrees == 0:
        treeCost = 0
    else:
        treeCost = numberOfTrees * 100

    #calculate grand total cost
    grandTotal = baseCharge + squareFootcost + grassCost + float(treeCost)

    #display cost to user
    print("The grandtotal cost for house number {0} will be: ${1:.2f}".format(houseNumber, grandTotal))

main()