# nbr_prm
- A script to calculate the **prime numbers** between Mini and Maxi.
- And a file with the first 7,805 prime numbers.

``` python
def nbpre(mini,maxi):
	nbpre=True;
	i=mini                                # i prend la valeur de mini
	s=maxi                                # i prend la valeur de mini
	while (i<=s):                         # tant que i est inferieur ou egale a s
		nbdiv=0                       # nombre de diviseurs de i
		j=1                           #modulo de i
		while(j<=i):                  # tant que j inferieur ou egale a i
			if i%j==0:            #si le reste de la division de i par j est = a 0
				nbdiv=nbdiv+1 # alors il y a un nouveau diviseur de i
			if nbdiv>2:           # (Optimisation du code) -> permet darreter la boucle s'il y a plus de 2 diviseurs (1 et i)
				j=i+1         # arrete la boucle
			else: # Sinon
				j=j+1         # ajoute 1 a j et continu
		if nbdiv==2:                  #si nbdiv egale 2
			print("=>" + str(i))  # alors on affiche i
		i=i+1                         # on ajoute 1 a i et on continu
```
