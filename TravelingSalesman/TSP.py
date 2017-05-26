from math import *
import random
import copy
from tkinter import *

#Прорисовка полотна

root = Tk()
canv = Canvas(root, width=1000, height=1000, bg="white")
canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
canv.create_line(0, 500, 1000, 500, width=2, arrow=LAST)

top_frame = Frame(root)
top_frame.pack()

run = Button(top_frame, text = "Run")
run.pack(side=TOP, fill = X)
newTest = Button(top_frame, text = "New list")
newTest.pack(side=LEFT)


labelX = Label(top_frame)
labelY = Label(top_frame)
labelTextX = Label(top_frame, text = "x: ")
labelTextY = Label(top_frame, text = "y: ")

labelPopulation = Label(top_frame)
labelPopulationText = Label(top_frame, text = "Populations: ")
labelMutation = Label(top_frame)
labelMutationText = Label(top_frame, text = "Mutations: ")

labelMinLenghText = Label(top_frame, text = "Min. lengh:")
labelMinLengh = Label(top_frame)

labelPopulation.configure(text = str(0))
labelMutation.configure(text = str(0))
labelPopulationText.pack(side = LEFT)
labelPopulation.pack(side = LEFT)
labelMutationText.pack(side = LEFT)
labelMutation.pack(side = LEFT)

labelMinLenghText.pack(side = LEFT)
labelMinLengh.configure(text = str(0))
labelMinLengh.pack(side = LEFT)

labelEntText = Label(top_frame, text = "size of first population: ")
entFirstPopulationCount = Entry(top_frame, width=10, bd=3)
labelEntText.pack(side = LEFT)
entFirstPopulationCount.insert(10, "200")
entFirstPopulationCount.pack(side = LEFT)

labelChildText = Label(top_frame, text = "Count fo the best who go on: ")
entChildCount = Entry(top_frame, width=10, bd=3)
labelChildText.pack(side = LEFT)
entChildCount.insert(10, "20")
entChildCount.pack(side = LEFT)

labelTournamentText = Label(top_frame, text = "Size of Tournament: ")
entTournamentCount = Entry(top_frame, width=10, bd=3)
labelTournamentText.pack(side = LEFT)
entTournamentCount.insert(10, "15")
entTournamentCount.pack(side = LEFT)

labelEntText = Label(top_frame, text = "Max iterations: ")
entMaxIterationsCount = Entry(top_frame, width=10, bd=3)
labelEntText.pack(side = LEFT)
entMaxIterationsCount.insert(10, "400")
entMaxIterationsCount.pack(side = LEFT)



f = open('Cities.txt', 'w')
cities = []
countOfIterations = 0
mutationCount = 0
firstTest = True
fromFile = False
firstPopulationCount = 200
maxIterationsCount = 400


class Way:
    tableOfLength = []

    def __init__(self):
        self.genome = []
        sequenceOfCities = []

        self.genome.append(1)
        for i in range(2, len(Way.tableOfLength[0]) + 1):
            sequenceOfCities.append(i)

        random.shuffle(sequenceOfCities)  # Случайная последовательность чисел от 2 до кол-во городов

        for i in range(len(sequenceOfCities)):
            self.genome.append(sequenceOfCities[i])
        self.genome.append(1)

        self.fitness = 0
        self.culcFitness()

    def culcFitness(self):  # Вычисления функции приспособленности , как длина пути
        self.fitness = 0
        for i in range(len(self.genome) - 1):
            self.fitness += Way.tableOfLength[self.genome[i] - 1][self.genome[i + 1] - 1]
        return self.fitness

