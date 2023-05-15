all: calculator

calculator: \
		main.c \
		operations.h \
		addition.o \
		division.o \
		multiplication.o \
		subtraction.o
	gcc -o calculator main.c addition.o division.o multiplication.o subtraction.o

addition.o: addition.c
	gcc -c addition.c
division.o: division.c
	gcc -c division.c
multiplication.o: multiplication.c
	gcc -c multiplication.c
subtraction.o: subtraction.c
	gcc -c subtraction.c

clean:
	rm -rf calculator *.o

.PHONY: all clean
