
import googletrans as gt


langdict = gt.LANGUAGES                             # langdict is a dictionary that contains language codes (keys)
keylang = list(langdict.keys())                     # keylang is a list that contains all the language codes.                   
valuelang = list(langdict.values())                 # valuelang is a list that contains all the language names.
                                                    
print (keylang)
print(valuelang)
t = gt.Translator()
while True:
    inputlang= input("Enter the input language:")
    for i in range(len(keylang)):
        if inputlang.lower() == valuelang[i]:
            inputlang = keylang[i]
            break

        else:
            print("sorry language is not found")

            mytext = input("enter the text you need to translate:")
            outputlang =input("enter the outputlang:")
            for j in range(len(keylang)):
             if outputlang.lower() == valuelang[j]:
                  outputlang = keylang[j]
            break
    else:
        print("sorry the language is not found: ")
        translatedtext = t.translate(mytext,src=inputlang,dest=outputlang)
        print(translatedtext.text)
        
   


       






