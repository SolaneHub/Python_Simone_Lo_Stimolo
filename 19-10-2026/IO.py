File_valorizzato_da_open = open("pippo.txt", "r")

# metodo di lettura totale del file
contenuto_file_totale = File_valorizzato_da_open.read()
print(contenuto_file_totale)

# metodo di lettura line by line del file
contenuto_file_riga = File_valorizzato_da_open.readline()
print(contenuto_file_riga)