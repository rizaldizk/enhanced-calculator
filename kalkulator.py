opsi = input("Anda ingin melakukan operasi apa? +/-/*/:/pangkat/pembanding/akar/logaritma: ")

if opsi == ("pangkat"):
	print("KETERANGAN: input pertama adalah angka yang ingin dipangkatkan, sedangkan input kedua adalah pangkat")
	
if opsi == ("pembanding"):
	print("KETERANGAN: hasil akan menunjukkan angka yang lebih besar")

if opsi == ("akar"):
	print("KETERANGAN: masukan angka yang sama pada input pertama dan kedua (angka yang ingin diakarkan)")
	
if opsi == ("logaritma"):
	print("KETERANGAN: input pertama merupakan nilai a, input kedua merupakan nilai b atau b log a")

num1 = float(input("masukan angka: ")) 	
num2 = float(input("masukan angka: "))

if opsi == ("+"):
	print(num1+num2)
elif opsi == ("-"):
	print(num1-num2)
elif opsi == ("*"):
	print(num1*num2)
elif opsi == (":"):
	print(num1/num2)
elif opsi == ("pangkat"):
	float(input(pow(num1, num2)))
elif opsi == ("pembanding"):
	if (num1) == (num2):
		print("equal")
	elif (num1) >= (num2):
		print(num1)
	elif (num1) <= (num2):
		print(num2)
elif opsi == ("akar"):
	if not num2 == num1:
		print("input kedua harus sama dengan input pertama (angka yang akan diakarkan")
		exit()
	import math
	print(math.sqrt(num1))
elif opsi == ("logaritma"):
	import math
	print(math.log(num2, num1))
else:
	print("galat")