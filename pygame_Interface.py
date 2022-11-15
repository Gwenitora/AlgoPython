import sys
import pygame

#definir une class Grille 
class Grille :
    
    #definir une classe __init__ (variable special = __ __ ) de parametre self , ecran 
    def __init__(self,ecran):
        
        #initialisé self.ecran egale ecran 
        self.ecran = ecran
        
        # initialiser self.ligne egale a une liste [( (200,0),(200,600)),((400,0),(400,600)),((0,200),(600,200)),((0,400),(600,400)),]
        self.lignes = [( (200,0),(200,600)),
                       ((400,0),(400,600)),
                       ((0,200),(600,200)),
                       ((0,400),(600,400)),]
    
        
    #definir une fonction afficher de parametre self 
    def afficher(self):
        #pour toute les ligne dans l'argument self.ligne 
        for ligne in self.lignes : 
            #dessiner en noir les argument d'index 0 et 1 d'epaisseur 10 
            pygame.draw.line(self.ecran,(0,0,0),ligne[0],ligne[1],10)
            
            
            
#definir une class jeu
class Jeu :
    #definir un init de parametre self
    def __init__(self) :
        
        #Ouvrir une fenetre de 600 par 600 
        self.ecran = pygame.display.set_mode((600,600))
        
        #donner un titre a la fenetre 
        pygame.display.set_caption('Morpion pas dans le calfrock mon copain' )
        
        #initialisé self.jeu_encours a True 
        self.jeu_encours = True
        
        #initialisé dans la class jeu self.grille egale Grille(self.ecran) / 
        self.grille = Grille(self.ecran)
        
        
        
    #definir fonction_principal de parametre self :   
    def fonction_principale(self):
        #tant que self.jeu_encours
        while self.jeu_encours:
            #pour tout les evenement se trouvant dans pygame
            for event in pygame.event.get():
                #si le type d'evenement est equivalent a pygame.QUIT / si le joueur clique sur la croix 
                if event.type == pygame.QUIT:
                    #alors sortir du sys / fermer la fenetre 
                    sys.exit()
            #donné une couleur de type ((150,150,150))
            self.ecran.fill((150,150,150))
            
            #rappeler la fonction self.grille.afficher / afficher les grille 
            self.grille.afficher()
            
            #rafraichissement de l'ecran 
            pygame.display.flip()




#si __name__ est equivalent a '__main__'
if __name__ == '__main__': 
    #Alors appeler la fonction init  
    pygame.init()
    #Alors appeler la fonction fonction_principale se trouvant dans la class jeu 
    Jeu().fonction_principale()
    #Alors appeler la fonction quit
    pygame.quit( )