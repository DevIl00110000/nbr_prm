def nbpre(mini,maxi):
        nbpre=True;
        i=mini # i prend la valeur de mini
        s=maxi # i prend la valeur de mini
        while (i<=s): # tant que i est inferieur ou egale a s
                nbdiv=0 # nombre de diviseurs de i
                j=1 #modulo de i
                while(j<=i): # tant que j inferieur ou egale a i
                        if i%j==0: #si le reste de la division de i par j est = a 0
                                nbdiv=nbdiv+1 # alors il y a un nouveau diviseur de i
                        if nbdiv>2: # (Optimisation du code) -> permet darreter la boucle s'il y a plus de 2 diviseurs (1 et i)
                            j=i+1 # arrete la boucle
                        else:     # Sinon
                            j=j+1 # ajoute 1 a j et continu
                if nbdiv==2: #si nbdiv egale 2
                        print("=>" + str(i)) # alors on affiche i
                i=i+1 # on ajoute 1 a i et on continu

if __name__ == '__main__':     # Program start from here
          min = 5000;
          max = 10000;
          try:
                nbpre(min, max);
          except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                print("")
                print("END")



# i prend la valeur de mini
# i prend la valeur de mini
    # BOUCLE_1 tant que i est inferieur ou egale a s
        # nombre de diviseurs de i
        # j modulo de i prend la valeur 1
        # BOUCLE_2 tant que j inferieur ou egale a i
            #si le reste de la division de i par j est = a 0
            # alors il y a un nouveau diviseur de i
            # Si nbdiv > 2 (Optimisation du code) -> permet darreter la boucle s'il y a plus de 2 diviseurs (1 et i)
            #arrete la boucle
            # Sinon
            # ajoute 1 a j et continu
            # Fin de BOUCLE_2
        #si nbdiv egale 2
            # alors on affiche i
            # Fin de BOUCLE_1
# on ajoute 1 a i et on continu