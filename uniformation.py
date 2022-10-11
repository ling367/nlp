#! usr/bin/python3
#programme a pour but d'unifier les étiquettes de la sortie de TreeTagger avec celles d'Udpipe
# il prend en argument le code de la rubrique
import re
import sys
def normalisation(texte):
#il prend un string comme argument
	#texte=re.sub("NOM","NOUN",texte)
	texte=re.sub("NOM(:([a-z]{3}))?","NOUN",texte)
	#texte=re.sub("PRP","ADP",texte)
	texte=re.sub("PRP(:det)?","ADP",texte)
	#texte=re.sub("PUN","PUNCT",texte)
	texte=re.sub("PUN(:([a-z]{3}))?","PUNCT",texte)
	texte=re.sub("SENT","PUNCT",texte)
	texte=re.sub("DET:([A-Z]{3})","DET",texte)
	texte=re.sub("VER:([a-z]{4})","VERB",texte)
	texte=re.sub("ABR","NOUN",texte)
	texte=re.sub("KON","CCONJ",texte)
	texte=re.sub("PRO(:([A-Z]{3}))?","PRON",texte)
	texte=re.sub("NAM","PROPN",texte)
	#texte_unif=re.sub("NUM","NOUN",texte10)
	return texte
#-------------------------------------------	
rub_num = sys.argv[1]
print ("Normalisation sortie TTagger XML:",rub_num)
INPUT = open("./BAO2/BAO2_Pl_Tree_tagger{}.xml".format(rub_num),"r", encoding="UTF-8").readlines()
texte = "".join(INPUT)

INPUT2= open("./BAO2/BAO2_Py_Tree_Tagger{}.xml".format(rub_num),"r", encoding="UTF-8").readlines()

texte2 = "".join(INPUT2)


#Créer deux fichiers de sortie pour mettre les données unifiées:
#pas besoin d'écrire l'entête et la grande balise d'ouverture car le fichier d'entrée est bien en xml
OUT = open("./BAO3/BAO3_Pl_Tree_tagger{}.xml".format(rub_num),"w", encoding="UTF-8")
#attention à mettre la fonction exécuté avant la fonction write sinon on va juste écrire l'entrée mais pas 
#les données de sortie.
texte_uni_pl = normalisation(texte)
OUT.write(texte_uni_pl)


OUT2 = open("./BAO3/BAO3_Py_Tree_tagger{}.xml".format(rub_num),"w", encoding="UTF-8")
normalisation(texte2)
texte_uni_py = normalisation(texte2)
OUT2.write(texte_uni_py)

#on a donc pas besoin non plus d'écrire la grande balise fermante
OUT.close()
OUT2.close()

print ("\nTerminée")
