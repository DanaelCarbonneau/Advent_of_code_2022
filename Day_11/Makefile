all: jour_10

jour_10: jour_10.o structures.o 
    gcc -o jour_10 jour_10.o structures.o 

jour_10.o: jour_10.c structures.h
    gcc -c jour_10.c

structures.o: structures.c structures.h
	gcc -c structures.c

clea: *.o jour_10