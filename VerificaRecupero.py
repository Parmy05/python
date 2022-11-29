diz={}
import pprint
pp=pprint.PrettyPrinter(indent=4)

def leggiCodiceValido():
  codice=input("Scrivi il codice da inserire: ")
  while len(codice)==0:
    codice=input("Scrivi il codice da inserire: ")
  return codice
 
def leggiPosizioneValido():
  pos=input("Scrivi la posizione da aggiungere: ")
  while len(pos)==0:
    pos=input("Scrivi la posizione da aggiungere: ")
  return pos
  
def leggiPrezzoValido():
  prezzo=input("Scrivi il prezzo da aggiungere: ")
  while len(prezzo)==0:
    prezzo=input("Scrivi il prezzo da aggiungere: ")
  return prezzo

def leggiDataValido():
  data=input("Scrivi la data corretta: ")
  while len(data)==0:
    data=input("Scrivi la data corretta: ")
  return data

def leggiGiorniValido():
  giorni=input("Scrivi i giorni: ")
  while len(giorni)==0:
    giorni=input("Scrivi i giorni: ")
  return giorni

def leggiOpzioneValido():
  opzione=(input("Inserire l'opzione: "))
  while opzione==0:
    opzione=(input("Inserire l'opzione: "))
  return opzione

def leggiPrenotazioneValido():
  prenotazioni=int(input("Inserire il numero di prenotazioni: "))
  while prenotazioni<=0:
    prenotazioni=int(input("Inserire il numero di prenotazioni: "))
  return prenotazioni

def leggiDatiValido():
  return [leggiPosizioneValido(),leggiPrezzoValido(),leggiDataValido(),leggiGiorniValido(),leggiOpzioneValido()]

def popola():
  NumPren=leggiPrenotazioneValido()
  for i in range(NumPren):
    aggiungi()

def aggiungi():
  chiave=leggiCodiceValido()
  while(chiave in diz):
    chiave=leggiCodiceValido()
  dati=leggiDatiValido()
  diz[chiave]=dati

def cerca():
  chiave=leggiCodiceValido()
  if(chiave in diz):
    print(diz[chiave])
  else:
    print("Contatto non esistente")

def tutti():
    print(diz)

Scelta = 1
while (Scelta!=0):
  print('0) Esci')
  print('1) Popola')#Spinarelli 9:58
  print('2) Mostra le prenotazioni di un ombrellone')#Gornati 10.56
  print('3) Mostra tutte le prenotazioni')#Gornati 10:23
  print('4) Riduzione prezzo percentuale')
  print('5) Calcolo incasso totale di un mese')
  print('6) Visualizza le prenotazioni di n mesi')
  print('7) Mese incasso minimo')
  Scelta=int(input("Inserire la scelta desiderata: "))
  if Scelta==1:
    popola()
  elif Scelta==2:
    cerca()
  elif Scelta==3:
    tutti()
  elif Scelta==4:
    percentuale()
  elif Scelta==5:
    incasso()
  elif Scelta==6:
    visualizza()
  elif Scelta==7:
    minimo()