def getXY(event): # Добавляємо нову точку
    global f
    print("New dot was added")
    getx = event.x - 500
    gety = -event.y + 500

    print('x', getx)
    print('y', gety)
    if f.closed:
        f = open('Cities.txt', 'a')
    f.write(str(getx))
    f.write(" ")
    f.write(str(gety) + str("\n"))
    cities.append([getx, gety])

    if len(cities) == 1: # Первая точка красная
        canv.create_oval(getx + 500, -gety + 500, getx + 500 + 5, -gety + 500 + 5, fill='red')
        canv.create_text(getx + 500 + 10, -gety + 500 + 2.5, text=str(len(cities)), font=("Helvectica", "10"))
        return
    canv.create_oval(getx + 500, -gety + 500, getx + 500 + 5, -gety + 500 + 5, fill='black')
    canv.create_text(getx + 500 + 10, -gety + 500 + 2.5, text=str(len(cities)), font=("Helvectica", "10"))

def getXY_M(event):  # Вывод относительно курсора
    getx = event.x - 500
    gety = -event.y + 500

    labelX.configure(text=str(getx))
    labelY.configure(text=str(gety))
    labelTextX.pack(side=LEFT)
    labelX.pack(side=LEFT)
    labelTextY.pack(side=LEFT)
    labelY.pack(side=LEFT)

