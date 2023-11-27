# Optimal Packing Structures

import math
import random
import matplotlib.pyplot as plt

plt.show()

coins = []
coinss = []
time = 0

Length = int (input("Enter integer length of box: "))
Width = int (input("Enter integer width of box: "))

radius = int (input("Enter integer radius of coin: "))
diameter = radius * 2

if(((Length) % diameter == 0) and ((Width) % diameter == 0) and Length*Width/(diameter*diameter) <= 49): # when square packing is optimal
  coin_amount = (Length/diameter) * (Width/diameter)
  x_axis = radius
  y_axis = radius
  coin, dimension = plt.subplots()

  plt.xlim(0, Width)
  plt.ylim(0, Length)

  dimension.set_aspect(1)

  x_axis1 = x_axis # new variables so I can increment without affecting original
  x_axis2 = x_axis
  y_axis1 = y_axis
  y_axis2 = y_axis

  range_x1 = int ((Width - x_axis) * (100*radius)) # multiplication because no decimal in later for loop
  range_x2 = int (x_axis * 100*radius)
  range_y1 = int ((Length - y_axis) * 100*radius)
  range_y2 = int (y_axis * 100*radius)

  shift1 = 0
  shift2 = 0

  a = 0
  x__axis = x_axis
  for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
    if (x__axis <= (Width - radius) and x__axis >= radius):
      dimension.add_artist(plt.Circle((x__axis, y_axis), radius))
      coinss.append((x__axis, y_axis))
    x__axis += diameter # all the coins to the right of the original

  x = 0
  while (x <= range_x1-radius):
    for y in range(0,range_y1*1000*radius,1000*radius):
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis1 + shift2) <= (Length - radius)and (y_axis1 + shift2) >= radius):
        dimension.add_artist(plt.Circle((x_axis1 + shift1, y_axis1 + shift2), radius))
        coinss.append((x_axis1 + shift1, y_axis1 + shift2))
      y_axis1 += diameter
    for y in range(2000*radius,range_y2*1000*radius,1000*radius): # adding all the coins vertically in square pattern
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis2 - shift2) <= (Length - radius)and (y_axis2 - shift2) >= radius):
        dimension.add_artist(plt.Circle((x_axis1 + shift1, y_axis2 - shift2), radius))
        coinss.append((x_axis1 + shift1, y_axis2 - shift2))
      y_axis2 -= diameter
    y_axis1 = y_axis
    y_axis2 = y_axis
    x_axis1 += diameter
    x += 10*radius
  coin_area = coin_amount * math.pi * (radius**2)

elif (((Length) / radius == 5) and ((Width) / radius == 5)): # specific case when there is a coin in only the center and corners
  coin_amount = 0
  coin, dimension = plt.subplots()
  plt.xlim(0, Width)
  plt.ylim(0, Length)
  dimension.set_aspect(1)

  coinss.append((radius, radius))
  dimension.add_artist(plt.Circle((radius, radius), radius)) # corner coin
  coin_amount += 1
  coinss.append((Width-radius, radius))
  dimension.add_artist(plt.Circle((Width-radius, radius), radius)) # corner coin
  coin_amount += 1
  coinss.append((radius, Length-radius))
  dimension.add_artist(plt.Circle((radius, Length-radius), radius)) # corner coin
  coin_amount += 1
  coinss.append((Width-radius, Length-radius))
  dimension.add_artist(plt.Circle((Width-radius, Length-radius), radius)) # corner coin
  coin_amount += 1
  coinss.append((2.5*radius, 2.5*radius))
  dimension.add_artist(plt.Circle((2.5*radius, 2.5*radius), radius)) # center coin
  coin_amount += 1

  coins.append(coin_amount) # add each coin amount to a list
  coin_area = coin_amount * math.pi * (radius**2) # total coin area

