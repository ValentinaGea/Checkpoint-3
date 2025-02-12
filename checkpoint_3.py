# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
nombre_alumno = 'Javier Martinez'
edad = 20
asignaturas = ['Álgebra', 'JavaScript', 'Python']
primer_curso = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
primeras_letras = asignaturas[0][:3]
#print(primeras_letras)

# Exercise 3: Use an index to grab the first element from your list.
primera_asignatura = asignaturas[0]
#print(primera_asignatura)

# Exercise 4: Create a new number variable that adds 10 to your original number.
nueva_edad = edad + 10
#print(nueva_edad)

# Exercise 5: Use an index to get the last element in your list.
ultima_asignatura = asignaturas[-1]
#print(ultima_asignatura)

# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
#print(names_list)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
nuevo_nombre = nombre_alumno[ :4].upper() + nombre_alumno[4: ]
#print(nuevo_nombre)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
sentence = f'Tu edad es {edad} años.'
#print(sentence)

# Exercise 9: Print “hello world”.
print('Hello world')

""" Ejercicio:
una cadena que contenga la palabra "Hola".
Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena.
Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós"."""
sentence = 'Hola, mi nombre es Valentina'
buscar_palabra = sentence.index('Hola')
palabra_encontrada = sentence[buscar_palabra:buscar_palabra + 4]
print(palabra_encontrada)
sentence = sentence.replace('Hola', 'Adios')
print(sentence)

