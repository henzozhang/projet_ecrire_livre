
import sqlite3 
from datetime import datetime

import function

def create_comment(text,ChapterID,UserID):
    """
    fonction create_comment
    :parametre text,ChapterID,UserID
    :return bdd.Comment
    """

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""INSET INTO comment VALUE(?,?,?,?,?),""" (None,ChapterID,UserID,str(datetime.now()),text ))
    connexion.commit()
    connexion.close()

test="il etais un fois dans un royaume des Francs"
chapiterID = "chapitre1"
UserID = "004"

create_comment("il etais un fois dans un royaume des Francs",0,4)