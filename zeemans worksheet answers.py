import pickle
import zampy
import math
import csv
import statistics
#To find frequence of each word in a file, and displau the 5 most frequent words
def find_frequency():
    file = open('sample.txt')
    contents = file.read()
    words = contents.split()
    datadict = {}
    for word in words:
        if word.isalpha():
            try:
                datadict[word] += 1
            except KeyError:
                datadict[word] = 1
    datalist = list()
    for key, value in datadict.items():
        if len(datalist) > 0:
            if len(datalist) <= 5:
                if len(datalist) < 5:
                    datalist.append(key)
                for index in range(len(datalist)):
                    if value > datadict[datalist[index]]:
                        datalist.insert(index, key)
                        if len(datalist) > 5:
                            datalist.pop() 
                        break
        else:
            datalist.append(key)
    print('The top 5 most frequent words are:')
    print(datalist)
    print('The frequencies of other words are:', datadict)

#find_frequency()
#2. WAP to read a text file and replace a specific word in the file. Save the changes in a new file.
def replace_specific_word(word_to_replace, replace_word):
    main_file = open('sample.txt')
    new_file = open('new.txt', 'w+')
    new_file.write(main_file.read().replace(word_to_replace, replace_word))
    new_file.close()
    main_file.close()
#replace_specific_word('Idlib', 'Syria')

#3. WAP to red a text file and reverse the ordr of lines and write it to another file.
def reverse_line_order():
    main_file = open('sample.txt')
    new_file = open('new.txt', 'w+')
    new_file.writelines(main_file.readlines()[::-1])
    new_file.close()
#reverse_line_order()

#4. WAP to read a text file and find the longest word in the file.
def find_longest_word():
    file = open('sample.txt')
    data = file.read()
    words = data.split()
    lengths = []
    for word in words:
        lengths.append(len(word))
    maxlen = max(lengths)
    for word in words:
        if len(word) == maxlen:
            words.remove(word)
            print('Longest word:', word)

#5. read a text file and convert all uppercase to lowercase.
def uppertolower():
    file = open('sample.txt')
    content = file.read()
    updatedcontent = ""
    for char in content:
        if char.isalpha():
            if char.islower():
                updatedcontent += char.upper()
            elif char.isupper():
                updatedcontent += char.lower()
        else:
            updatedcontent += char
    print(updatedcontent)
    new_file = open('new.txt', 'w+')
    new_file.write(updatedcontent)
    new_file.close()
#uppertolower()
#6. lowStockProducts() to read 'INVENTORY.DAT' display details where stock quantity less than 50
#additionally, calculate and display the total count of such low stock products.
#Structure: (ProductID, ProductName, Quantity, Price)

#zampy.create_file_with_data('inventory', '.dat', "((1, 'Table', 45, 3500), (2, 'Chair', 65, 5000), (3, 'Zaman', 1, 1))")
data = ((1, 'Table', 45, 3500), (2, 'Chair', 65, 5000), (3, 'Zaman', 1, 1))
pickle.dump(data, open('inventory.dat', 'wb'))

def lowStockProducts():
    file = open('inventory.dat', 'rb')
    data = pickle.load(file)
    lowStocks = []
    #print(data)
    for entry in data:
        if entry[2] < 50:
            lowStocks.append(entry)
    print(f'Total count of low stock products: {len(lowStocks)}')
    print(f'The products are: \n')
    for entry in lowStocks:
        print(entry)

#lowStockProducts()

def updatePrice(productID, newPrice):
    with open('inventory.dat', 'rb') as file:
        tdata = pickle.load(file)
        #data = [[x[0], x[1], x[2], x[3]] for x in tdata]
    newdata = tuple()
    for entry in tdata:
        if entry[0] == productID:
            newdata += ((entry[0], entry[1], entry[2], newPrice),)
        else:
            newdata += ((entry[0], entry[1], entry[2], entry[3]),)
    with open('inventory.dat', 'wb') as updatedfile:
        #tdata = (((x[0], x[1], x[2], x[3]),) for x in data)
        #print(tdata)
        pickle.dump(newdata, updatedfile)

#updatePrice(2, 10000)
#8. Add product that accepts a record with the structure as a parameter. Function should append the new product to
# inventory.dat

