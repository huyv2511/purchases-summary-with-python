import csv
from purChase import purChase

purchaseList=[]
purchaseDict = {

}
# def openCVFile(filename):
#   print("Hi")
#   with open(filename, newline = '') as csvfile:
#     print("Opening file")

with open('C:\\Users\\vanta\\OneDrive\\Desktop\\Coding\\python\\tyler\\credit_card_2020.csv', newline='') as csvfile:
    sum = 0.0
    number_of_purchases = 0
    reader = csv.DictReader(csvfile)
    for row in reader:
      p = purChase(row['category'],float(row['price']))
      purchaseList.append(p)
      
  
      if purchaseDict.__contains__(row['category']) == False:
        purchaseDict[row['category']] = float(row['price'])
      else:
        purchaseDict[row['category']] = float(purchaseDict[row['category']]) +float(row['price'])

      sum = float(row['price']) + sum
      number_of_purchases +=1
   

    print("total cost of purchases is:" + str(sum))
    print("Number of purchases is: "+str(purchaseList.__sizeof__))
    print("----------------------------------")

for p in purchaseDict:
  totalCost = purchaseDict[p]
  print("Total cost for " + p + " is " + str(totalCost))


print("----------------------------------")

for p in purchaseDict:
  total = 0
  for i in purchaseList:
    if p == i.category:
      total+=1
  print("Total number of purchases for " + p + " is "+ str(total))
  
print("----------------------------------")



high = purchaseList[0].price
low = float(purchaseList[0].price)




for p in purchaseList:
  curPrice = float(p.price)
  if(curPrice> high):
    high = curPrice
for p in purchaseList:
  curPrice = float(p.price)
  if(curPrice<low):
    low = curPrice


highSet = set()
for p in purchaseList:
  curPrice = float(p.price)
  if(curPrice == high):
    highSet.add(p.category)
print("Purchase with highest price and its category is " + str(high) + " " + str(highSet))
lowSet = set()
for p in purchaseList:
  curPrice = float(p.price)
  if(curPrice == low):
    lowSet.add(p.category)
print("Purchase with lowest price and its category is " + str(low) + " " + str(lowSet))

