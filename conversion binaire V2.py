class conversion_de_binaire:
    def __init__(self,nbrBinaire = 0 ,nbrBaseDix = 0,nbrCorrect=True, choixUtilisateur="B"):
        self.choixUtilisateur = choixUtilisateur
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

    def selection (self):
        while True:
            self.choixUtilisateur = input("Que voulez-vous faire ?\n"
            "Binaire vers base dix : B \n"
            "base dix vers binaire : D").strip().upper()
            if self.choixUtilisateur in ["B","D"]:
                break
            else :
                print ("Choix invalide, saisissez B ou D")
        return self.choixUtilisateur


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

    def verif_base_dix (self):
        self.nbrBaseDix = int(input("veuillez saisir un nombre inférieur a 255 : "))
        if self.nbrBaseDix > 255 :
            print("Le nombre saisi n'est pas correct...")
            self.nbrCorrect = False
            return

    def conversion_basedix_binaire (self):
        for i in range (8):
            if self.nbrBaseDix >= self.tableauBinaire[i][0]:
                self.nbrBaseDix = self.nbrBaseDix - self.tableauBinaire[i][0]
                self.tableauBinaire[i][1] = "1"
            else:
                self.tableauBinaire[i][1] = "0"

    def concatenation_basedix (self):
        self.nbrBinaire = [line[1] for line in self.tableauBinaire]
        self.nbrBinaire = "".join(self.nbrBinaire)
        return self.nbrBinaire



conversion = conversion_de_binaire()
conversion.selection()
if conversion.choixUtilisateur == "B":

    conversion.decoupe_binaire()
    resultat = conversion.converssion_binaire_base_dix()

    if conversion.nbrCorrect == True :
        print("Le nombre en base dix est : ", resultat)
    else :
        print("Ca a foiré ?")

else:
    conversion.verif_base_dix()
    conversion.conversion_basedix_binaire()
    resultat = conversion.concatenation_basedix()
    print("Le nombre en binaire est :", resultat)


