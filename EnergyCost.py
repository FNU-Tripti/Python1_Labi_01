from datetime import date

# Local variable declaration

# Declaration of the variables as float type to accumulate the total charges
import datetime

totalcost = 0.0

# Declaration of thr variable as float type to accumulate the total costPerKiloWatt
totalCostPerKiloWatt = 0.0

# Declaration of the variable as float type to accumulate the total annual usage
totalAnnualusage = 0.0

# Declared average for variance
varianceAverage = 0.1600
varianceTotalItems = 6

# Declaration of variable to calculate the variance
variance = 0.0

# Declaration of variable to calculate the standard deviation
standardDeviation = 0.0

# Declaration of total number of appliances or items
totalItems = 0;

# Declaration of variable to store average
average = 0.0

# Declaration of the variable to store the appliance name
applianceName = ""

# Declaration of the variable for cost per KW - hr
costPerKiloWatt = 0.0

# Declaration of the variable for annual usage
annualUsage = 0.0

print("Program Executed by FNU Tripti (A20503656)" , date.today())
# Data for Appliance #1
print("[ Please enter the requested data for appliance #1 ]")
print("Appliance Name: ")
applianceName = input()

print("Cost per KW - hr of the appliance (in cents):")
costPerKiloWatt = float(input())

# Accumulating total Cost Per Kilowatt
totalCostPerKiloWatt = totalCostPerKiloWatt + costPerKiloWatt



print("Annual usage (in KW - hr):")
annualUsage = float(input())

# Accumulating total annual usage
totalAnnualusage = totalAnnualusage + annualUsage

totalcost = totalcost + (costPerKiloWatt * annualUsage)


# Calculation of Variance
variance = (variance + (varianceAverage - costPerKiloWatt) ** 2) / varianceTotalItems



# Incrementing total number of items
totalItems = totalItems + 1

print("Total Number of items thus far: " + str(totalItems))
print("The total Cost Per Kilo Watt thus far $%.2f" % totalCostPerKiloWatt)
print ("The total cost thus far %.2f" % totalAnnualusage)
print("The total cost thus far $%.2f" % totalcost)
print("The variance calculated thus far is  $%.4f" % variance)


# Data for Appliance #2

print("[ Please enter the requested data for appliance #2 ]")
print("Appliance Name: ")
applianceName = input()

print("Cost per KW - hr of the appliance (in cents):")
costPerKiloWatt = float(input())

# Accumulating total Cost Per Kilowatt
totalCostPerKiloWatt = totalCostPerKiloWatt + costPerKiloWatt

print("Annual usage (in KW - hr):")
annualUsage = float(input())


# Accumulating total annual usage
totalAnnualusage = totalAnnualusage + annualUsage

# Accumulating total Cost Per Kilowatt
totalcost = totalcost + (costPerKiloWatt * annualUsage)

# Incrementing total number of items
totalItems = totalItems + 1

# Calculation of Variance
variance = (variance + (varianceAverage - costPerKiloWatt) ** 2) / varianceTotalItems


print("Total Number of items thus far: " + str(totalItems))
print("The total Cost Per Kilo Watt thus far $%.2f" % totalCostPerKiloWatt)
print ("The total cost thus far %.2f" % totalAnnualusage)
print("The total cost thus far $%.2f" % totalcost)
print("The variance calculated thus far is  $%.4f" % variance)



# Data for appliance #3

print("[ Please enter the requested data for appliance #3]")
print("Appliance Name: ")
applianceName = input()

print("Cost per KW - hr of the appliance (in cents):")
costPerKiloWatt = float(input())

# Accumulating total Cost Per Kilowatt
totalCostPerKiloWatt = totalCostPerKiloWatt + costPerKiloWatt

print("Annual usage (in KW - hr):")
annualUsage = float(input())

# Accumulating total annual usage
totalAnnualusage = totalAnnualusage + annualUsage

# Accumulating total Cost Per Kilowatt
totalcost = totalcost + (costPerKiloWatt * annualUsage)

# Incrementing total number of items
totalItems = totalItems + 1

# Calculation of Variance
variance = (variance + (varianceAverage - costPerKiloWatt) ** 2) / varianceTotalItems


