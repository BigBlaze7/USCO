'''
ID: jackson40
LANG: PYTHON3
TASK: milk
'''

def readinput():
    n = open('milk.in')
    data = n.readlines()
    n.close()
    numUnits = int(data[0].split()[0])
    numFarmers = int(data[0].split()[1])

    farmersPrices = {}
    for i in range(1,numFarmers + 1):
      localprice = int(data[i].split()[0])
      localunits = int(data[i].split()[1])

      if localprice in farmersPrices:
        farmersPrices[localprice] += localunits
      else:
        farmersPrices[localprice] = localunits

    return numUnits, farmersPrices

def price(numUnits, farmersPrices):
  priceOrder = []
  order = 0
  for i in sorted(farmersPrices.keys()):
    priceOrder.append(i)
    order += 1
  return priceOrder

farmer = 0
priceOfCowWater = 0
order = 0

numUnits, farmersPrices = readinput()
# price(numUnits, farmersPrices)
# print(farmersPrices)
priceOrder = price(numUnits, farmersPrices)
print(priceOrder)

for i in range(numUnits):
  if farmersPrices[priceOrder[order]] > 0:
      farmer += priceOrder[order]
      farmersPrices[priceOrder[order]] -= 1
  elif farmersPrices[priceOrder[order]] == 0:
      order += 1
      farmersPrices[priceOrder[order]] -= 1
      farmer += priceOrder[order]
print(farmer)

o = open('milk.out', 'w+')
o.write(str(farmer))
o.close()
