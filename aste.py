fails=open("lapa.txt", 'w', encoding="utf-8")

linija1= "rozes ir sarkanas. \n"
linija2= "rudens ir klāt. \n"
linija3= "python ir jauks. \n"
linija4= "vai tu esi jautri .\n"

fails.write(linija1 + linija2 + linija3 + linija4)
fails.close()