def addProduct():
    mfile = open('inventory.dat', 'rb')
    existingData = pickle.load(mfile)
    mfile.close()
    newRecord = (int(input('Enter Product ID: ')), input('Enter product name: '), int(input('Enter quantity: ')), int(input('Enter price: ')))
    newData = existingData + (newRecord,)
    #print(newData)
    rfile = open('inventory.dat', 'wb')
    pickle.dump(newData, rfile)
    rfile.close()
#addProduct()
#print(pickle.load(open('inventory.dat', 'rb')))

#9. deleteProduct()

def deleteProduct(productID):
    mfile = open('inventory.dat', 'rb')
    existingData = pickle.load(mfile)
    newData = ()
    for record in existingData:
        if record[0] == productID:
            continue
        newData += (record,)
    rfile = open('inventory.dat', 'wb')
    pickle.dump(newData, rfile)
#deleteProduct(2)
#print(pickle.load(open('inventory.dat', 'rb')))

#10. already done in nb, check later code

#11. cheapestFlight()
def cheapestFlight():
    with open('flight.dat', 'rb') as file:
        data = pickle.load(file)
        lowestFlight = None
        for flight in data:
            if lowestFlight:
                if flight[2] < lowestFlight[2]:
                    lowestFlight = flight
            else:
                lowestFlight = flight
        print(lowestFlight, "has the lowest fare.")
#pickle.dump([[zampy.random_number(2, False), zampy.random_name(), zampy.random_number(), zampy.random_city(), zampy.random_city()] for x in range(10)], open('flight.dat', 'wb'))
#print(pickle.load(open('flight.dat', 'rb')))
#cheapestFlight()

#12. findBookType: dont in nb, check later code.

#13. cheapestBook
def cheapestBook():
    with open('book.dat', 'rb') as file:
        data = pickle.load(file)
        lowestBook = None
        for key, value in data.items():
            if lowestBook:
                if value[2] < lowestBook[1][2]:
                    lowestBook = [key, value]
            else:
                lowestBook = [key, value]
    print('lowestPrice is:', lowestBook)

#14. flightStats()
def flightStats():
    with open('flight.dat', 'rb') as file:
        data = pickle.load(file)
        lowestFlight = None
        highestFlight = None
        listOfFares = []
        for record in data:
            listOfFares.append(record[2])
            if lowestFlight:
                if record[2] < lowestFlight[2]:
                    lowestFlight = record
            else:
                lowestFlight = record
            if highestFlight:
                if record[2] > highestFlight[2]:
                    highestFlight = record
            else:
                highestFlight = record
        print('lowestFlight:', lowestFlight, '\nHighestFlight:', highestFlight, '\nAverage fare:', statistics.mean(listOfFares))
#flightStats()

#bookStats:
def bookStats():
    with open('book.dat', 'rb') as file:
        data = pickle.load(file)
        lowestBook, highestBook, listOFFares = None, None, []
        for key, value in data.items():
            listOFFares.append(value[2])
            if lowestBook:
                if value[2] < lowestBook[1][2]:
                    lowestBook = [key, value]
            else:
                lowestBook = [key, value]
            
            if highestBook:
                if value[2] > highestBook[1][2]:
                    highestBook = [key, value]
            else:
                highestBook = [key, value]
        print('lowestBook:', lowestBook, '\nhighestBook:', highestBook, '\nAverage price:', statistics.mean(listOFFares))

#16. flightSearch()
#print(pickle.load(open('flight.dat', 'rb')))
def flightSearch(maxFare):
    with open('flight.dat', 'rb') as file:
        data = pickle.load(file)
        listOfReqFlights = []
        for record in data:
            if record[2] <= maxFare:
                if len(listOfReqFlights) > 0:
                    for index in range(len(listOfReqFlights)):
                        if record[2] <= listOfReqFlights[index][2]:
                            listOfReqFlights.insert(index, record)
                            break
                        else:
                            listOfReqFlights.append(record)
                            break
                else:
                    listOfReqFlights.append(record)
        print('Requested list in ascending order is:')
        #print(listOfReqFlights)
        for index in range(len(listOfReqFlights)):
            print(f'{index + 1}. {listOfReqFlights[index]}')
#flightSearch(8000)

#17. bookSearch():

