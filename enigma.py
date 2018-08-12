alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#alphabets for each rotor
alpha1 = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
alpha2 = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
alpha3 = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
alpha4 = list("ESOVPZJAYQUIRHXLNFTGKDCMWB")
alpha5 = list("VZBRGITYUPSDNHLXAWMJQOFECK")
reflector = list("YRUHQSLDPXNGOKMIEBFZCWVJAT")
#notches for each rotor
notch1 = "Q"
notch2 = "E"
notch3 = "V"
notch4 = "J"
notch5 = "Z"
#user-inputted rotors
rotor1 = int(input("Enter rotor #1 (must be integer from 1-5): "))
rotor2 = int(input("Enter rotor #2 (must be integer from 1-5): "))
rotor3 = int(input("Enter rotor #3 (must be integer from 1-5): "))
rotors = [rotor1, rotor2, rotor3]
#user-inputted position of each rotor

position1 = input("Enter position #1 (must be a capital letter in the alphabet): ")
position2 = input("Enter position #2 (must be a capital letter in the alphabet): ")
position3 = input("Enter position #3 (must be a capital letter in the alphabet): ")
position = [position1, position2, position3]



#user-inputted string
secretMessage = input("Enter your secret message (must be all capital letters): ")
#dictionary where each rotor # is the key, and includes the alphabet and notch for that rotor
rotorRef = {1: [alpha1,notch1], 2: [alpha2, notch2], 3: [alpha3, notch3], 4: [alpha4, notch4], 5: [alpha5, notch5]}


#initialization of positions of rotors
idx1 = alphabet.index(position[0])
idx2 = alphabet.index(position[1])

idx3 = alphabet.index(position[2])
string1 = rotorRef[rotors[0]][0][idx1:] + rotorRef[rotors[0]][0][:idx1]
string2 = rotorRef[rotors[1]][0][idx2:] + rotorRef[rotors[1]][0][:idx2]
string3 = rotorRef[rotors[2]][0][idx3:]+ rotorRef[rotors[2]][0][:idx3]
rotorRef[rotors[0]][0] = string1
rotorRef[rotors[1]][0] = string2
rotorRef[rotors[2]][0] = string3

#input:none
#output:none
#moves first letter of the first rotor's alphabet to the end, and continues on to other rotors when notch is reached
def rotation():
  r1 = rotorRef[rotors[0]][0].pop(0)
  rotorRef[rotors[0]][0].append(r1)
  tmp = alphabet.index(position[0])
  if position[0]!="Z":
    position[0] = alphabet[tmp+1]
  else:
    position[0] = "A"
  if alphabet[tmp] == rotorRef[rotors[0]][1]:
    r2 = rotorRef[rotors[1]][0].pop(0)
    rotorRef[rotors[1]][0].append(r2)
    tmp = alphabet.index(position[1])
    if position[1]!="Z":
      position[1] = alphabet[tmp+1]
    else:
      position[1] = "A"
    if alphabet[tmp] == rotorRef[rotors[1]][1]:
      r3 = rotorRef[rotors[2]][0].pop(0)
      rotorRef[rotors[2]][0].append(r3)
  #print(rotorRef[rotors[0]][0])

def substitution(letter):
  letter = rotorRef[rotors[0]][0][alphabet.index(letter)]
  letter = rotorRef[rotors[1]][0][alphabet.index(letter)]
  letter = rotorRef[rotors[2]][0][alphabet.index(letter)]
  letter = reflector[alphabet.index(letter)]
  letter = alphabet[rotorRef[rotors[2]][0].index(letter)]
  letter = alphabet[rotorRef[rotors[1]][0].index(letter)]
  letter = alphabet[rotorRef[rotors[0]][0].index(letter)]
  return letter 

encryptedMessage = ""

for letter in secretMessage:
  rotation()
  encryptedMessage += substitution(letter)
  
  
  
print(encryptedMessage)
  
  
  


