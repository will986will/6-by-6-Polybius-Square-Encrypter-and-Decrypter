#intro
correctChoices = [1,2]
print ("Welcome to my polybius square")
print ("Would you like to:")
print ("1.Encrypt")
print ("2.Decrypt")
choice = int(input("Choose 1/2: "))
while choice not in correctChoices:
  if choice == 69 or choice == 420:
    choice = int(input("Nice but no just no! Choose 1/2: "))
  else:
    choice = int(input("Error Incorrect Input! Choose 1/2: "))
letters = []
numbers = []
possibleNums = ["1","2","3","4","5","6"]
finalProductArray = []
finalProduct =""
enteredLetter = 0
correctNums = 0
numberDecrypting = ""
#setting the square for letters
x0graphdirection = ["a","b","c","d","e","f"]
x1graphdirection = ["g","h","i","j","k","l"]
x2graphdirection = ["m","n","o","p","q","r"]
x3graphdirection = ["s","t","u","v","w","x"]
x4graphdirection = ["y","z","0","1","2","3"]
x5graphdirection = ["4","5","6","7","8","9"]
#setting the square for numbers
x0graphdirectionNum = ["11","12","13","14","15","16"]
x1graphdirectionNum = ["21","22","23","24","25","26"]
x2graphdirectionNum = ["31","32","33","34","35","36"]
x3graphdirectionNum = ["41","42","43","44","45","46"]
x4graphdirectionNum = ["51","52","53","54","55","56"]
x5graphdirectionNum = ["61","62","63","64","65","66"]

#checking the choice
if choice == 1:
  textToEncrypt = input("What would you like to encrypt")
  textToEncrypt = textToEncrypt.lower()
  wordLen = len(textToEncrypt)
  for letterNum in range (wordLen):
    enteredLetter = 0
    letters.append(textToEncrypt[letterNum])
    for xDirection in range(6):
      for yDirection in range(6):
        if xDirection == 0:
          if letters[letterNum] == x0graphdirection[yDirection]:
            finalProductArray.append(1)
            finalProductArray.append(yDirection+1)
            xDirection = 5
            yDirection = 5
            enteredLetter = 1
        elif xDirection == 1:
          if letters[letterNum] == x1graphdirection[yDirection]:
            finalProductArray.append(2)
            finalProductArray.append(yDirection+1)
            xDirection = 5
            yDirection = 5
            enteredLetter = 1
        elif xDirection == 2:
          if letters[letterNum] == x2graphdirection[yDirection]:
            finalProductArray.append(3)
            finalProductArray.append(yDirection+1)
            xDirection = 5
            yDirection = 5
            enteredLetter = 1
        elif xDirection == 3:
          if letters[letterNum] == x3graphdirection[yDirection]:
            finalProductArray.append(4)
            finalProductArray.append(yDirection+1)
            xDirection = 5
            yDirection = 5
            enteredLetter = 1
        elif xDirection == 4:
          if letters[letterNum] == x4graphdirection[yDirection]:
            finalProductArray.append(5)
            finalProductArray.append(yDirection+1)
            xDirection = 5
            yDirection = 5
            enteredLetter = 1
        elif xDirection == 5:
          if letters[letterNum] == x5graphdirection[yDirection]:
            finalProductArray.append(6)
            finalProductArray.append(yDirection+1)
            yDirection = 5
            enteredLetter = 1
    if enteredLetter == 0:
      finalProductArray.append(letters[letterNum])
  finalProductLen = len(finalProductArray)
  for willsAreAwesome in range (finalProductLen):
    finalProduct+=str(finalProductArray[willsAreAwesome])
  print("")
  print(finalProduct)
if choice == 2:
  textToDecrypt = input("What would you like to Decrypt")
  decryptionLength = len(textToDecrypt)
  for charToDecrypt in range (decryptionLength):
    numbers.append(textToDecrypt[charToDecrypt])
    #test
    if numbers[charToDecrypt] in possibleNums:
      correctNums = correctNums + 1
    else:
      finalProductArray.append(numbers[charToDecrypt])
    if correctNums == 2:
      #test
      numberDecrypting = numbers[charToDecrypt-1]+numbers[charToDecrypt]
      if numberDecrypting[0] == "1":
        for yDirection in range(6):
          if numberDecrypting == x0graphdirectionNum[yDirection]:
            finalProductArray.append(x0graphdirection[yDirection])
      if numberDecrypting[0] == "2":
        for yDirection in range(6):
          if numberDecrypting == x1graphdirectionNum[yDirection]:
            finalProductArray.append(x1graphdirection[yDirection])
      if numberDecrypting[0] == "3":
        for yDirection in range(6):
          if numberDecrypting == x2graphdirectionNum[yDirection]:
            finalProductArray.append(x2graphdirection[yDirection])
      if numberDecrypting[0] == "4":
        for yDirection in range(6):
          if numberDecrypting == x3graphdirectionNum[yDirection]:
            finalProductArray.append(x3graphdirection[yDirection])
      if numberDecrypting[0] == "5":
        for yDirection in range(6):
          if numberDecrypting == x4graphdirectionNum[yDirection]:
            finalProductArray.append(x4graphdirection[yDirection])
      if numberDecrypting[0] == "6":
        for yDirection in range(6):
          if numberDecrypting == x5graphdirectionNum[yDirection]:
            finalProductArray.append(x5graphdirection[yDirection])
      correctNums = 0
  finalProductLen = len(finalProductArray)
  for willsAreAwesome in range (finalProductLen):
    finalProduct+=str(finalProductArray[willsAreAwesome])
  print("")
  print(finalProduct)