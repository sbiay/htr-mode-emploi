---
title: Mode d'emploi pour évaluer et entraîner un modèle HTR avec Kraken
---

Plan :

1. [Installer Python et Kraken](#t1)
2. [Exporter une vérité de terrain depuis e-Scriptorium](#t2)
3. [Placer la vérité de terrain dans un dossier dédié](#t3)
4. [Importer le modèle HTR](#t4)
5. [Évaluer le modèle Bicerin sur la vérité de terrain](#t5)
6. [Personnaliser le modèle Bicerin à l'aide de la vérité de terrain](#t6)
7. [Compléments (seulement pour Piccioncino)](#t7)

[comment]: <> (FINET)

Toutes ces opérations se passent dans une session **Ubuntu**.


<a id='t1'/>

# Installer Python et Kraken

1. Pour ouvrir le programme **Terminal** :
	
	1. Appuyer sur la touche `Windows`
	2. Taper au clavier `terminal`
	3. `Entrée`

2. Quand le programme est ouvert :

	- Pour agrandir le texte : `Ctrl Maj +` (touche en haut du clavier, après les numéros)
	- Pour diminuer le texte : `Ctrl -` (touche du numéro 6)

3. Pour installer Python 3 saisir la commande suivante (**NB** l'icône sur la droite de la commande permet de la copier ; pour la coller dans **Terminal**, faire Ctrl + Maj + V) :

    ```shell
    sudo apt-get install python3 libfreetype6-dev python3-pip python3-venv python3-virtualenv
    ```

4. Installer Kraken

	```shell
	pip install kraken
	```

# Renommer des images en foliotation

1. Télécharger le fichier [numerotation.csv](https://raw.githubusercontent.com/sbiay/htr-mode-emploi/main/numerotation.csv)

2. L'ouvrir

3. Ouvrir toutes les images à renommer dans [XnView](https://www.xnview.com/fr/xnviewmp/#downloads)

4. Sélectionner toutes les images à renommer et faire `Copier`

5. Dans le tableau `numerotation.csv`, se placer dans la située à droite du numéro de folio correspondant au début de la sélection

6. `Coller`, puis fermer en sauvegardant

7. Envoyer le fichier `numerotation.csv` à Piccioncino



<a id='t2'/>

# Exporter une vérité de terrain depuis e-Scriptorium

1. Sélectionner toutes les images de la vérité de terrain
2. Cliquer sur **Export**
3. Sélectionner la transcription **Manual**
4. Cocher **Include images**
5. Format **Alto**


<a id='t3'/>

# Placer la vérité de terrain dans un dossier dédié

1. Ouvrir **Terminal**

2. Se déplacer dans le dossier `Téléchargements/` :
	
	```shell
	cd ~/Téléchargements/
	```

3. Créer un nouveau dossier pour les entraînements :

	```shell
	mkdir -p ~/Bureau/htr/vt
	```

4. Extraire l'archive dans le nouveau dossier :

	```shell
	unzip {NOM DE LARCHIVE}.zip -d ~/Bureau/htr/vt
	```


<a id='t4'/>

# Importer le modèle HTR

1. Se déplacer dans le dossier `htr/` :

	```shell
	cd ~/Bureau/htr
	```

2. Créer un dossier pour les modèles :

	```shell
	mkdir modeles
	```

3. Télécharger le modèle Bicerin en cliquant [ici](https://github.com/HTR-United/cremma-medieval/releases/download/1.1.0/cremmamedievalnew_best.mlmodel)

4. Placer le modèle dans le dossier dédié :

	```shell
	mv ~/Téléchargements/cremmamedievalnew_best.mlmodel modeles/
	```


<a id='t5'/>

# Évaluer le modèle Bicerin sur la vérité de terrain

1. Se placer dans le dossier suivant :

	```shell
	cd ~/Bureau/htr
	```

2. Lancer la commande suivante :
	
	```shell
	ketos test -m ./modeles/cremmamedievalnew_best.mlmodel ./vt/*xml -f alto
	```

Quelle est l'*Average accuracy* ? C'est le pourcentage d'acuité du modèle 100% = parfait !


<a id='t6'/>

# Personnaliser le modèle Bicerin à l'aide de la vérité de terrain

C'est une opération potentiellement longue (plusieurs heures).


1. Se placer dans le dossier suivant :

	```shell
	cd ~/Bureau/htr
	```

2. Créer un dossier pour les modèles entraînés :

	```shell
	mkdir modeles/entrainement
	```

Lancer la commande :


```shell
ketos train -r 0.0001 --lag 20  -s '[1,120,0,1 Cr3,13,32 Do0.1,2 Mp2,2 Cr3,13,32 Do0.1,2 Mp2,2 Cr3,9,64 Do0.1,2 Mp2,2 Cr3,9,64 Do0.1,2 S1(1x0)1,3 Lbx200 Do0.1,2 Lbx200 Do.1,2 Lbx200 Do]' --device cpu --resize add -i ./modeles/cremmamedievalnew_best.mlmodel -f alto --output modeles/entrainement/ ./vt/*xml
```


<a id='t7'/>

# Compléments (seulement pour Piccioncino)

L'installation de Ubuntu sous Win10 est possible en ligne de commande ; voir [ici](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-2---check-requirements-for-running-wsl-2)

ketos train : J'ai retiré l'option --augment qui posait des problèmes avec le package albumentations.