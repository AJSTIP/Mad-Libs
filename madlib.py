#import module
from tkinter import *

# initialize window
root = Tk()
root.geometry('600x600')
root.title('Super Epic Mad Libs Generator')
Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()
Label(root, text='Please Choose one :', font='arial 15 bold').place(x=200, y=80)


################Stories##############

def madlib1():

    person = input('please enter a person : ')
    place = input('please enter a place: ')
    adjetive = input('please enter a adjetive: ')
    verb = input('please enter a verb: ')
    food = input('food name: ')
    print('Who knew ' + person + 's , favorites place was ' + place + ' they have lived there for many years they describe it as ' + adjetive + ', while they were out today they ' +
          verb + ' to cheer them up they got there favorite food ' + food + '.')


def madlib2():

    celebrity = input('please enter a celebrity : ')
    place = input('please enter a place: ')
    animal = input('please enter an animal: ')
    personTwo = input('please enter person twos name: ')
    personTwoJob = input('occupation name: ')
    print('Oh no ' + celebrity + ' has gone missing, they were last seen outside ' + place + ' while walking their ' +
          animal + ' luckily ' + personTwo + ' who is a ' + personTwoJob + ' went looking and found them! ')


def madlib3():
    creature = input('please enter a creature: ')
    creatureName = input('please enter the creatures name : ')
    foods = input('enter food item : ')
    verb = input('enter a verb: ')
    place = input('enter place : ')

    print('Today I saw a ' + creature + ' right near ' + place + ' Its name was '+creatureName + ' and its favorite food was ' +
          foods + '. Unfortunately it was all out of ' + foods + 'It saw me and I had no choice but to ' + verb + '.')


# buttons
Button(root, text='Favorite Place', font='arial 15',
       command=madlib1, bg='ghost white').place(x=225, y=120)
Button(root, text='Missing Celebrity', font='arial 15',
       command=madlib2, bg='ghost white').place(x=210, y=180)
Button(root, text='Magical Beast', font='arial 15',
       command=madlib3, bg='ghost white').place(x=220, y=240)

root.mainloop()