def bookSearch(minPrice, bookType):
    with open('book.dat', 'rb') as file:
        data = pickle.load(file)
        lBooks = []
        for key, value in data.items():
            if value[1] == bookType and value[2] >= minPrice: #value[1] == bookType and 
                tempRecord = [key, value]
                if len(lBooks) == 0:
                    lBooks.append(tempRecord)
                else:
                    for index in range(len(lBooks)):
                        if lBooks[index][1][2] <= value[2]:
                            lBooks.insert(index, tempRecord)
                            break
                    else:
                        lBooks.append(tempRecord)
        for index in range(len(lBooks)):
            print(f'{index + 1}. {lBooks[index]}')

#18.a. allow for user to add book records into book.dat, and count number of recrds by specific author in book.dat
#18.b. count students who got less than 40% in class.dat 

#data = dict([(zampy.random_number(2, False), [f"{zampy.random_name(1)}'s Book", f"{zampy.random_genre()}", zampy.random_number()]) for x in range(50)])
#print(data)
#pickle.dump(data, open('book.dat', 'wb'))
#print(pickle.load(open('book.dat', 'rb')))
#bookSearch(3000, 'Mystery')
#half yearly practice
def mymean(listofvalues: list) -> int:
    try:
        return sum(listofvalues)/len(listofvalues)
    except:
        print('An error had occured.')
        return None

def factorial(number: int) -> int:
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

def name_maker(firstname, lastname):
    return " ".join([firstname, lastname])

def areaperimiter(radius: float) -> float:
    return math.pi * (radius ** 2), 2 * math.pi * radius