else: # a form of hexagonal packing is optimal
  coin_amount = 0

  x_axis = radius
  y_axis = radius
  coin, dimension = plt.subplots()

  plt.xlim(0, Width)
  plt.ylim(0, Length)

  dimension.set_aspect(1)

  x_axis1 = x_axis # new variables so I can increment without affecting original
  x_axis2 = x_axis
  y_axis1 = y_axis
  y_axis2 = y_axis

  range_x1 = int ((Width - x_axis) * (100*radius)) # multiplication because no decimal in later for loop
  range_x2 = int (x_axis * 100*radius)
  range_y1 = int ((Length - y_axis) * 100*radius)
  range_y2 = int (y_axis * 100*radius)

  shift2 = math.sqrt(3) / 2 * diameter # to make hexagonal pattern
  shift1 = 0 # shift1 later becomes radius

  a = 0
  x__axis = x_axis
  for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
    if (x__axis <= (Width - radius) and x__axis >= radius):
      coinss.append((x__axis, y_axis))
      coin_amount += 1
    x__axis += diameter # all the coins to the right of the original

  x = 0
  while (x <= range_x1-radius):
    for y in range(0,range_y1*1000*radius,1000*radius):
      if ((y/(1000*radius))%2 == 0):
        shift1 = radius # every other row needs to be moved up
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis1 + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis1 + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        coinss.append((x_axis1 + shift1, y_axis1 + shift2-(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1 # if it can fit in the box
      y_axis1 += diameter
    for y in range(2000*radius,range_y2*1000*radius,1000*radius): # adding all the coins vertically in hexagon pattern
      if ((y/1000)%2 == 0):
        shift1 = radius
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis2 - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis2 - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        coinss.append((x_axis1 + shift1, y_axis2 - shift2+(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1
      y_axis2 -= diameter
    y_axis1 = y_axis
    y_axis2 = y_axis
    x_axis1 += diameter
    x += 10*radius


  coins.append(coin_amount) # add each coin amount to a list

  # try combining rectangular and hexagonal packing
  coin_amount = 0
  plots = []
  x_axis = radius
  y_axis = radius

  x_axis1 = x_axis # new variables so I can increment without affecting original
  x_axis2 = x_axis
  y_axis1 = y_axis
  y_axis2 = y_axis

  range_x1 = int ((Width - x_axis) * (100*radius)) # multiplication because no decimal in later for loop
  range_x2 = int (x_axis * 100*radius)
  range_y1 = int ((Length - y_axis) * 100*radius)
  range_y2 = int (y_axis * 100*radius)

  shift2 = math.sqrt(3) / 2 * diameter # to make hexagonal pattern
  shift1 = 0 # shift1 later becomes radius

  a = 0 # first horizontal row of coins
  x__axis = x_axis
  for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
    if (x__axis <= (Width - radius) and x__axis >= radius):
      plots.append((x__axis, y_axis))
      coin_amount += 1
    x__axis += diameter # all the coins to the right of the original
  a = 0
  x__axis = x_axis # second horizontal row in rectangular packing
  y_axis += diameter
  if (y_axis <= Length - radius):
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plots.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  y_axis -= diameter
  x = 0 # then start hexagonal packing, to make a modified hexagonal packing structure
  while (x <= range_x1-radius):
    for y in range(0,range_y1*1000*radius,1000*radius):
      if ((y/(1000*radius))%2 == 0):
        shift1 = radius # every other row needs to be moved up
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis1 + diameter + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis1 + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plots.append((x_axis1 + shift1, y_axis1 + diameter + shift2-(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1 # if it can fit in the box, add the coin
      y_axis1 += diameter
    for y in range(2000*radius,range_y2*1000*radius,1000*radius): # adding all the coins vertically in hexagon pattern
      if ((y/1000)%2 == 0):
        shift1 = radius
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis2 + diameter - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis2 - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plots.append((x_axis1 + shift1, y_axis2 + diameter - shift2+(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1
      y_axis2 -= diameter
    y_axis1 = y_axis
    y_axis2 = y_axis
    x_axis1 += diameter
    x += 10*radius

  coins.append(coin_amount) # add each coin amount to a list

  # three rows of rectangular before hexagonal packing
  coin_amount = 0
  plotss = []
  x_axis = radius
  y_axis = radius

  x_axis1 = x_axis # new variables so I can increment without affecting original
  x_axis2 = x_axis
  y_axis1 = y_axis
  y_axis2 = y_axis

  range_x1 = int ((Width - x_axis) * (100*radius)) # multiplication because no decimal in later for loop
  range_x2 = int (x_axis * 100*radius)
  range_y1 = int ((Length - y_axis) * 100*radius)
  range_y2 = int (y_axis * 100*radius)

  shift2 = math.sqrt(3) / 2 * diameter # to make hexagonal pattern
  shift1 = 0 # shift1 later becomes radius

  a = 0 # first horizontal row of coins
  x__axis = x_axis
  for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
    if (x__axis <= (Width - radius) and x__axis >= radius):
      plotss.append((x__axis, y_axis))
      coin_amount += 1
    x__axis += diameter # all the coins to the right of the original
  a = 0
  number = 0
  x__axis = x_axis # second horizontal row in rectangular packing
  y_axis += diameter
  if (y_axis <= Length - radius):
    number = 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # third horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  y_axis -= diameter
  y_axis -= diameter
  x = 0 # then start hexagonal packing, to make a modified hexagonal packing structure
  while (x <= range_x1-radius):
    for y in range(0,range_y1*1000*radius,1000*radius):
      if ((y/(1000*radius))%2 == 0):
        shift1 = radius # every other row needs to be moved up
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis1 + number*diameter + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis1 + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotss.append((x_axis1 + shift1, y_axis1 + number*diameter + shift2-(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1 # if it can fit in the box, add the coin
      y_axis1 += diameter
    for y in range(2000*radius,range_y2*1000*radius,1000*radius): # adding all the coins vertically in hexagon pattern
      if ((y/1000)%2 == 0):
        shift1 = radius
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis2 + number*diameter - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis2 - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotss.append((x_axis1 + shift1, y_axis2 + number*diameter - shift2+(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1
      y_axis2 -= diameter
    y_axis1 = y_axis
    y_axis2 = y_axis
    x_axis1 += diameter
    x += 10*radius

  coins.append(coin_amount) # add each coin amount to a list

  # try combining rectangular and hexagonal packing with four rectangular rows
  coin_amount = 0
  plotsss = []
  x_axis = radius
  y_axis = radius

  x_axis1 = x_axis # new variables so I can increment without affecting original
  x_axis2 = x_axis
  y_axis1 = y_axis
  y_axis2 = y_axis

  range_x1 = int ((Width - x_axis) * (100*radius)) # multiplication because no decimal in later for loop
  range_x2 = int (x_axis * 100*radius)
  range_y1 = int ((Length - y_axis) * 100*radius)
  range_y2 = int (y_axis * 100*radius)

  shift2 = math.sqrt(3) / 2 * diameter # to make hexagonal pattern
  shift1 = 0 # shift1 later becomes radius

  a = 0 # first horizontal row of coins
  x__axis = x_axis
  for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
    if (x__axis <= (Width - radius) and x__axis >= radius):
      plotsss.append((x__axis, y_axis))
      coin_amount += 1
    x__axis += diameter # all the coins to the right of the original
  a = 0
  number = 0
  x__axis = x_axis # second horizontal row in rectangular packing
  y_axis += diameter
  if (y_axis <= Length - radius):
    number = 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotsss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # third horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotsss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # fourth horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotsss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  x = 0 # then start hexagonal packing, to make a modified hexagonal packing structure
  while (x <= range_x1-radius):
    for y in range(0,range_y1*1000*radius,1000*radius):
      if ((y/(1000*radius))%2 == 0):
        shift1 = radius # every other row needs to be moved up
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis1 + number*diameter + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis1 + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotsss.append((x_axis1 + shift1, y_axis1 + number*diameter + shift2-(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1 # if it can fit in the box, add the coin
      y_axis1 += diameter
    for y in range(2000*radius,range_y2*1000*radius,1000*radius): # adding all the coins vertically in hexagon pattern
      if ((y/1000)%2 == 0):
        shift1 = radius
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis2 + number*diameter - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis2 - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotsss.append((x_axis1 + shift1, y_axis2 + number*diameter - shift2+(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1
      y_axis2 -= diameter
    y_axis1 = y_axis
    y_axis2 = y_axis
    x_axis1 += diameter
    x += 10*radius

  coins.append(coin_amount) # add each coin amount to a list

  # five rows of rectangular before hexagonal packing
  coin_amount = 0
  plotssss = []
  x_axis = radius
  y_axis = radius

  x_axis1 = x_axis # new variables so I can increment without affecting original
  x_axis2 = x_axis
  y_axis1 = y_axis
  y_axis2 = y_axis

  range_x1 = int ((Width - x_axis) * (100*radius)) # multiplication because no decimal in later for loop
  range_x2 = int (x_axis * 100*radius)
  range_y1 = int ((Length - y_axis) * 100*radius)
  range_y2 = int (y_axis * 100*radius)

  shift2 = math.sqrt(3) / 2 * diameter # to make hexagonal pattern
  shift1 = 0 # shift1 later becomes radius

  a = 0 # first horizontal row of coins
  x__axis = x_axis
  for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
    if (x__axis <= (Width - radius) and x__axis >= radius):
      plotssss.append((x__axis, y_axis))
      coin_amount += 1
    x__axis += diameter # all the coins to the right of the original
  a = 0
  number = 0
  x__axis = x_axis # second horizontal row in rectangular packing
  y_axis += diameter
  if (y_axis <= Length - radius):
    number = 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # third horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # fourth horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # fifth horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  x = 0 # then start hexagonal packing, to make a modified hexagonal packing structure
  while (x <= range_x1-radius):
    for y in range(0,range_y1*1000*radius,1000*radius):
      if ((y/(1000*radius))%2 == 0):
        shift1 = radius # every other row needs to be moved up
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis1 + number*diameter + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis1 + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotssss.append((x_axis1 + shift1, y_axis1 + number*diameter + shift2-(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1 # if it can fit in the box, add the coin
      y_axis1 += diameter
    for y in range(2000*radius,range_y2*1000*radius,1000*radius): # adding all the coins vertically in hexagon pattern
      if ((y/1000)%2 == 0):
        shift1 = radius
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis2 + number*diameter - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis2 - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotssss.append((x_axis1 + shift1, y_axis2 + number*diameter - shift2+(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1
      y_axis2 -= diameter
    y_axis1 = y_axis
    y_axis2 = y_axis
    x_axis1 += diameter
    x += 10*radius

  coins.append(coin_amount) # add each coin amount to a list

  # six rows of rectangular before hexagonal packing
  coin_amount = 0
  plotsssss = []
  x_axis = radius
  y_axis = radius

  x_axis1 = x_axis # new variables so I can increment without affecting original
  x_axis2 = x_axis
  y_axis1 = y_axis
  y_axis2 = y_axis

  range_x1 = int ((Width - x_axis) * (100*radius)) # multiplication because no decimal in later for loop
  range_x2 = int (x_axis * 100*radius)
  range_y1 = int ((Length - y_axis) * 100*radius)
  range_y2 = int (y_axis * 100*radius)

  shift2 = math.sqrt(3) / 2 * diameter # to make hexagonal pattern
  shift1 = 0 # shift1 later becomes radius

  a = 0 # first horizontal row of coins
  x__axis = x_axis
  for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
    if (x__axis <= (Width - radius) and x__axis >= radius):
      plotsssss.append((x__axis, y_axis))
      coin_amount += 1
    x__axis += diameter # all the coins to the right of the original
  a = 0
  number = 0
  x__axis = x_axis # second horizontal row in rectangular packing
  y_axis += diameter
  if (y_axis <= Length - radius):
    number = 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotsssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # third horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotsssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # fourth horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotsssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # fifth horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotsssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # sixth horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotsssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  x = 0 # then start hexagonal packing, to make a modified hexagonal packing structure
  while (x <= range_x1-radius):
    for y in range(0,range_y1*1000*radius,1000*radius):
      if ((y/(1000*radius))%2 == 0):
        shift1 = radius # every other row needs to be moved up
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis1 + number*diameter + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis1 + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotsssss.append((x_axis1 + shift1, y_axis1 + number*diameter + shift2-(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1 # if it can fit in the box, add the coin
      y_axis1 += diameter
    for y in range(2000*radius,range_y2*1000*radius,1000*radius): # adding all the coins vertically in hexagon pattern
      if ((y/1000)%2 == 0):
        shift1 = radius
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis2 + number*diameter - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis2 - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotsssss.append((x_axis1 + shift1, y_axis2 + number*diameter - shift2+(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1
      y_axis2 -= diameter
    y_axis1 = y_axis
    y_axis2 = y_axis
    x_axis1 += diameter
    x += 10*radius

  coins.append(coin_amount) # add each coin amount to a list

  # seven rows of rectangular before hexagonal packing
  coin_amount = 0
  plotssssss = []
  x_axis = radius
  y_axis = radius

  x_axis1 = x_axis # new variables so I can increment without affecting original
  x_axis2 = x_axis
  y_axis1 = y_axis
  y_axis2 = y_axis

  range_x1 = int ((Width - x_axis) * (100*radius)) # multiplication because no decimal in later for loop
  range_x2 = int (x_axis * 100*radius)
  range_y1 = int ((Length - y_axis) * 100*radius)
  range_y2 = int (y_axis * 100*radius)

  shift2 = math.sqrt(3) / 2 * diameter # to make hexagonal pattern
  shift1 = 0 # shift1 later becomes radius

  a = 0 # first horizontal row of coins
  x__axis = x_axis
  for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
    if (x__axis <= (Width - radius) and x__axis >= radius):
      plotssssss.append((x__axis, y_axis))
      coin_amount += 1
    x__axis += diameter # all the coins to the right of the original
  a = 0
  number = 0
  x__axis = x_axis # second horizontal row in rectangular packing
  y_axis += diameter
  if (y_axis <= Length - radius):
    number = 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # third horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # fourth horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # fifth horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # sixth horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  x__axis = x_axis # seventh horizontal row in rectangular packing
  y_axis += diameter
  a = 0
  if (y_axis <= Length - radius):
    number += 1
    for a in range (0,range_x1*100*radius,100*radius): # no decimal allowed for range, so increment by 100
      if (x__axis <= (Width - radius) and x__axis >= radius):
        plotssssss.append((x__axis, y_axis))
        coin_amount += 1
      x__axis += diameter # all the coins to the right of the original
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  y_axis -= diameter
  x = 0 # then start hexagonal packing, to make a modified hexagonal packing structure
  while (x <= range_x1-radius):
    for y in range(0,range_y1*1000*radius,1000*radius):
      if ((y/(1000*radius))%2 == 0):
        shift1 = radius # every other row needs to be moved up
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis1 + number*diameter + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis1 + shift2 - (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotssssss.append((x_axis1 + shift1, y_axis1 + number*diameter + shift2-(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1 # if it can fit in the box, add the coin
      y_axis1 += diameter
    for y in range(2000*radius,range_y2*1000*radius,1000*radius): # adding all the coins vertically in hexagon pattern
      if ((y/1000)%2 == 0):
        shift1 = radius
      else:
        shift1 = 0
      if ((x_axis1 + shift1) <= (Width - radius) and (x_axis1 + shift1) >= radius and (y_axis2 + number*diameter - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) <= (Length - radius)and (y_axis2 - shift2 + (diameter - (math.sqrt(3) * radius))*(y/(1000*radius))) >= radius):
        plotssssss.append((x_axis1 + shift1, y_axis2 + number*diameter - shift2+(0.2 - (math.sqrt(3) * 0.1))*(y/100)))
        coin_amount += 1
      y_axis2 -= diameter
    y_axis1 = y_axis
    y_axis2 = y_axis
    x_axis1 += diameter
    x += 10*radius

  coins.append(coin_amount) # add each coin amount to a list


  amounts = []
  for c in coins:
    amounts.append(c)
  coins.sort()
  coin_amount = coins[-1] # maximum amount of coins
  coin_area = coin_amount * math.pi * (radius**2)
  if (coin_amount == amounts[0]): # plots hexagonal packing structure
    for c in coinss:
      dimension.add_artist(plt.Circle(c, radius))
  elif (coin_amount == amounts[2]):
    for p in plotss: # plots modified hexagonal packing structure with 3 rectangular rows when it is more efficient
      dimension.add_artist(plt.Circle(p, radius))
  elif (coin_amount == amounts[3]):
    for p in plotsss: # plots modified hexagonal packing structure with 4 rectangular rows when it is more efficient
      dimension.add_artist(plt.Circle(p, radius))
  elif (coin_amount == amounts[4]):
    for p in plotssss: # plots modified hexagonal packing structure with 5 rectangular rows when it is more efficient
      dimension.add_artist(plt.Circle(p, radius))
  elif (coin_amount == amounts[5]):
    for p in plotsssss: # plots modified hexagonal packing structure with 6 rectangular rows when it is more efficient
      dimension.add_artist(plt.Circle(p, radius))
  elif (coin_amount == amounts[6]):
    for p in plotssssss: # plots modified hexagonal packing structure with 7 rectangular rows when it is more efficient
      dimension.add_artist(plt.Circle(p, radius))
  else:
    for p in plots: # plots modified hexagonal packing structure with 2 rectangular rows when it is more efficient
      dimension.add_artist(plt.Circle(p, radius))
box_area = Width * Length
extra_space = box_area - coin_area

efficiency = (1 - (extra_space/box_area))*100 # maximum efficiency

print("\nYou have stored a value of: \t", coin_amount, "coins.")
print("Your extra space is:  \t\t", extra_space, "square units.")
print("Your efficiency is:  \t\t", efficiency, "%\n")
