import csv
import os
import shutil

donnees = []
with open("numerotation.csv") as csvf:
	lecteur = csv.reader(csvf, delimiter='\t', quotechar="|")

	for l in lecteur:
		foliotation = l[0]
		fichier = l[1].split("/")[-1]
		if not l[1] and not l[0]:
			break
		if l[0] and l[1]:
			donnees.append([foliotation, fichier])

for d in donnees:
	shutil.copy(d[1], f"./sortie/{d[0]}.jpg")