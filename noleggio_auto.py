diz={"AA123BB":[("Giugno", 9 , 1293), ("Luglio", 7 , 3231),("Agosto", 7 , 4020), ("Settembre", 6 , 3928)],
    "AB345CD":[("Giugno", 8 , 1391), ("Luglio", 6 , 1234), ("Agosto", 9 , 4932), ("Settembre", 8 , 2872)],
    "CD456FF":[("Giugno", 7 , 2872), ("Lugio", 6 , 3273), ("Agosto", 4 , 3211), ("Settembre", 8 , 2827)]}
diz["ZZ999PT"]=[("Giugno", 10 ,18000), ("Luglio", 10 , 18000),("Agosto", 10 , 18000), ("Settembre", 10 , 18000)]
print(diz["AA123BB"][1])
print(diz["AA123BB"][1][1])
totale=0
for i in range(len(diz["AB345CD"])):
  totale+=diz["AB345CD"][i][2]
print(totale)
SommaTot=0
for i in range(len(diz["AB345CD"])):
  SommaTot+=diz["AA123BB"][i][2] + diz["AB345CD"][i][2] + diz["CD456FF"][i][2] + diz["ZZ999PT"][i][2]
print(SommaTot)
max=0
for i in range(len(diz["CD456FF"])):
  if(max<diz["CD456FF"][i][2]):
    max=diz["CD456FF"][i][2]
print(max)
