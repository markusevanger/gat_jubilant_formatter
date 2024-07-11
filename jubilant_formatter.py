import csv, re, os
from datetime import datetime, timedelta
from collections import defaultdict


# CSV key values:
FIRSTNAME = "Fornavn"
LASTNAME = "Etternavn"
DATE = "Dato"
AGE = "År"
PLACE = "Poststed"
ZIPCODE = "Postnr."
BORN = "Født"

def getMonthName(month:int):

    months = {
        1 : "januar",
        2 : "februar",
        3 : "mars",
        4 : "april",
        5 : "mai",
        6 : "juni",
        7 : "juli",
        8 : "august",
        9 : "september",
        10 : "oktober",
        11 : "november",
        12 : "desember"
    }
    return months[month]
def getDayName(day:int):
    days = {
        0 : "mandag",
        1 : "tirsdag",
        2 : "onsdag",
        3 : "torsdag", 
        4 : "fredag",
        5 : "lørdag",
        6 : "søndag"
    }
    return days[day]

class Person: 
    def __init__(self, firstname, lastname, date, age, place, zipcode, born):
        self.firstname = firstname
        self.lastname = lastname
        self.date = convertToDatetime(date)
        self.dateRaw = date
        self.age = extractNumbers(age)
        self.place = place
        self.zipcode = zipcode
        self.born = born
class format:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def convertToDatetime(inpTime):
    format = "%Y-%m-%d"
    return datetime.strptime(inpTime, format)
def extractNumbers(stringWithNumbers):
    numbers = re.findall(r'\d+', stringWithNumbers)
    return int(''.join(numbers)) if numbers else None

# Creates list of Persons from csv file. 
def createListOfPersons(inputFile:str):

    print("📖 Leser fil...")
    persons = []

    filteredFileName = f"{inputFile.strip('.csv')}_filtered.csv"
    if os.path.isfile(f"./{filteredFileName}"):
        inputFile = filteredFileName
        print("(Bruker filtrert data)")

    with open(inputFile, "r", encoding="utf-8") as file:
        csvFile = csv.DictReader(file)

        for personData in csvFile:
            newPerson = Person(
                firstname=personData[FIRSTNAME],
                lastname=personData[LASTNAME],
                date=personData[DATE],
                age=personData[AGE],
                place=personData[PLACE],
                zipcode=personData[ZIPCODE],
                born=personData[BORN]
            )
            persons.append(newPerson)
    print("📖 Ferdig å lese fil")
    return persons

# Takes list of Persons and makes a map where key is a datetime. 
def mapPersonsToDate(persons:list):

    persons.sort(key=lambda x: x.date, reverse=False) # sort list of persons by date in acending order

    dates = defaultdict(list)
    for person in persons:
        date = person.date
        if date.weekday in [1, 3, 5]:
            dates[date].append(person)
        else: 
            closestDate = date
            while closestDate.weekday() not in [1, 3, 5]:
                closestDate = closestDate - timedelta(days = 1)
            dates[closestDate].append(person)




    return dates

# Writes data to file formatted for GAT jubilanter. 
def write(mappedPersons):

    allDates = mappedPersons.keys()
    maxDate = max(allDates)
    minDate = min(allDates)

    outputName = f"GAT_Jubilanter_{minDate.day}.{minDate.month}-{maxDate.day}.{maxDate.month}.txt"
    DISCLAIMER = f"""
Denne filen filen er automatisk generert ved bruk av dette verktøyet: https://github.com/markusevanger/gat_jubilant_formatter
Under ligger jubilanter til GAT for perioden {minDate.day}.{minDate.month}-{maxDate.day}.{maxDate.month}. Vær obs på de første og siste datoene, da data settet som er
oppgitt ikke matcher opp med utgivelsene til avisene. Et datasett som starter f.eks 3. juli, har ikke jublianter for 2. juli. I disse
tilfeller burde ting bli gjort manuelt.  

    """

    with open(outputName, "w", encoding="utf-8") as file:

        file.write(DISCLAIMER)

        for date in allDates:
            
            file.write(f"\n\n\n======================= GAT {getDayName(date.weekday())} {date.day}. {getMonthName(date.month)} {date.year}: ======================= \n ")
            mappedPersons[date].sort(key=lambda x:x.age, reverse=True)


            lastAge = None
            for person in mappedPersons[date]:

                if lastAge != person.age:
                    file.write(f"\n{person.age} år \n")
                    lastAge = person.age

                file.write(f"{person.firstname} {person.lastname}, {person.place}, fyller {person.age} år {person.date.day}. {getMonthName(date.month)}. \n")

    print(f"📝 Skrevet til {outputName}")




# Takes list of persons and prompts user for last names, finding and removing them.  
def filterOut(persons):
    
    filteredPersons = persons
    lastname = input(f"Ønsker du å filtrere ut navn? {format.UNDERLINE}Y{format.END} for ja / {format.UNDERLINE}N{format.END} eller {format.UNDERLINE}blank{format.END} for å avslutte: ")

    while lastname.lower() not in ["nei", "", "n"]:
        lastname = input(f"|    🔍 Skriv inn ett etternavn ({format.UNDERLINE}blank{format.END} for å avslutte): ")
        
        if lastname != "":
            
            personFound = None

            for person in persons:
                if person.lastname.lower() == lastname.lower():
                    print("|")
                    print(f"|   Fant: {format.BOLD}{person.firstname} {person.lastname}{format.END}, {person.place}: {person.age} år")
                    isCorrect = input(f"|   Ønsker du å {person.firstname} fjerne fra listen? {format.UNDERLINE}Y{format.END} ({format.UNDERLINE}blank{format.END} er også ja) / {format.UNDERLINE}N{format.END} for å finne flere: ").lower() != "n"
                    if isCorrect:
                        personFound = person
                        break
                    
            
            if not personFound:
                print(f"|    |    ❌ Fant ingen med etternavn: {lastname}")
                print("|    |    🔄 Prøv på nytt eller skriv ett nytt etternavn")
                print("|    |")
            else:
                filteredPersons.remove(personFound)
                print(f"|   |   ✔  Fjernet {personFound.firstname} {personFound.lastname} fra listen.")
                print("|")



    return filteredPersons




# Writes a new CSV file with filtered persons to be read, so program can be run multiple times and remember the persons removed.
def createUpdatedStorage(persons, fileName):

    updatedStorageFileName = f"{fileName.strip('.csv')}_filtered.csv"
    
    fields = [DATE, AGE, FIRSTNAME, LASTNAME, PLACE, ZIPCODE, BORN]
    
    rows = []
    for person in persons:
        rows.append([person.dateRaw, person.age, person.firstname, person.lastname, person.place, person.zipcode, person.born])
    with open(updatedStorageFileName, 'w', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    print("🗂️ Lagret filtret data i egen fil")

def findCsvData():
    
    for file in os.listdir():
        if ".csv" in file and "_formatted" not in file:
            print(f"🔖 Fant fil: {file}")
            return file
    return None
 


def main():

    fileName = findCsvData()
    if not fileName:
        print("❌  Kunne ikke finne en .csv fil i mappen. Har du lagt den til i samme mappe som alle de andre filene?") 
        return

    persons = createListOfPersons(fileName)

    print(f"✂️  Ønsker du å fjerne personer fra listen?")
    filteredPersons = filterOut(persons)
    print()
    
    createUpdatedStorage(filteredPersons, fileName)
    mappedPersons = mapPersonsToDate(filteredPersons) # map with date as key and list of persons as value. 
    write(mappedPersons)
    print("✅ Ferdig!")
    
main()