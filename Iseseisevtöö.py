import math
import random



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

# def eurokalkulaator():
#     valik = input("Kas soovite teisendada Eurosid[EUR] või Kroone[EEK]: ").upper()
#     kroonid = 15.6466

#     if valik == "EUR":
#         summa_eurodes = int(input("Sisestage summa eurodes: "))
#         summa_kroonides = summa_eurodes * kroonid
#         print(f"{summa_eurodes} eurot on {summa_kroonides} krooni")
#     elif valik == "EEK":
#         summa_kroonides = int(input("Sisestage summa kroonides: "))
#         summa_eurodes = summa_kroonides / kroonid
#         print(f"{summa_kroonides} krooni on {summa_eurodes} eurot")
#     else:
#         print("Vale valik!")


# eurokalkulaator()