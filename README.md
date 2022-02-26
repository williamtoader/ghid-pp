# Fișă de lucru
Voi actualiza lista cu mai multe probleme în măsura în care am timpul.

O să pun câteva indicații la problemele date.

În fișierul `cheats.py` voi pune cateva secvențe de cod care pot fi utile.

# Set de probleme dat la examenul de anul acesta:
(Work in progress)

## Proba 1


### Problema 1
Să se determine toate datele palindrom din secolul 21 (in orice ordine).
Exemple (cateva date palindrom): 10.02.2001, 20.02.2002, 01.02.2010, ..., 13.02.2031, 29.02.2092

### Problema 2

Din fisierul studenti.txt se citesc, pe cate o linie, separate prin virgula si un singur spatiu, urmatoarele date despre un student:

- cnp;
- nume si prenume;
- un sir de perechi nota – numar de credite;  
  
Scrieti o functie cu un numar variabil de argumente numite prin care sa se afiseze in fisierul rezultate.out, pentru fiecare student, pe cate o linie, numele si numarul de credite acumulate. Pentru a lua numarul de credite aferent unui examen este necesara promovarea lui.

Exemplu:
```
INPUT

studenti.txt

6030303100600, Crisan Maria, 10 - 4, 9 - 4, 10 - 3, 9 - 4
5030303100870, Florea Dorin, 10 - 3, 9 - 3, 10 - 4, 8 - 4, 10 - 2
5021218123456, Manaila Alin, 7 - 4, 4 - 3, 9 - 3, 8 - 3, 6 - 3
6021027456456, Toader Georgiana, 4 - 3, 4 - 4, 8 - 4, 8 - 3, 6 - 2

OUTPUT

rezultate.txt

030303100600, Crisan Maria, 15
5030303100870, Florea Dorin, 16
5021218123456, Manaila Alin, 13
6021027456456, Toader Georgiana, 9
```

### Problema 3
Din fișierul sarbatori.txt se citesc următoarele informații (in aceasta forma):
```
01.01        Vasile, Vasilica
07.01        Ioan, Ion, Ioana
30.01        Grigore
10.02        Valentin, Valentina, Vali
23.04        Gheorghe, Georgeta, Gica, Geta
21.05        Elena, Constantin, Costel, Costin, Cosmin, Lenuta, Ilinca
29.06        Petru, Pavel, Petrica
12.07        Veronica
20.07        Ilie
30.08        Alex, Alexandru, Alexandra
08.09        Maria, Marian
08.11        Mihai, Gabriel, Gabi, Mihaita
06.12        Nicolae, Nicoleta, Nicu, Nicusor
07.12        Filofteia
27.12        Stefan, Stefania
```

O regulă stabilită în M&K Company este ca, în oricare zi ce se regăsește în fișierul sarbatori.txt să se acorde fiecărui angajat sărbatorit (ce are unul dintre prenume ce apare în fișier, în dreptul sărbătorii) un bonus echivalent cu 10% din salariul lunar.

Se citesc de la tastatură, de pe o singura linie, numele de familie, toate prenumele și salariul unui angajat, separate prin cate un spatiu. Să se verifice dacă astăzi (data curentă) angajatul primește sau nu bonus, astfel:

- în cazul în care ziua este una obișnuită (nu apare în fișierul sarbatori.txt) se va afișa mesajul Zi fara bonusuri;
- dacă data current apare printre cele din fișier, atunci se va afișa mesajul: Angajatul…(nume prenume) primeste astazi un bonus de ..(suma calculata, acel 10% din salariu).. de lei.

Exemplu:

INPUT  
Georgescu Marian Grigore  4000

OUTPUT  
Dacă data curentă este 04 feb. 2022, atunci se va afisa mesajul  
`Zi fara bonusuri.`  
Dacă data curenta este 30 ian. 2022, atunci se va afisa mesajul  
`Angajatul Georgescu Marina Grigore primeste astazi un bonus de 400 de lei.`  

