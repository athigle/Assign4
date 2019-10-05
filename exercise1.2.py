#!/usr/bin/python

aircraft_1=dict()
aircraft_2=dict()
aircraft_3=dict()
aircraft_4=dict()
aircraft_5=dict()
aircrafts=list()

aircraft_1['x']=21
aircraft_1['y']=41

aircraft_2['x']=31
aircraft_2['y']=51

aircraft_3['x']=61
aircraft_3['y']=81

aircraft_4['x']=71
aircraft_4['y']=91

aircraft_5['x']=100
aircraft_5['y']=110

aircrafts.append(aircraft_1)
aircrafts.append(aircraft_2)
aircrafts.append(aircraft_3)
aircrafts.append(aircraft_4)
aircrafts.append(aircraft_5)

print("aircrafts list: {}".format(aircrafts))
print("\n")
print("x of aircraft_1: {}".format(aircrafts[0]['x']))
print("y of aircraft_1: {}".format(aircrafts[0]['y']))
print("\n")
print("x of aircraft_2: {}".format(aircrafts[1]['x']))
print("y of aircraft_2: {}".format(aircrafts[1]['y']))
print("\n")
print("x of aircraft_3: {}".format(aircrafts[2]['x']))
print("y of aircraft_3: {}".format(aircrafts[2]['y']))
print("\n")
print("x of aircraft_4: {}".format(aircrafts[3]['x']))
print("y of aircraft_4: {}".format(aircrafts[3]['y']))
print("\n")
print("x of aircraft_5: {}".format(aircrafts[4]['x']))
print("y of aircraft_5: {}".format(aircrafts[4]['y']))

