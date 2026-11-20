from customtkinter import *

app1 = CTk()
app1.title('Generatore Codice Fiscale')

w_px = 350
h_px = 500

# Ottiene Dimensioni Schermo
screen_width = app1.winfo_screenwidth()
screen_height = app1.winfo_screenheight()
# Calcola Posizione X & Y per Centrare Finestra
x = int((screen_width / 2) - (w_px / 2))
y = int((screen_height / 2) - (h_px / 2))
# Imposta Geometria Finestra
app1.geometry(f"{w_px}x{h_px}+{x}+{y}")


### è costituito da x16 caratteri alfanumerici ###
# 1) Cognome 1°-3° x3 Consonanti; 1°-2°-3°, e poi Vocali

# 2) Nome 4°-6° x3 Consonanti altrimenti Vocali
# se uguale o più di 4 consonanti allora 1°-3°-4°; altrimenti 1°-2°-3°, e poi Vocali

# 3) 7°-9° x2 Anno e x1 Mese Nascita
# 4) 10°-11° x2 Giorno Nascita e Sesso (+40 Donne)
# 5) 12°-15° x4 Codice Catastale Comune Nascita
# 6) 16° x1 Carattere di Controllo


### Dichiarazione variabili globali ###
vocali = "AEIOU"

consonanti = "BCDFGHJKLMNPQRSTVWXYZ"

mesiCodLett = {
    "gennaio": "A",
    "febbraio": "B",
    "marzo": "C",
    "aprile": "D",
    "maggio": "E",
    "giugno": "H",
    "luglio": "L",
    "agosto": "M",
    "settembre": "P",
    "ottobre": "R",
    "novembre": "S",
    "dicembre": "T"
}

codCatastDiz = {
    "agira": "A070",
    "barrafranca": "A676",
    "enna": "C342",
    "palermo": "G273",
    "catania": "C351",
    "nissoria": "F900",
    "valguarnera": "L583",
    "aidone": "A098",
    "leonforte": "E536",
    "piazza Armerina": "G580",
    "villarosa": "M011",
    "assoro": "A478",
    "nicosia": "F892",
    "troina": "L448"
}

sessoList = ["M", "F"]

def calcoloCodiceFiscale():
    consCognomeScel = ""
    consNomeScel = ""
    
    cgnmGet1 = cognome.get().upper()
    nmGet1 = nome.get().upper()
    annGet1 = anno.get()
    lttMeseGet1 = mese.get().lower()
    grnGet1 = giorno.get()
    codCatastGet1 = codCatastEntry.get().lower()
    
    # Scelta Consonante Cognome
    for l_cgnm in cgnmGet1:
        if l_cgnm in consonanti:
            consCognomeScel += l_cgnm
        if len(consCognomeScel) == 3:
            break

    # Scelta Consonante Nome    
    for l_nm in nmGet1:
        if l_nm in consonanti:
            consNomeScel += l_nm
        if len(consNomeScel) == 3:
            break

    # Scelta Numero dall'Anno
    cifreAnnoScel = annGet1[-2:]
    
    # Scelta Lettera dal Mese
    lettMeseScel = mesiCodLett.get(lttMeseGet1)

    # Giorno
    iniz_Giorno = int(grnGet1)
    
    # final_giorno = str(iniz_Giorno)
    
    # Scelta Sesso
    LettSessoScel = sessoMenu.get()
    if LettSessoScel == "F":
        iniz_Giorno += 40
    elif 1 <= iniz_Giorno <= 10:
        final_giorno = "0" + str(iniz_Giorno)
    else:
        final_giorno = str(iniz_Giorno)

    # Codice Catastale
    CodCatastVal = codCatastDiz.get(codCatastGet1)

    lbl_Finale.configure(text=consCognomeScel
                         + consNomeScel 
                         + cifreAnnoScel 
                         + lettMeseScel
                         + final_giorno
                         + CodCatastVal)


### Widget per l'interfaccia ###
CTkLabel(master=app1, font=('', 26), text='Generatore Codice Fiscale').pack(pady=5)

sessoMenu = CTkOptionMenu(master=app1, values=sessoList)
sessoMenu.pack(pady=10)

cognome = CTkEntry(master=app1, placeholder_text='Cognome')
cognome.pack(pady=10)
# cognome.insert(0, "")
nome = CTkEntry(master=app1, placeholder_text='Nome')
nome.pack(pady=10)
# nome.insert(0, "")

anno = CTkEntry(master=app1, placeholder_text='Anno')
anno.pack(pady=10)
# anno.insert(0, "")
mese = CTkEntry(master=app1, placeholder_text='Mese')
mese.pack(pady=10)
# mese.insert(0, "")
giorno = CTkEntry(master=app1, placeholder_text='Giorno')
giorno.pack(pady=10)
# giorno.insert(0, "")

codCatastEntry = CTkEntry(master=app1, placeholder_text='Comune')
codCatastEntry.pack(pady=10)
# codCatastEntry.insert(0, "")

btnCalcola = CTkButton(master=app1, command=calcoloCodiceFiscale, text='Calcola')
btnCalcola.pack(pady=10)

lbl_Finale = CTkLabel(master=app1, font=('', 30), text="")
lbl_Finale.pack(pady=10)

app1.mainloop()
