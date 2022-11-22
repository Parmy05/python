#1
diz={"Giuseppe Gullo":[("corsa campestre",(40,21,0),"Allieve"),("corsa 100mt",(0,12,0),"Juniores mas"),("corsa 200mt"),(0,29,19),"Juniores mas"],
    "Antonia Barbera":[("corsa campestre",(0,39,11),"Juniores fem"),("corsa 100mt",(0,18,0),"Juniores fem"),("corsa 200mt"),(0,0,0),"Juniores fem"],
    "Nicola Esposito":[("corsa campestre",(0,43,22),"Allieve"),("corsa 100mt",(0,14,0),"Juniores mas"),("corsa 200mt"),(0,36,19),"Juniores mas"]}
#2
diz["Tommaso Parmigiani"]=[("corsa campestre",(60,0,12),"Allieve"),("corsa 100mt",(0,0,0),"Juniores mas"),("corsa 200mt"),(19,0,59),"Allieve"]
#3 9.15 Gornati
diz["Giuseppe Gullo"]=[("corsa campestre",(40,21,0),"Allieve"),("corsa 100mt",(0,12,0),"Juniores mas"),("corsa 200mt",(0,29,19),"Juniores mas"),("corsa ad ostacoli 400 mt",(0,40,34),"Allievo")]
diz["Antonio Barbera"]=[("corsa campestre",(0,39,11),"Juniores fem"),("corsa 100mt",(0,18,0),"Juniores fem"),("corsa 200mt",(0,0,0),"Juniores fem"),("corsa ad ostacoli 400 mt",(0,39,10),"Allieva")]
diz["Nicola Esposito"]=[("corsa campestre",(0,43,22),"Allieve"),("corsa 100mt",(0,14,0),"Juniores mas"),("corsa 200mt",(0,36,19),"Juniores mas"),("corsa ad ostacoli 400 mt",(0,40,10),"Allievo")]
diz["Tommaso Parmigiani"]=[("corsa campestre",(60,0,12),"Allieve"),("corsa 100mt",(0,0,0),"Juniores mas"),("corsa 200mt",(19,0,59),"Allieve"),("corsa ad ostacoli 400 mt",(0,40,26),"Allievo")]
#4 9.51 Gornati
print(diz["Giuseppe Gullo"][0])
#5 10.07 Gornati
for i in range(3):
  print(diz["Nicola Esposito"][2][1][i])
#6 9.51 Gornati
print(diz["Antonio Barbera"][1][1])
