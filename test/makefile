CC=g++
EXE_FILE=bank.out
clear:all
	rm *.o

all: Bank.o main.o clear
	$(CC) main.o Bank.o -o $(EXE_FILE)

Bank.o: Bank.cpp Bank.hpp
	$(CC) -c Bank.cpp -o Bank.o

main.o: main.cpp Bank.hpp
	$(CC) -c main.cpp -o main.o

 