### Problema 4
Se citeste n de la tastatura. Gigel și George generează aleator cȃte o listă de n numere de maxim 4 cifre. Cȃștigă cel care are ȋn listă mai puține numere prime. Se joacă 3 runde. Determinaţi cine este cȃștigătorul după 3 runde (afisare in consola).\

### Problema 5
Pentru firma P&G  se organizează o tombolă. Din fisierul angajati.in se citesc, de pe cate o linie a fisierului, numele si prenumele cate unui angajat. Se citeste de la tastatura un numar natural k, mai mic decat numarul liniilor din fisierul angajati.in. Să se afiseze in fisierul extragere.out k nume diferite de angajati, la intamplare, din cele existente in fisierul angajate.in.  

Exemplu:  
Daca fisierul angajati.in contine  

```
Jercan Elena
Ion Horia
Marin Ioana-Daniela
Neagoe Marina
Florescu Teodora
Popa Diana
Radu Tatiana
```
si k = 4, atunci fisierul extragere.out poate contine  

```
Neagoe Marina
Popa Diana
Radu Tatiana
Ion Horia
```

## Proba 2

### Problema 1
a) Scrieti o functie care verifica daca un numar natural, primit ca parametru, este sau nu palindrom.

b) Din fișierul numere.txt se citesc numere naturale, separate prin virgula si/sau spatii/pe mai multe linii. Apeland functia scrisa la punctul a) si folosind metoda Divide et Impera să se determine cate numere palindrom sunt in fisier. Rezultatul se afiseaza in consola.

### Problema 2
Din fisierul “date.txt” se citesc numere intregi (asezate pe mai multe linii). Se citeste de la tastatura un numar intreg S. Să se determine, folosind un algoritm de complexitate O(n log n), utilizand metoda Divide et Impera, doua numere naturale din sir, T1 si T2, cu proprietatea ca T1 + T2 = S. Se garanteaza ca exista o pereche unica T1, T2 cu proprietatea ceruta. Afisarea se va face in fisieul “date.out”. (Indiciu: cautare binara).

Exemplu:

INPUT  
date.txt  
```
2   4   8  -5
-20  13   1   3
```  
consola  
```
7
```  
OUTPUT  
date.out  
```
3   4
```

---

# Set de probleme dat la examenele din anii trecuți:

### Problema 1

Fara a folosi structuri repetitive, determinati numarul de valori de 1 din scrierea
binara a unui numar citit de la tastatura.
Exemplu: pentru 147 se va afișa 4.


### Problema 2

Fara a folosi structuri repetitive, afisati o singură dată, 
în ordine lexicografică, vocalele folosite intr-un text citit din fisierul text.txt.
```
Input:
Fisierul text.txt conține
Ana are mere.
Output:
A, a, e
```

### Problema 3

Se citește de la tastatură un număr natural n, 
apoi n numere întregi ce se vor memora într-o colecție A. 
Se citește de la tastatură un număr natural m, 
apoi m întregi ce se vor memora într-o colecție B.
Ex.: n=6, A: 113, -4, 7, -4, -5, -109 și m=7, B: 120, 178, -4, -4, -4, 120, -109
Să se afișeze o singură dată elementele negative din A care apar și în B.                                          
Ex.: pentru colecțiile de mai sus, se va afișa șirul -4, -109.   


### Problema 4

Se da un text literar in limba romana, fara diacritice, 
care respecta toate regulile ortografice ale limbii romane 
(fara spatii nepotrivite, semne de punctuatie gresite, etc). 
Să se afișeze in consola, pe o singura linie, separate prin virgule, 
cuvintele din text în ordinea crescătoare a numărului de caractere, 
iar pentru cele de aceleași lungime, ordonarea se va face alfabetic 
(vom considera majuscule înaintea literelor mici – conform ordinii codurilor ASCII).


### Problema 5