def swaptwonumbers(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    return num1, num2

def countlinesinafile():
    try:
        with open('sample.txt') as file:
            return len(file.readlines())
    except:
        print('Some error occured.')

def readEeandTt():
    data = {}
    with open('sample.txt') as file:
        for char in file.read():
            if char.isalpha() and (char in 'Ee' or char in 'Tt'):
                char = char.lower()
                if char in data.keys():
                    data[char] += 1
                else:
                    data[char] = 0
        print(data)

def countlinesendingwithfullstoporcomma():
    count = 0
    with open('sample.txt') as file:
        for line in file.readlines():
            if line.endswith('.\n') or line.endswith(',\n'):
                count += 1
    print(count)

def readandseperatewithhashes():
    with open('sample.txt') as file:
        lines = file.readlines()
        for line in lines:
            print('#'.join(line.split()))

def vowelcount():
    count = 0
    with open('sample.txt') as file:
        for char in file.read():
            if char.isalpha():
                if char.lower() in 'aeiou':
                    count += 1
        print('Number of vowels is', count)

def linesstartingwithyou():
    with open('sample.txt') as file:
        for line in file.readlines():
            if line.startswith('You'):
                print(line)

def removeeverythingwitha():
    file_1 = open('sample.txt')
    main_data = file_1.readlines()
    file_1.close()
    file_1_new = open('sample.txt', 'w+')
    file_2 = open('everythingthathasa.txt', 'w+')
    #data_contains_a = []
    for line in main_data:
        if 'a' in line:
            file_2.write(line)
        else:
            file_1_new.write(line)
    file_1_new.close()
    file_2.close()

def deleteline(word: str):
    data = None
    with open('sample.txt') as file:
        data = file.readlines()
    file_1_aftermod = open('sample.txt', 'w+')
    file_2 = open('hasdeletedword.txt', 'w+')
    for line in data:
        if word in line.split():
            file_2.write(line)
        else:
            file_1_aftermod.write(line)
    file_1_aftermod.close()
    file_2.close()

def readrecordsofstudentsabovefifty():
    file = open('sample.dat', 'rb')
    data = pickle.load(file)
    for record in data:
        if record[2] > 50 and record[2] < 60:
            print(record)
#data = [[101, 'Tom', 55], [102, 'Tim', 45], [103, 'Tum', 34], [104, 'Tam', 57]]
#data = [['Basketball', zampy.random_name() + "'s Team", zampy.random_number(2)] for x in range(5)]
#print(data)
#pickle.dump(data, open('sports.dat', 'wb'))

#print(pickle.load(open('sample.dat', 'rb')))
def writerec():
    while True:
        file = open('sample.dat', 'rb')
        recordid = int(input('Enter record ID: '))
        name = input('Enter name of plant: ')
        price = int(input('Enter price of plant: '))
        record = (recordid, name, price)
        existingdata = pickle.load(file)
        existingdata.append(record)
        file_update = open('sample.dat', 'wb')
        pickle.dump(existingdata, file_update)
        file_update.close()
        if input('Continue? (y/n): ').lower() in 'n':
            break
    file = open('sample.dat', 'rb')
    data = pickle.load(file)
    print('The following records have a price above 500: ')
    for record in data:
        if record[2] > 500:
            print(record)

def copyData():
    with open('sports.dat', 'rb') as sportfile:
        data = pickle.load(sportfile)
        basketfile = open('basket.dat', 'wb')
        basketdata = []
        for record in data:
            if record[0].lower() == 'basketball':
                basketdata.append(record)
        pickle.dump(basketdata, basketfile)
        basketfile.close()

def findType(mtype: str):
    with open('cinema.dat', 'rb') as main_file:
        data = pickle.load(main_file)
        filtered_list = []
        for key, value in data.items():
            filtered_list.append([key, value[1]])
        print('The requested data: ')
        for record in filtered_list:
            if record[1] == mtype:
                print(data[record[0]])

def expensiveProducts():
    count = 0
    with open("inventory.dat") as file:
        data = pickle.load(file)
        for record in data:
            if record[3] > 1000:
                print(record[0], "has a cost above 1000!")
                count += 1
    print('The number of expensive records is', count)

def csvstudentmanager():
    file = open('students.csv', 'w+', newline='')
    fc = csv.writer(file)
    fc.writerow(['Roll No.', 'Student Name', 'Marks'])
    file.close()
    while True:
        choices = zampy.make_menu_from_options(['Add student', 'Count total records', 'Display records above 75'])
        choice = int(input(choices))
        if choice == 1:
            file = open('students.csv', 'r+', newline="")
            fc = csv.reader(file)
            next(fc)
            fc = csv.writer(file)
            
            studentrecord = [int(input('Enter roll no: ')), input('Enter student name: '), int(input('Enter marks: '))]
            fc.writerow(studentrecord)
            file.close()
        elif choice == 2:
            file = open('students.csv', 'r+', newline="")
            fc = csv.reader(file)
            next(fc)
            count = 0
            for row in fc:
                count += 1
            print(count)
            file.close()
        elif choice == 3:
            file = open('students.csv', 'r+', newline="")
            fc = csv.reader(file)
            next(fc)
            for record in fc:
                if int(record[2]) > 75:
                    print(record)
            file.close()

def csvopen():
    file = open('books.csv', 'r+')
    return file
def csvread():
    file = csvopen()
    fc = csv.reader(file)
    next(fc) #skip the header
    for record in fc:
        if record[0].startswith('R'):
            print(record)

#fc = csv.writer(csvopen())
#fc.writerows([['Title', 'Author', 'Price'], [zampy.random_name(), zampy.random_name(), zampy.random_number], [zampy.random_name(), zampy.random_name(), zampy.random_number]])

def addfurniture():
    record = [int(input('Enter furniture ID: ')), input('Enter furniture name: '), int(input('Enter furniture price: '))]
    with open('furdata.csv', 'w+', newline='') as file:
        fc = csv.writer(file)
        fc.writerow(['FID', 'Fname', 'Fprice'])
        fc.writerow(record)

def searchfurniture():
    with open('furdata.csv', newline='') as file:
        fc = csv.reader(file)
        next(fc)
        for record in fc:
            if int(record[2]) > 10000:
                print(record, 'has more than 10000 price.')

def writeitemsinonego():
    with open('products.csv', "w+", newline='') as file:
        records = []
        while True:
            records.append([input('Enter code: '), input('Enter description: '), input('Enter price: ')])
            if input('Continue? ') in 'Nn':
                break
        fc = csv.writer(file)
        fc.writerow(['Code', 'Description', 'Price'])
        fc.writerows(records)

def PUSH(stack, element):
    stack.append(element)

def POP(stack):
    try:
        return stack.pop()
    except:
        return None
def stackscores(): 
    data = {'KAPIL': 40, 'ABC': 50, 'DEF': 60}
    stack = []
    for key, value in data.items():
        if value > 50:
            PUSH(stack, key)

    for index in range(len(stack)):
        print(POP(stack))

def stackeevennumbers():
    data = [x*2 for x in range(1, 11)]
    stack = []
    for number in data:
        if number % 2 == 0:
            PUSH(stack, number)
    for index in range(len(stack)):
        print(POP(stack))

def stackmarks():
    data = {101: (50, 60, 70), 102: (60, 70, 80), 103: (70, 80, 90)}
    stack = []
    for key, value in data.items():
        if value[2] >= 80:
            PUSH(stack, key)

    while True:
        triedPopping = POP(stack)
        if triedPopping != None:
            print(triedPopping)
        else:
            print('Stack empty.')
            break

def copy_rec_flights():
    with open('flight.dat', 'rb') as mainfile:
        newfile = open("record.dat", 'wb')
        recordstodump = []
        data = pickle.load(mainfile)
        for record in data:
            if record[-2].lower() == 'delhi' and record[-1].lower() == 'mumbai':
                recordstodump.append(record)
        pickle.dump(recordstodump, newfile)
        newfile.close()

#pickle.dump([[1, zampy.random_name(), zampy.random_number(), 'Delhi', 'Mumbai'], [2, zampy.random_name(), zampy.random_number(), 'Mumbai', 'Delhi'], [3, zampy.random_name(), zampy.random_number(), 'Delhi', 'Mumbai']], open('flight.dat', 'wb'))

def findbook(price: int):
    with open('book.dat', 'rb') as file:
        data = pickle.load(file)
        for key, value in data.items():
            if value[2] >= price:
                print(f'Book with bookNO {key} and book details {value} has price more than/equal to {price}')

#Venu is a python programmer working in a school. For the Annual Sports Event, he has created 4 a CSV file named result.csv, to store the results of students in different sports event. The
#structure of result.csv is: [St_id,St_name,Game_Name,Result] Where
#St_id is student ID (Integer)
#St_name is Student Name (String)
#Game_Name is name of game in which student is participating (String)
#Result is result of the game whose value can either be 'Won', 'Lost' or 'Tie'
#For efficiently maintaining data of the event, Venu wants to write the following user defined functions:
#Accept : To accept record from the user and add it to the file result.csv. The column heading should also be added on top of the csv file.
#woncount0: To count the number of students who have won any event.
#As a python expert, help him complete the task.

def accept():
    st_id = int(input('Enter student ID: '))
    st_name = input('Enter student name: ')
    game_name = input('Enter game name: ')
    result = input('Enter result (won/lost/tie): ')
    record = [st_id, st_name, game_name, result]
    with open('results.csv', 'r+') as file:
        fc = csv.writer(file)
        fc.writerows([['St_id', 'St_name', 'Game_Name', 'Result'], record])

def woncount():
    with open('results.csv') as file:
        fc = csv.reader(file)
        next(fc)
        count = 0
        for record in fc:
            if record[-1].lower() == 'won':
                count += 1 
        print(count)

#A csv file "Happiness.csv" contains the data of a survey. Each record of the
#file contains the following data:
#● Name of a country
#● Population of the country
#● Sample Size (Number of persons who participated in the survey in
#that country)
#● Happy (Number of persons who accepted that they were Happy)
#For example, a sample record of the file may be:
#[‘Signiland’, 5673000, 5000, 3426]
#Write the following Python functions to perform the specified operations on
#this file:
#(I) Read all the data from the file in the form of a list and display all
#those records for which the population is more than 5000000.
#(II) Count the number of records in the file

def popabove5000000():
    with open('Happiness.csv') as file:
        fc = csv.reader(file)
        next(fc)
        for record in fc:
            if int(record[1]) > 5000000:
                print(record)
def countrecords():
    with open('Happiness.csv') as file:
        fc = csv.reader(file)
        next(fc)
        count = 0
        for record in fc:
            count += 1
        print(count)

'''with open('C:\\Users\\Kassim\\Documents\\GitHub\\12th-python\\sample files\\book.dat', 'rb') as file:
    newfile = open('booksfortesting.dat','ab')
    data = pickle.load(file)
    for item in data.items():
        pickle.dump(item, newfile)
    newfile.close()
def tryinginfiniteload():
    with open('booksfortesting.dat', 'rb') as file:
        iteration = 0
        while True:
            try:
                record = pickle.load(file)
                print(record)
                iteration += 1
                print(iteration)
            except EOFError:
                print('Encountered EOFError.')
                break
tryinginfiniteload()'''