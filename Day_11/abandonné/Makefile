

jour_11 : jour_11.o structures.o
	gcc -o jour_11 jour_11.o structures.o

jour_11_input : jour_11_input.o structures.o
	gcc -o jour_11_input jour_11_input.o structures.o

jour_11_input : jour_11_input.c structures.h
	gcc -c jour_11_input.c

jour_11.o : jour_11.c structures.h
	gcc -c jour_11.c

structures.o : structures.c structures.h
	gcc -c structures.c