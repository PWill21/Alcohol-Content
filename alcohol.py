
## Program Name: alchohol.py
## Programmer: Patrick Will
## Date: 6/16/2018
## Purpose: A program to find the alcohol content in ounces of an alcoholic drink

#variables
abv = float(input('What is the ABV in percent?: '))
volume = float(input('What is the volume in ounces?: '))

#functions
def CalculateTotalAlcohol(v,a):
    total_alchohol = v * (a / 100)
    print(total_alchohol, 'ounces')

CalculateTotalAlcohol(volume,abv)