def runAlgorithm(event): # Гинетический алгоритм
    global firstPopulationCount
    global maxIterationsCount
    firstPopulationCount = int(entFirstPopulationCount.get())
    maxIterationsCount = int(entMaxIterationsCount.get())
    countOfBestChild = int(entChildCount.get())
    sizeOfTournament = int(entTournamentCount.get())
    global f
    if f.closed != True:
        f.close()
    global cities
    global countOfIterations
    global mutationCount
    global firstTest

    if cities == []:
        return
    if (firstTest != True) | (fromFile == True): # Если добавили точки но не стерли лист , то убераем стрелки и делаем прощет с новыми точками
        canv.delete(ALL)
        canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
        canv.create_line(0, 500, 1000, 500, width=2, arrow=LAST)
        for i in range(len(cities)):
            if i == 0:
                canv.create_oval(cities[i][0] + 500, -cities[i][1] + 500, cities[i][0] + 500 + 5,
                                 -cities[i][1] + 500 + 5, fill='red')
                canv.create_text(cities[i][0] + 500 + 10, -cities[i][1] + 500 + 2.5, text=str(i + 1), font=("Helvectica", "10"))
                continue
            canv.create_oval(cities[i][0] + 500, -cities[i][1] + 500, cities[i][0] + 500 + 5, -cities[i][1] + 500 + 5,
                             fill='black')
            canv.create_text(cities[i][0] + 500 + 10, -cities[i][1] + 500 + 2.5, text=str(i + 1), font=("Helvectica", "10"))

    firstTest = False
    countOfIterations = 0
    mutationCount = 0


    def Mutations(child): # Мутация(перестановка городов)
        global mutationCount
        if (len(child) < 4): # если меньше 4 городов то мутация не даст результата
            mutationCount += 1
            return
        firstPosition = random.randint(1, len(child) - 2)
        while (True):
            secondPosition = random.randint(1, len(child) - 2)
            if firstPosition != secondPosition:
                break
        child[firstPosition], child[secondPosition] = child[secondPosition], child[firstPosition] #проверка мутации
        mutationCount += 1

    def CreatingAPopulation(NumberOfWays):
        Ways = []
        for i in range(NumberOfWays):
            Ways.append(Way())
        return Ways

    tOfLength = []
    """
          1|2|3
          -----
       1  0|5|4
       2  5|0|2
       3  4|2|0
    """

    def cycleCrossover(Parent1, Parent2): #Обмен генами циклическим кросовером
        newGenome = []
        sequenceOfGens = [] # список генов переходящих 1 к одному начиная с 2 города
        Gen = Parent1.genome[1]
        index = 1
        sequenceOfGens.append(Gen)
        while (True): # -//-
            Gen = Parent2.genome[index]
            if Gen in sequenceOfGens:
                break
            sequenceOfGens.append(Gen)
            index = Parent1.genome.index(Gen)

        newGenome.append(1)
        for i in range(1, len(Parent1.genome) - 1):
            if Parent1.genome[i] in sequenceOfGens: # Если ген входит в цикличный список от 1 родителя
                newGenome.append(Parent1.genome[i])
            else: # если нет , то берем от 2 родителя
                newGenome.append(Parent2.genome[i])

        newGenome.append(1) # каждый набор должен завершаться 1 городом



        chance = random.randint(1, 100) # Рандом числа
        if chance <= 15:
            Mutations(newGenome)

        return newGenome

    def orderCrossover(Parent1, Parent2, firstDelimiter, secondDelimiter):
        newGenome = copy.deepcopy(Parent1.genome)
        listOfGensBetween = []
        for i in range(firstDelimiter, secondDelimiter + 1):
            listOfGensBetween.append(Parent1.genome[i])

        listOfGensFromSecondParent = []

        for i in range(secondDelimiter + 1, len(Parent2.genome) - 1):
            listOfGensFromSecondParent.append(Parent2.genome[i])
        for i in range(1, secondDelimiter + 1):
            listOfGensFromSecondParent.append(Parent2.genome[i])

        index = 0

        for i in range(secondDelimiter + 1, len(newGenome) - 1):
            while(True):
                if listOfGensFromSecondParent[index] not in listOfGensBetween:
                    newGenome[i] = listOfGensFromSecondParent[index]
                    index += 1
                    break
                else:
                    index += 1

        for i in range(1, firstDelimiter):
            while(True):
                if listOfGensFromSecondParent[index] not in listOfGensBetween:
                    newGenome[i] = listOfGensFromSecondParent[index]
                    index += 1
                    break
                else:
                    index += 1

        return newGenome

    def funcOfChangeGens(Parent1, Parent2): # Получение отдельно 2 наследников
        #firstChild = cycleCrossover(Parent1, Parent2)
        #secondChild = cycleCrossover(Parent2, Parent1)

        firstDelimiter = random.randint(1,len(Parent1.genome) - 1)
        while (True):
            secondDelimiter = random.randint(1,len(Parent1.genome) - 1)
            if (secondDelimiter >= firstDelimiter):
                break

        firstChild = orderCrossover(Parent1, Parent2, firstDelimiter, secondDelimiter)
        secondChild = orderCrossover(Parent2, Parent1, firstDelimiter, secondDelimiter)
        return [firstChild, secondChild]

    def functionOfReproduction(Par): # функция скрещивания
        Parents = copy.deepcopy(Par)

        for i in range(len(Parents) - 1): # Отсортируем в порядке убывания родителей
            minFitness = Parents[i].fitness
            index = i
            for j in range(i, len(Parents)):
                if minFitness > Parents[j].fitness:
                    index = j
                    minFitness = Parents[j].fitness
            Parents[i], Parents[index] = Parents[index], Parents[i]


        newPopulation = []
        for i in range(0, countOfBestChild):
            newPopulation.append(Way())
            for j in range(len(Parents[0].genome)):
                newPopulation[i].genome[j] = Parents[i].genome[j]
            newPopulation[i].culcFitness()

        testList = []

        #           *Турнирный отбор*
        for i in range(firstPopulationCount - countOfBestChild):
            listOfTournamentParticipant = []
            for j in range(0, sizeOfTournament):
                while (True):
                    y = random.randint(0, firstPopulationCount - 1)
                    if Parents[y] in listOfTournamentParticipant:
                        continue
                    else:
                        listOfTournamentParticipant.append(Parents[y])
                        break
            indexOfTheBest = 0

            for j in range(len(listOfTournamentParticipant) - 1):
                if listOfTournamentParticipant[indexOfTheBest].fitness > listOfTournamentParticipant[j + 1].fitness:
                    indexOfTheBest = j + 1
            testList.append(listOfTournamentParticipant[indexOfTheBest])
            listOfTournamentParticipant.clear()

        #                   **


        for i in range(0, len(testList), 2): # берем 2 пары дляскрещивания

            a = funcOfChangeGens(testList[i], testList[i + 1])  # Возвращение пары детей

            newPopulation.append(Way()) # пустой 1 ребенок


            for j in range(len(a[0])): # переписываем гены 1 ребенка
                newPopulation[i].genome[j] = a[0][j]
            newPopulation[i].culcFitness()

            newPopulation.append(Way()) # аналогично с 2

            for j in range(len(a[1])): # -//-
                newPopulation[i + 1].genome[j] = a[1][j]
            newPopulation[i + 1].culcFitness()

        return newPopulation

    # Расчет растояния между городами
    for i in range(len(cities)):
        mas = []
        for j in range(len(cities)):
            x = sqrt(pow(cities[j][0] - cities[i][0], 2) + pow(cities[j][1] - cities[i][1], 2))
            mas.append(round(x, 2))
        tOfLength.append(mas)

    Way.tableOfLength = tOfLength # таблица расстояния
    Ways = CreatingAPopulation(firstPopulationCount) # популяция из 6 представителей

    countOfIterations += 1
    for i in range(len(Ways)):
        Ways[i].culcFitness()
    minFitness1 = Ways[0].fitness
    bestWay1 = 0
    currentIteration = 0 # Переменна для кол-во операций
    while (True):
        currentIteration += 1
        for i in range(len(Ways)): # Выбор лучшего представителя
            if minFitness1 > Ways[i].fitness:
                minFitness1 = Ways[i].fitness
                bestWay1 = i

        t = functionOfReproduction(Ways)  # Создания дочерней популяции

        countOfIterations += 1

        minFitness2 = t[0].fitness
        bestWay2 = 0
        for i in range(len(t)): # лучший представитель в дочерней популяции
            if minFitness2 > t[i].fitness:
                minFitness2 = t[i].fitness
                bestWay2 = i


        if  currentIteration == maxIterationsCount: # если сделали 300 итераций , то заканчиваем работу
            break
        # Если выхода нет , то дочерняя становется главной и процес продолжается
        Ways = copy.deepcopy(t)
        minFitness1 = Ways[0].fitness
        bestWay1 = 0

    #bestWay = 0
    if bestWay1 < bestWay2:
        bestWay = bestWay1
    else:#Прорисовка стрелок
        bestWay = bestWay2
    for i in range(len(Ways[bestWay1].genome) - 1):
        if i == 0:
            canv.create_line(cities[Ways[bestWay].genome[i] - 1][0] + 500 + 2.5,
                             -cities[Ways[bestWay].genome[i] - 1][1] + 500 + 2.5,
                             cities[Ways[bestWay].genome[i + 1] - 1][0] + 500 + 2.5,
                             -cities[Ways[bestWay].genome[i + 1] - 1][1] + 500 + 2.5, width=2, arrow=LAST, fill="blue")
            continue
        canv.create_line(cities[Ways[bestWay].genome[i] - 1][0] + 500 + 2.5,
                         -cities[Ways[bestWay].genome[i] - 1][1] + 500 + 2.5,
                         cities[Ways[bestWay].genome[i + 1] - 1][0] + 500 + 2.5,
                         -cities[Ways[bestWay].genome[i + 1] - 1][1] + 500 + 2.5, width=2, arrow=LAST)


    labelPopulation.configure(text = str(countOfIterations))
    labelMutation.configure(text = str(mutationCount))
    labelMinLengh.configure(text=str(round(minFitness1, 2)))
    print("len par= ", len(Ways))
    print("Children = ", len(t))

    f = open('Cities.txt', 'a')

def createNewTest(event):
    global f
    f.close()
    f = open('Cities.txt', 'w')
    global firstTest
    global fromFile
    fromFile = False
    firstTest = True
    canv.delete(ALL)
    cities.clear()
    labelPopulation.configure(text = str(0))
    labelMutation.configure(text = str(0))
    labelMinLengh.configure(text=str(0))
    canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
    canv.create_line(0, 500, 1000, 500, width=2, arrow=LAST)


canv.bind('<Button-1>', getXY)
run.bind('<Button-1>', runAlgorithm)
canv.bind('<Motion>', getXY_M)
newTest.bind('<Button-1>', createNewTest)

canv.pack()
root.mainloop()



