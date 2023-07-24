# Program written by Ramsha Ishtiaque
# Written on : 20th July 2023

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


# Main program

JanSales = int(input("Total sales for the month of January: "))
FebSales = int(input("Total sales for the month of February: "))
MarchSales = int(input("Total sales for the month of March: "))
AprSales = int(input("Total sales for the month of April: "))
MaySales = int(input("Total sales for the month of May: "))
JuneSales = int(input("Total sales for the month of June: "))
JulySales = int(input("Total sales for the month of July: "))
AugSales = int(input("Total sales for the month of August: "))
SepSales = int(input("Total sales for the month of September: "))
OctSales = int(input("Total sales for the month of October: "))
NovSales = int(input("Total sales for the month of November: "))
DecSales = int(input("Total sales for the month of December: "))

x_axis = ["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = [JanSales, FebSales, MarchSales, AprSales, MaySales, JuneSales, JulySales, AugSales, SepSales, OctSales, NovSales, DecSales]


fig, ax = plt.subplots()

ax.bar(x_axis, y_axis, align='center')

ax.set_title('Sales in 2022')
ax.set_ylabel('Total Sales ($)')
ax.set_xlabel('Months')

ax.set_xticks(x_axis)
ax.set_xticklabels(("Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"))

plt.show()






