def main():
	s= int(input())
	estrelas = input()
	estrela = estrelas.split()
	tm = len(estrela) - 1
	rb = -1
	i = 0
	while True:
		quantidade_estrela_i = estrela[i]
		if(i > rb):
			rb = rb + 1

		if(int(estrela[i]) > 0):
			estrela[i] = int(estrela[i]) - 1

		if(int(quantidade_estrela_i) % 2 == 0):
			if(i-1 >= 0):
				i = i - 1
			else:
				break
		else:
			if(i+1 <= tm):
				i = i + 1
			else:
				break

	restante = 0
	for i in range(s):
		restante = restante + int(estrela[i])

	print("%d %d" % (rb+1,restante))
if __name__ == '__main__':
	main()