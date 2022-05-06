all: 1.py in1.txt
	python3 1.py < in1.txt > out.txt
	python3 1.1.py < in1.txt > out1.txt
	diff out.txt out1.txt
	

1: 1.1.py in1.txt
	python3 1.1.py < in1.txt > out1.txt

test: test.py in2.txt
	python3 test.py < in2.txt> out1.txt