print("Total Number of items thus far: " + str(totalItems))
print("The total Cost Per Kilo Watt thus far $%.2f" % totalCostPerKiloWatt)
print("The total cost thus far %.2f" % totalAnnualusage)
print("The total cost thus far $%.2f" % totalcost)
print("The variance calculated thus far is  $%.4f" % variance)


# Data for appliance # 4
print("[ please enter the requested data for appliance #4]")
print("Appliance Name: ")
applianceName = input()

print("cost per KW - hr of the appliance ( in cents)")
costPerKiloWatt = float(input())

# Accumulating total Cost Per Kilowatt
totalCostPerKiloWatt = totalCostPerKiloWatt + costPerKiloWatt

print("Annual usage (in KW- hr):")
annualUsage = float(input())

# Accumulating total annual usage
totalAnnualusage = totalAnnualusage + annualUsage

# Accumulating total Cost Per Kilowatt
totalcost = totalcost + (costPerKiloWatt * annualUsage)


# Incrementing total number of items
totalItems = totalItems + 1

# Calculation of Variance
variance = (variance + (varianceAverage - costPerKiloWatt) ** 2) / varianceTotalItems


print("Total Number of items thus far: " + str(totalItems))
print("The total Cost Per Kilo Watt thus far $%.2f" % totalCostPerKiloWatt)
print("The total cost thus far %.2f" % totalAnnualusage)
print("The total cost thus far $%.2f" % totalcost)
print("The variance calculated thus far is  $%.4f" % variance)


# Data for appliance #5
print("[please  entered the requested data for appliance #5]")
print("Appliance Name: ")
applianceName = input()

print("cost per KW - hr of the appliance ( in cents)")
costPerKiloWatt = float(input())

# Accumulating total Cost Per Kilowatt
totalCostPerKiloWatt = totalCostPerKiloWatt + costPerKiloWatt

print("Annual usages(in KW - hr):")
annualUsage = float(input())

# Accumulating total annual usage
totalAnnualusage = totalAnnualusage + annualUsage

# Accumulating total Cost Per Kilowatt
totalcost = totalcost + (costPerKiloWatt * annualUsage)


# Incrementing total number of items
totalItems = totalItems + 1

# Calculation of Variance
variance = (variance + (varianceAverage - costPerKiloWatt) ** 2) / varianceTotalItems

print("Total Number of items thus far: " + str(totalItems))
print("The total Cost Per Kilo Watt thus far $%.2f" % totalCostPerKiloWatt)
print("The total cost thus far %.2f" % totalAnnualusage)
print("The total cost thus far $%.2f" % totalcost)
print("The variance calculated thus far is  $%.4f" % variance)



# Data for appliance #6

print("[please  entered the requested data for appliance #6]")
print("Appliance Name: ")
applianceName = input()

print("cost per KW - hr of the appliance ( in cents)")
costPerKiloWatt = float(input())

# Accumulating total Cost Per Kilowatt
totalCostPerKiloWatt = totalCostPerKiloWatt + costPerKiloWatt

print("Annual usages(in KW - hr):")
annualUsage = float(input())

# Accumulating total annual usage
totalAnnualusage = totalAnnualusage + annualUsage

# Accumulating total Cost Per Kilowatt
totalcost = totalcost + (costPerKiloWatt * annualUsage)


# Incrementing total number of items
totalItems = totalItems + 1

# Calculation of Variance
variance = (variance + (varianceAverage - costPerKiloWatt) ** 2) / varianceTotalItems



print("Total Number of items thus far: " + str(totalItems))
print("The total Cost Per Kilo Watt $%.2f" % totalCostPerKiloWatt)
print("The total cost thus far %.2f" % totalAnnualusage)
print("The total cost  $%.2f" % totalcost)
print("The variance calculated thus far is  $%.4f" % variance)

print("Calculating the average cost of the Power.")
print("The formula of the average of the power is: totalCostPerKiloWatt / totalItems")

average = totalCostPerKiloWatt / totalItems

print("The average cost of the power is $%.4f" % average)

standardDeviation = variance ** .5

print("The Standard Deviation is $%.4f" % standardDeviation)

print("Program Executed by FNU Tripti (A20503656)" , date.today())

















