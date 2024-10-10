class conversion_de_binaire:
    def __init__(self,nbrBinaire = 0 ,nbrBaseDix = 0,nbrCorrect=True):
        self.nbrCorrect = nbrCorrect
        self.nbrBinaire = nbrBinaire
        self.nbrBaseDix = nbrBaseDix
        self.tableauBinaire = [
         [128, None],
         [64,None],
         [32,None],
         [16,None],
         [8,None],
         [4,None],
         [2,None],
         [1, None]
        ]

    def decoupe_binaire (self):
        self.nbrBinaire = input("veuillez saisir votre octet en binaire : ")
        if len(self.nbrBinaire) > 8 :
            print ("Un octet j'ai dis...")
            return
        for i in range(8):
            self.tableauBinaire[i][1] = str(self.nbrBinaire)[i]
            if str(self.nbrBinaire)[i] not in ["0", "1"]:
                print("le binaire c'est que des 0 ou 1...")
                self.nbrCorrect = False
                return

    def converssion_binaire_base_dix (self):
        self.nbrBaseDix = 0
        for i in range(8):
            if self.tableauBinaire[i][1] == "1":
                self.nbrBaseDix = self.nbrBaseDix + self.tableauBinaire[i][0]
        return self.nbrBaseDix


conversion = conversion_de_binaire()

conversion.decoupe_binaire()
resultat = conversion.converssion_binaire_base_dix()

if conversion.nbrCorrect == True :
    print("Le nombre en base dix est : ", resultat)
else :
    print("Ca a foiré ?")



