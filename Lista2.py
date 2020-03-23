#UWAGA: ABY WYŚWIETLIĆ SORTOWANE LISTY, NALEŻY W LINIACH NR: 23,37,56, USUNĄĆ ZNAK KOMENTARZA NA POCZĄTKU, CZYLI HASHTAG (#)
import sys, random, time #importuję moduł "sys" do kończenia pracy programu, w przypadku popełnionego błędu przy wprowadzaniu danych, "random" do losowania liczb, "time" do mierzenia czasu
try:    #ponieważ liczba liczb do posortowania musi być liczbą całkowitą, robię zabezpieczenie
    n=int(input("Podaj długość ciągu liczb do posortowania (n-liczbowy ciąg): "))
    p=int(input("Podaj początek zakresu liczb, z którego mam losować liczby: "))
    q=int(input("Podaj koniec zakresu liczb, z którego mam losować liczby: "))
except:
    print("Niepoprawna wartość")
    sys.exit(0)
max_czas_babel=0  #w celu znalezienia najdłuższego czasu sortowania, tworzę do tego zmienną
max_czas_wstaw=0
suma_czas_babel=0   #potrzebuję do policzenia średniej arytmetycznej sumy pomiarów
suma_czas_wstaw=0
for k in range (1,11):  #10 losowań ciągów, czyli 10 przebiegów
    print("***********************************************")
    print("LOSOWANIE NR: %d"%k)
    print("***********************************************")
    tablica=[] #rezerwuję sobie listę na liczby
    for i in range (n):
        #ponieważ chcę sortować wyłącznie liczby całkowite, robię zabezpieczenie przed wrzuceniem niepożądanych ciągów znaków
        tablica.append(random.randint(p,q))   #losuję liczby do posortowania od 1 do 100
    print("LISTA PRZED POSORTOWANIEM: ")
    #print(tablica)

    #sortowanie bąbelkowe
    babelkowe=tablica #tworzę kopię tablicy na potrzeby sortowania bąbelkowego
    start_babel=time.time() #start pomiaru czasu
    for j in range(n):
        for i in range(n-1):
            if babelkowe[i]>babelkowe[i+1]:
                pom=babelkowe[i]
                babelkowe[i]=babelkowe[i+1]
                babelkowe[i+1]=pom
    end_babel=time.time()   #stop pomiaru czasu
    czas_babel=end_babel-start_babel    #odejmowanie czasu kończowego od początkowego, wyrażonego w sekundach
    print("LISTA PO SORTOWANIU BĄBELKOWYM: ")
    #print(babelkowe)    #wyświetl listę po sortowaniu bąbelkowym
    print("Czas: %f"%czas_babel)    #czas sortowania
    if czas_babel>max_czas_babel:
        max_czas_babel=czas_babel
    suma_czas_babel+=czas_babel

    #sortowanie przez wstawianie
    wstawianie=tablica #tworzę kopię tablicy na potrzeby sortowania przez wstawianie
    start_wstaw=time.time()
    for i in range(1,n):
        pom2=wstawianie[i]
        j=i-1
        while(j>-1) and wstawianie[j]>pom2:
            wstawianie[j+1]=wstawianie[j]
            j=j-1
        wstawianie[j+1]=pom2
    end_wstaw=time.time()
    czas_wstaw=end_wstaw-start_wstaw
    print("LISTA PO SORTOWANIU PRZEZ WSTAWIANIE: ")
    #print(wstawianie)   #wyświetl listę po sortowaniu przez wstawianie
    print("Czas: %f"%czas_wstaw)    #czas sortowania
    if czas_wstaw>max_czas_wstaw:
        max_czas_wstaw=czas_wstaw
    suma_czas_wstaw+=czas_wstaw
sredni_czas_babel=(suma_czas_babel/10)
sredni_czas_wstaw=(suma_czas_wstaw/10)
print()
print("***********************************************")
print("WYNIKI:")
print("Maksymalny czas przy sortowaniu babelkowym: %.05f"%max_czas_babel)
print("Maksymalny czas przy sortowaniu przez wstawianie: %.05f"%max_czas_wstaw)
print("Średni czas przy sortowaniu babelkowym: %.05f"%sredni_czas_babel)
print("Średni czas przy sortowaniu przez wstawianie: %.05f"%sredni_czas_wstaw)
print("UWAGA: Jeśli średni i maksymalny czas sortowania wynosi 0, spróbuj zwiększyć długość ciągu liczb")