Fie o listă ce conține liste sau tupluri încuibate 
(ex.: l =  [1, [2,3], [4, 5, (6, (7, 8, 9))], 10]. 
Să se transforme într-o listă simplă, fără a folosi liste suplimentare, 
păstrând ordinea elementelor. 


### Problema 6

Intr-o companie, in ultima vineri din fiecare luna se tine o mica petrecere, 
pentru cei care sunt nascuti in respectiva luna. Din fisierul date.in se citesc, 
de pe cate o linie, numele unei persoane si data nasterii, in formatul zz.ll.aaaa 
(ca in exemplu).
In fisierul date.out sa se afiseze pentru fiecare luna in parte data la care are 
loc petrecerea si numele sarbatoritilor (ca in exemplu).
Exemplu
```
INPUT
date.in
Popa Daniela   10.03.1986
Ion Laurentiu  	18.07.1990
Tatu Elena  	        	11.03.1986
Grigore Denisa       	   27.08.2001
Georgescu Florin    	 	18.07.2000
Dinu Andrei            	10.03.1997
Pop Floarea            	20.04.1970
OUTPUT
-        pentru anul 2021 se va afisa:
26 martie 2021: Popa Daniela, Tatu Elena, Dinu Andrei
30 aprilie 2021: Pop Floarea
30 iulie 2021: Ion Laurentiu, Georgescu Florin
27 august 2021: Grigore Denisa
```

### Problema 7

Din fisierul date.in se citesc, de pe cate un rand, 
numele si data angajarii pentru fiecare salariat dintr-o 
companie (ca in exemplu). Sa se afiseze in fisierul date.out 
numele angajatilor care au o vechime mai mare de 5 ani completi 
(nu se vor face rotunjiri: de exemplu, un angajat cu vechime de 4 ani, 
11 luni si 10 zile nu va fi afisat).
Exemplu:
```
INPUT
date.in
Popa Daniela   10.03.2018
Ion Laurentiu  	18.07.2020
Tatu Elena              	30.01.2016
Grigore Denisa       	   27.08.2015
Georgescu Florin    	 	29.01.2016
Dinu Andrei            	10.03.2010		
Pop Floarea            	20.04.2020
```

### Problema 8

Presupunem că reținem date despre compania M&K. 
Se citesc din fisierul angajati.txt urmatoarele date:
-    	pe prima linie a fișierului: 
            n (număr natural, ce reprezintă numărul de angajați);
-    	pe linia a doua: numele primului angajat;
-    	pe linia a treia: salariul primului angajat;
-    	pe linia a patra: numele celui de-al doilea angajat;
-    	pe linia a cincea: salariul celui de-al doilea angajat;
-    	…… idem și pentru ceilalți angajați, până la n.

Să se afișeze în fișierul angajati.out toți angajații cu toate numele corectate, 
ordonate alfabetic. Pentru angajați cu același nume de familie aceștia 
vor apărea ordonați după salariu, descrescator.

```
Input:	   5
po__pesC!u  ..Ma4r%iA....
4500
CozM9a// ...* Al)iNa!
4400
AnT0onEs%6*--cu   .+-.  Ion cOrn33eL;'.
4100
C09o(Zm--...a          andR!!_ei/.,,.
4500
AnT0onEs%6cu   .+-.   duMit*7ru.. cOrn33eL;'.
4000

   Output: 	   Antonescu Ion Cornel
   Antonescu Dumitru Cornel
   Cozma Andrei
   Cozma Alina
   Popescu Maria 
```

### Problema 9

Într-un spațiu pentru îngrijirea vârstnicilor există obiceiul ca în 
prima sambata de după aniversarea unui bătrân să i se facă o petrecere într-o 
sală de festivități. Personalul trebuie să cunoască câte aniversări sunt la fiecare 
dată (pentru a ști câte cadouri să pregătească). Se citește din fisierul date.in 
numarul natural n apoi, pentru n persoane, pe cate o linie, numele și data nașterii, 
în formatul zz-ll-aaaa (ca in exemplu). Afișați în fișierul date.out toate datele 
calendaristice în care vor fi următoarele lor aniversări, împreună cu 
persoanele aniversate la fiecare dată. Datele afișate vor fi 
ordonate descrescător după numărul de persoane aniversate la respectivele date. 
Dacă ziua bătrânului pică în weekend, 
atunci el va fi sărbătorit în sâmbăta din respectivul weekend.
Exemplu:
```
INPUT
date.in
7
Popa Daniela   10-03-1931
Ion Laurentiu-Mihai  	18-07-1940
Tatu Elena Diana      	09-03-1936
Grigore Denisa   	27-08-1928
Georgescu Florin  	20-07-1928
Dinu Andrei     	13-03-1937

Pop Floarea    	30-03-1943
OUTPUT (valabil pentru rularea codului in dec. 2021)
12-03-2022  Popa Daniela, Tatu Elena Diana, Dinu Andrei
23-07-2022   Ion Laurentiu-Mihai, Georgescu Florin
27-08-2022   Grigore Denisa
02-04-2022  Pop Floarea
```

### Problema 10

Se citește din fisierul date.in numarul natural n apoi, pentru n persoane, 
pe cate o linie, numele și CNP-ul. Sa se afiseze in fisierul date.out numele 
persoanelor care se pensioneaza in luna curenta 
(cea in care are loc executia codului). Se considera ca varsta de pensionare pentru 
femei este 63 de ani, iar pentru barbati de 65 de ani.
```
INPUT
7
Popa Daniela   2800808100567
Ion Laurentiu  	1560120180567
Tatu Elena       	2580112100987
Grigore Denisa   	6011218100234
Georgescu Florin  	6020818100541
Dinu Andrei     	1700911180507
Pop Floarea    	2580312133987
OUTPUT
-          considerand ca rulam codul azi, 29.01.2021, se vor afisa numele:
Ion Laurentiu, Tatu Elena     	
```

### Problema 11

Se citește din fisierul date.in numarul natural n apoi, pentru n persoane, 
pe cate o linie, numele și CNP-ul. Sa se afiseze in fisierul date.out 
numele persoanelor care se pensioneaza in anul curent 
(cel in care are loc executia codului). Se considera ca varsta de pensionare 
pentru femei este 63 de ani, iar pentru barbati de 65 de ani.


### Problema 12

Din fisierul rezultate.in se citesc, de pe cate o linie, numele si 
trei note obtinute de cate un absolvent de liceu la examenul de bacalaureat 
(ca in exemplu). Sa se afisez in fisierul rezultate.out numele absolentilor, 
impreuna cu notele, ordonate descrescator dupa media celor 3 note (ca in exemplu). 
Daca exista mai multi absolventi cu aceeasi medie, ei vor fi 
afisati in ordine alfabetica.
Exemplu:
```
INPUT
rezultate.in
Vasile Elena   9	10     9.8
Popescu Maria    	10   9.2    9.6
Pop Mircea 	5.5 	8.2    6.7
Radu Laura    	8.4	5.5      7.8
Ene Florin     	8.9   7.8    5.6
Toma Ilena  	5.5 	5   5.6
OUTPUT
rezultate.out
Popescu Maria   10   9.2    9.6
Vasile Elena   9	10     9.8
Ene Florin     	8.9   7.8    5.6
Radu Laura    	8.4	5.5      7.8
Pop Mircea 	5.5 	8.2    6.7
Toma Ilena  	5.5 	5   5.6
```

### Problema 13

Din fisierul raport.txt se citeste un text literar, ce contine litere ale 
alfabetului englezesc si semnele de punctuatie uzuale. Sa se afiseze propozitiile 
ordonate descrescator dupa numarul de valori numerice ce apar in text. 
Se vor folosi ori de cate ori este posibil expresiile regulate. 
Daca exista mai multe propozitii cu acelasi numar de valori numerice 
se va afisa mai intai propozitia cu mai multe cuvinte 
(si valorile numerice se vor numara drept cuvinte).
Exemplu:
```
INPUT
raport.txt
Anul trecut, din 32 de copii, 18 s-au inscris la cercul de pictura, 
13 la cel de dansuri si restul la cercul de carting. Din acestia, 
pe parcursul anului, 3 au abandonat toate cercurile pe care le frecventau. 
Anul acesta s-au inscris cu 10 elevi mai multi fata de anul anterior.
OUTPUT
Anul trecut, din 32 de copii, 18 s-au inscris la cercul de pictura, 
13 la cel de dansuri si restul la cercul de carting.
Din acestia, pe parcursul anului, 3 au abandonat toate cercurile 
pe care le frecventau.
Anul acesta s-au inscris cu 10 elevi mai multi fata de anul anterior. 
```

### Problema 14

Se citeste din fisierul text.txt un text oarecare 
(pe una sau mai multe linii, eventual vide). 
Sa se afiseze in fisierul rezultat.txt 
numarul valorilor cu exact 4 cifre din fisierul text.txt. 
Nu se vor folosi structuri repetitive si se vor utiliza expresii regulate.
Exemplu:  
```
INPUT
text.txt
Primul razboi mondial s-a declansat in Europa si a durat de la 28 iulie 1914 
pana pe 11 noiembrie 1918, la care au participat peste 70 de milioane de militari, 
inclusiv 60 de milioane de europeni, mobilizati intr-unul dintre cele mai mari 
razboaie din istorie 
(sursa: https://ro.wikipedia.org/wiki/Primul_R%C4%83zboi_Mondial). 
OUTPUT
rezultat.txt
2
```


### Problema 15

Pentru un turist ce doreste sa se cazeze la pensiunea Viata fara griji, 
cititi de la tastatura, in aceasta ordine: CNP-ul, numele, o data de cazare, 
o data de decazare (datele vor fi în formatul zz-ll-aa), 
numarul de adulti si numarul de copii (cu varsta intre 5 si 12 ani). 
Copiii cu varsta peste 12 ani vor fi considerati adulti. 
Copiii (cu varsta intre 5 si 12 ani) au o reducere de 50%. 
Camerele sunt duble (de cate doua persoane). 
Intregului sejur se aplica, in plus, o reducere de 10% daca numarul de 
nopti pentru care s-a facut cazarea este mai mare de 5. 
Tarifele stabilite de pensiune sunt:
-   	cazare in zilele de duminica si de luni pana joi: 100 lei / camera;
-   	cazare in zilele de vineri si sambata: 120 lei / camera.
Folositi metoda safe_substitute pentru a afisa un mesaj de forma:
 
```
Stimate/stimata domnule/doamna (in functie de CNP) …(nume, prenume)……….,
 
Ati solicitat …(completati)… nopti de cazare, din care ….(completati)…. tarifate cu 100 lei / noapte si …….(completati)…. cu 120 lei / noapte. Din ……(completati)…. persoane, …..(completati)…… sunt adulti si …(completati)… sunt copii. Numar de camera ocupate: ….(completati)…. Nu beneficiati / Beneficiati de reducerea de 10% aplicata pentru sejururile mai mari de 5 nopti.
Total de plata: ……(completati) ….. lei.

Va dorim un sejur placut!
 
Pensiunea “Viata fara griji”
```

Exemplu:
```
INPUT
2801012300800
Popescu Diana
02-06-21
08-06-21
3
2
```



### Problema 16

n fisierul de intrare plecare_Bucuresti.txt se afla, pe cate o linie, 
numele unui oras, urmat de “: ”, impreuna cu pretul unui bilet, de adult, 
clasa a 2-a, cu loc, de la compania CFR din orasul Bucuresti catre respectivul 
oras (regim IR – InterRegio).  
Pretul este numar zecimal (in care se foloseste “.” 
ca separator – ca in exemplul de mai jos).
CFR are urmatoarele reduceri:
-   	15%, daca biletul se cumpara cu anticipatie de cel putin 21 de zile;
-   	10%, daca biletul se cumpara cu anticipatie intre 11 si 20 de zile;
-   	5%, daca biletul se cumpara cu anticipatie intre 6 si 10 de zile.

Pentru calculul numarului de zile se numara ziua plecarii, dar nu ziua in care 
este cumparat biletul.
Sa se citeasca de la tastatatura o data calendaristica, 
in formatul zz-ll-yyyy (exemplu: 12-03-2020), 
ce reprezinta data plecarii intr-o calatorie, 
pentru care vrem sa achizitionam biletul si un oras (dintre cele din fisier). 
Sa se afiseze in consola care este pretul biletului, 
cu reducerea maxima ce se poate aplica.
```
        	INPUT
        	plecare_Bucuresti.txt
        	Brasov: 48.6
            Galati: 60.1
        	Arad: 100.9
        	Cluj-Napoca: 90.8
        	Iasi: 90.8
        	
        	Consola:
        	Arad
        	22-06-2021
        	
        	OUTPUT
        	90.81  
```

Explicatie (nu face parte din OUTPUT): 
considerand ca se cumpara biletul azi, 2.06.2021, 
se poate aplica reducerea maxima de 10% 
(mai sunt 20 de zile pana in ziua plecarii: 22-06-2021).


### Problema 17

In fisierul de intrare plecare_Bucuresti.txt se afla, pe cate o linie, 
numele unui oras, urmat de “: ”, impreuna cu pretul unui bilet, 
de adult, clasa a 2-a, cu loc, de la compania CFR din orasul Bucuresti 
catre respectivul oras (regim IR – InterRegio).  
Pretul este numar zecimal (in care se foloseste “.” ca 
separator – ca in exemplul de mai jos). CFR aplica o reducere de 
weekend (sambata-duminica) de 15%. Fiind sezonul estival, 
la aceasta reducere se adauga o reducere de 10% 
(indiferent de ziua din saptamana in care are loc calatoria) 
daca destinatia este un oras din fisierul orase_reduceri.txt, 
in care numele oraselor sunt separate prin virgule/spatii/pe mai multe linii.
Sa se citeasca de la tastatura doua date calendaristice in 
formatul zz-ll-yyyy (exemplu: 12-03-2020), ce reprezinta data 
plecarii si data intoarcerii si orasul de destinatie. 
Sa se afiseze pretul total al celor doua bilete, 
dupa aplicarea tuturor reducerilor posibile.
```
INPUT
        	plecare_Bucuresti.txt
        	Brasov: 48.6
        	Constanta: 59.6
            Galati: 60.1
        	Arad: 100.9
        	Cluj-Napoca: 90.8
        	Iasi: 90.8
        	Mangalia: 60.2
        	
        	orase_reduceri.txt
        	Constanta,   Mangalia
        	
Consola:
12-06-2021
14-06-2021
Constanta
 
OUTPUT
98.34 
Explicatii (nu fac parte din OUTPUT): 12-06-2021 este zi de weekend, 
deci se aplica reducerea de 15%, iar 14-06-2021 este zi de luni (fara reducere). 
Pentru ambele bilete (zile) se adauga reducerea pentru orasul Constanta.
```

### Problema 18

Datele de 25.12 si 26.12 din fiecare an sunt zile de concediu 
(indiferent de ziua din saptamana in care cad). 
Stiind ca intodeauna sambata si duminica sunt zile libere, 
afisati pentru anul curent care va fi prima zi lucratoare de dupa Craciun 
(in format zz.ll.aaaa).
Exemple: pentru anul 2020 s-ar afisa 28.12.2020, iar pentru anul 2021 
s-ar afisa 27.12.2021


### Problema 19

Intr-o companie, data de 1 mai este libera. 
Daca aceasta cade intr-o zi de joi, se considera ca ziua de vineri va fi, 
de asemenea, zi libera. Similar, daca 1 mai ar cadea intr-o zi de marti, 
atunci si ziua de luni va fi libera. 
Afisati care sunt toate zilele libere din preajma lui 1 mai anul curent, 
conform regulii anterioare.
Exemple: pentru anul 2019 s-ar afisa 1.05.2019 (1 mai 2019 a fost miercuri), 
pentru anul 2020 s-ar afisa 1.05.2020, 2.05.2020, 3.05.2020 
(1 mai 2020 a fost vineri), pentru anul 2021 s-ar afisa 1.05.2021, 
2.05.2021 (1 mai 2021 va fi sambata), 
iar pentru anul 2025 s-ar afisa 1.05.2025, 
2.05.2025, 3.05.2025, 4.05.2025 (1 mai 2025 cade joia).


### Problema 20

Se citește de la tastatură un număr natural n, apoi, pentru n studenți, 
pe câte o linie, separate prin câte o virgulă și un spațiu, numele și 
patru valori naturale, reprezentând notele pentru patru examene. 
Pentru fiecare student să se afișeze în consolă numele, 
numarul de restante si media examenelor promovate, 
mai întâi pentru studenții integraliști (cu toate notele mai mari sau egale cu 5) 
în ordinea descrescătoare a mediilor, iar pentru ceilalți în ordinea crescătoare 
a numărului de restanțe; pentru cei cu același numar de restanțe, 
afisarea se va face după media examenelor promovate 
(vezi exemplul – numarul de zecimale pentru medie nu este important).

Exemplu:
INPUT
5
Ionescu Marian, 5, 4, 7, 10
Popescu Elena, 4, 3, 7, 5
Pop Dana, 4, 4, 5, 6
Florea Laura, 10, 9, 7, 8
Neagu Andrei, 9, 10, 9, 10
 
OUTPUT
Neagu Andrei, 0 restante, media 9.50
Florea Laura, 0 restante, media 8.50
Ionescu Marian, 1 restante, media 7.33
Popescu Elena, 2 restante, media 6
Pop Dana, 2 restante, media 5.5


### Problema 21

Din fișierul text_literar.txt se citește un text pe mai multe linii (un număr par). 
Să se afișeze un mesaj corespunzător: “Poezie” / “Proza”. 
Pentru ca textul să fie poezie trebuie ca între liniile din fișier să 
existe una dintre rimele:
-       împerecheată (rimează versurile 1-2, 3-4, 5-6, etc.);
-       încrucișată (rimează versurile 1-3, 2-4, 5-7, etc.);
-       îmbățișată (rimează versurile 1-4, 2-3, 5-8, 6-7, etc);
-       monorimă (rimează versurile 1-2-3-4, 5-6-7-8, etc).

Consideram ca doua versuri rimeaza daca au ultimele 3 caractere identice.


### Problema 22

Din fisierul angajati.in se citesc, de pe cate o linie a fisierului, numele 
si prenumele cate unui angajat. Se citeste de la tastatura un numar natural k, 
mai mic decat numarul liniilor din fisierul angajati.in. 
Să se afiseze in fisierul extragere.out k nume diferite de angajati, 
la intamplare, din cele existente in fisierul angajate.in.

```
Exemplu:
Daca fisierul angajati.in contine
 
Jercan Elena
Ion Horia
Marin Ioana-Daniela
Neagoe Marina
Florescu Teodora
Popa Diana
Radu Tatiana
 
si k = 4, atunci fisierul extragere.out poate contine
Neagoe Marina
Popa Diana
Radu Tatiana
Ion Horia
```
Indicație:
```python
import random
print(random.sample(range(1,6),5))
```

### Problema 23

Se da un text literar in limba romana, fara diacritice, 
care respecta toate regulile ortografice ale limbii romane 
(fara spatii nepotrivite, semne de punctuatie gresite, etc). 
Să se afișeze in consola, pe o singura linie, separate prin virgule, 
cuvintele din text ce contin trei consoane alaturate. Se va folosi modulul re, 
utilizând un tipar pentru cuvintele ce indeplinesc condiția ceruta.
Exemplu:
```
Input:
s = "Dintr-un nimic s-a transformat intr-o situatie intr-adevar grava."
Output:
Dintr-un, transformat, intr-o, intr-adevar
```

