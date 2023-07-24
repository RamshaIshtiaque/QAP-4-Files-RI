# Program written for One Stop Insurance Company by Ramsha Istiaque.
# Written on 16th June 2023

# Import required libraries
import datetime
import time
from tqdm import tqdm

# Open the defaults file and read the values into variables
f = open('OSICDef.dat', 'r')
NEXT_POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
DISC_ADD_CARS = float(f.readline())
EXTRA_LIAB_COVERAGE = float(f.readline())
GLASS_COVERAGE = float(f.readline())
LOANER_CAR_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())
f.close()

# Main Program
# User inputs
while True:
    CustFirstName = input("Enter the customer's first name (End to quit) : ").title()
    if CustFirstName == "End":
        break
    CustLastName = input("Enter the customer's last name: ").title()
    StAddress = input("Enter the street address: ")
    CityName = input("Enter the city's name: ").title()

    while True:
        list = ["NL", "PE", "NS", "NB", "ON", "QC", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
        Prov = input("Enter the province (LL): ").upper()
        if Prov == "":
            print("Error - Province cannot be blank")
        elif len(Prov) != 2:
            print("Error - Province must have only 2 characters.")
        elif Prov not in list:
            print("Error - Province is invalid.")
        else:
            break

    PostalCode = input("Enter the postal code: ")
    PhoneNum = input("Enter phone number: ")

    CarsInsured = int(input("Enter the number of cars being insured: "))
    ExtraLiability = input("Enter Y for Yes or N for No for extra liability: ").upper()
    GlassCoverage = input("Enter Y for Yes or N for No for glass coverage: ").upper()
    LoanerCar = input("Enter Y for Yes or N for No for loaner car: ").upper()

    while True:
        list2 = ["Full", "Monthly"]
        PayMethod = input("Enter the payment method (Full/Monthly): ").title()
        if PayMethod not in list2:
            print("Error - Choose one of the methods specified")
        else:
            break

    # Calculations
    if CarsInsured == "1":
        InsurancePremium = BASIC_PREMIUM
    else:
        InsurancePremium = BASIC_PREMIUM + ((BASIC_PREMIUM - (DISC_ADD_CARS * BASIC_PREMIUM)) * (CarsInsured - 1))

    if ExtraLiability == "Y":
        LiabilityCosts = EXTRA_LIAB_COVERAGE * CarsInsured
    else:
        LiabilityCosts = 0

    if GlassCoverage == "Y":
        GlassCoverageCosts = GLASS_COVERAGE * CarsInsured
    else:
        GlassCoverageCosts = 0

    if LoanerCar == "Y":
        LoanerCarCosts = LOANER_CAR_COVERAGE * CarsInsured
    else:
        LoanerCarCosts = 0

    ExtraCosts = LiabilityCosts + GlassCoverageCosts + LoanerCarCosts
    TotInsurancePremium = ExtraCosts + InsurancePremium
    HST = HST_RATE * TotInsurancePremium
    TotCost = TotInsurancePremium + HST

    if PayMethod == "Monthly":
        MonthlyPayment = (TotCost + PROCESSING_FEE) / 8
        MonthlyPaymentDsp = f"${MonthlyPayment:,.2f}"

    InvDateTime = datetime.datetime.now()
    InvDate = InvDateTime.date()
    NextPayDateTime = (datetime.datetime(year=InvDate.year, month=InvDate.month + 1, day=1))
    NextPayDate = NextPayDateTime.date()

    InsurancePremiumDsp = f"${InsurancePremium:,.2f}"
    ExtraCostsDsp = f"${ExtraCosts:,.2f}"
    TotInsurancePremiumDsp = f"${TotInsurancePremium:,.2f}"
    HSTDsp = f"${HST:,.2f}"
    TotCostDsp = f"${TotCost:,.2f}"


    print()
    print()
    print("                                 ONE STOP INSURANCE COMPANY")
    print("-----------------------------------------------------------------------------------------------")
    print(f"        Policy Number:                 {NEXT_POLICY_NUM:>4d}  Invoice Date:                  {InvDate}")
    print()
    print(f"        Customer Name:                 {CustFirstName:<8s} {CustLastName:<8s}")
    print(f"        Address:                       {StAddress:<15s}, {CityName:<10s}, {Prov:<2s}, {PostalCode:<6s}.")
    print()
    print("-----------------------------------------------------------------------------------------------")
    print()
    print(f"                     Number of cars being insured:  {CarsInsured:>2d}")
    print(f"                     Extra Liability:               {ExtraLiability:<1s}")
    print(f"                     Glass Coverage:                {GlassCoverage:<1s}")
    print(f"                     Loaner Car:                    {LoanerCar:<1s}")
    print()
    print("-----------------------------------------------------------------------------------------------")
    print()
    print(f"                     Insurance Premium:             {InsurancePremiumDsp:<9s}")
    print(f"                     Extra Costs:                   {ExtraCostsDsp:<9s}")
    print(f"                     Total Insurance Premium:       {TotInsurancePremiumDsp:<9s}")
    print(f"                     HST:                           {HSTDsp:<9s}")
    print(f"                     Total Cost:                    {TotCostDsp:<9s}")
    print()
    print("-----------------------------------------------------------------------------------------------")
    print()
    print(f"                     Payment Method:                {PayMethod:<7s}")

    if PayMethod == "Monthly":
        print(f"                     Monthly Payment:               {MonthlyPaymentDsp:<9s}")

    print(f"                     Next Payment Date:             {NextPayDate}")
    print()
    print("-----------------------------------------------------------------------------------------------")
    print()
    print()
    print("Saving data - please wait")
    print()

    # Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)

    print()

    # Write the values to a file for future reference.
    f = open("Policies.dat", "a")
    f.write(f"{NEXT_POLICY_NUM}, ")
    f.write(f"{InvDate}, ")
    f.write(f"{CustFirstName} {CustLastName}, ")
    f.write(f"{StAddress} {CityName}, {Prov}, {PostalCode}, ")
    f.write(f"{CarsInsured}, ")
    f.write(f"{ExtraLiability}, ")
    f.write(f"{GlassCoverage}, ")
    f.write(f"{LoanerCar}, ")
    f.write(f"{PayMethod}, ")
    f.write(f"{TotInsurancePremium}\n")
    f.close()
    print("Policy information processed and saved.")

    # Update any default values based on the processing requirements
    NEXT_POLICY_NUM += 1

    # Write the current values back t the default file. Note the use of “w” to overwrite and the use of
    # the \n so that each value is placed on a separate line.
    f = open('OSICDef.dat', 'w')
    f.write(f"{NEXT_POLICY_NUM}\n")
    f.write(f"{BASIC_PREMIUM}\n")
    f.write(f"{DISC_ADD_CARS}\n")
    f.write(f"{EXTRA_LIAB_COVERAGE}\n")
    f.write(f"{GLASS_COVERAGE}\n")
    f.write(f"{LOANER_CAR_COVERAGE}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESSING_FEE}\n")
    f.close()
