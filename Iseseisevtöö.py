#Hendri Olev Serman
#01.02.2024
#IT-23

import random

# # #Vanused

# def vanused():
#     vanused = [19, 17, 17, 16, 16, 16]
#     print("Vanuste loend:", vanused)
#     print("Suurim arv:", max(vanused))
#     print("Väikseim arv:", min(vanused))
#     print("Kogusumma:", sum(vanused))
#     print("Keskmine:", sum(vanused)/len(vanused))
    
# vanused()





# # Vähem kui viis

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# def vähem_kui_viis():
#     new_list = []
#     for i in a: new_list.append(i) if i < 5 else None
#     print(new_list)
# print()
# add = int(input("Sisesta number: "))
# a.append(add)

# vähem_kui_viis()





# # Paaris või paaritu

# def paaris_või_paaritu():
#     arv = int(input("Sisesta arv: "))
#     if arv == 0:
#         print("Sisesta mida iganes, aga mitte 0!")
#     elif arv % 2 == 0:
#         print("Arv on paaris")
#     else:
#         print("Arv on paaritu")
        
# paaris_või_paaritu()





# #Täringud

# def täringumang():
#     print("Osalete täringumängus!")
#     panus = int(input("Palun sisestage, mitu eurot soovite panustada: "))
#     print(f"Teie panus on {panus} eurot.")

#     print("Arvuti veeretab täringuid.")
#     arvuti_taringud = [random.randint(1, 6) for i in range(2)]
#     taringusumma = sum(arvuti_taringud)

#     vastus = int(input("Arvake ära mitu punkti arvuti viskas: "))

#     print(f"Arvuti viskas {arvuti_taringud[0]} ja {arvuti_taringud[1]}, kokku {taringusumma} punkti.")

#     if taringusumma == vastus:
#         võidetud_summa = panus * 2
#         print(f"Teie võitsite! Te võitsite {võidetud_summa} eurot!!!:)")
#     else:
#         print(f"Arvuti võitis, õige vastus oli {taringusumma}! Te kaotasite {panus} eurot:( ")

# täringumang()





# #Kaugushüpe

# def kaugushüpe():
#     lõpptulemused = []

#     for i in range(3):
#         tulemused = float(input(f"Sisesta kaugushüppe tulemus {i + 1}: "))
#         lõpptulemused.append(tulemused)

#     parim_tulemus = max(lõpptulemused)
#     keskmine_tulemus = sum(lõpptulemused) / len(lõpptulemused)

#     print("Parim tulemus on", parim_tulemus, "m")
#     print("Keskmine tulemus on", keskmine_tulemus, "m")

# kaugushüpe()





# #Eurokalkulaator

# def eurod_kroonideks():
#     kroonid = 15.6466
#     summa_eurodes = int(input("Sisesta summa eurodes: "))
#     summa_kroonides = summa_eurodes * kroonid
#     print(f"{summa_eurodes} eurot on {summa_kroonides} krooni")

# def kroonid_eurodeks():
#     kroonid = 15.6466
#     summa_kroonides = int(input("Sisesta summa kroonides: "))
#     summa_eurodes = summa_kroonides / kroonid
#     print(f"{summa_kroonides} krooni on {summa_eurodes} eurot")

# teisendamise_tyyp = input("Musi mario :) , kas soovid teisendada Eurosid[EUR] või Kroone[EEK]: ").upper()

# if teisendamise_tyyp == "EUR":
#     eurod_kroonideks()
# elif teisendamise_tyyp == "EEK":
#     kroonid_eurodeks()
# else:
#     print("Kas sa kirjutada ei oska? Vali üks kahest: EUR või EEK")