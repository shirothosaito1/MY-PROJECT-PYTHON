# Conversion rates
usd_usd = 1
usd_eur = 0.9707
usd_aud = 1.6048
usd_bdt = 121.7438
usd_cad = 1.4432
usd_inr = 86.5698
usd_gbp = 0.8164

eur_usd = 1.0355
eur_eur = 1
eur_aud = 1.6617
eur_bdt = 126.0648
eur_cad = 1.4944
eur_inr = 89.6423
eur_gbp = 0.8454

aud_usd = 0.6234
aud_eur = 0.6018
aud_aud = 1
aud_bdt = 75.8754
aud_cad = 0.8998
aud_inr = 53.9258
aud_gbp = 0.5087

bdt_usd = 0.0082
bdt_eur = 0.0079
bdt_aud = 0.0132
bdt_bdt = 1
bdt_cad = 0.0119
bdt_inr = 0.7106
bdt_gbp = 0.0067

cad_usd = 0.6928
cad_eur = 0.6693
cad_aud = 1.1112
cad_bdt = 83.9415
cad_cad = 1
cad_inr = 59.7253
cad_gbp = 0.5652

inr_usd = 0.0116
inr_eur = 0.0112
inr_aud = 0.0185
inr_bdt = 1.4072
inr_cad = 0.0167
inr_inr = 1
inr_gbp = 0.0095

gbp_usd = 1.2249
gbp_eur = 1.1831
gbp_aud = 1.9645
gbp_bdt = 147.3564
gbp_cad = 1.7696
gbp_inr = 104.8547
gbp_gbp = 1

# Currency Calculator
print("Currency Calculator")
ask = input('Enter your currency "USD" or "EUR" or "AUD" or "BDT" or "CAD" or "INR" or "GBP": ').upper()
ask_2 = input('Enter your convert currency "USD" or "EUR" or "AUD" or "BDT" or "CAD" or "INR" or "GBP": ').upper()
how_much = float(input("Enter amount: "))

if ask == "USD" and ask_2 == "USD":
    print(how_much * usd_usd)
elif ask == "USD" and ask_2 == "EUR":
    print(how_much * usd_eur)
elif ask == "USD" and ask_2 == "AUD":
    print(how_much * usd_aud)
elif ask == "USD" and ask_2 == "BDT":
    print(how_much * usd_bdt)
elif ask == "USD" and ask_2 == "CAD":
    print(how_much * usd_cad)
elif ask == "USD" and ask_2 == "INR":
    print(how_much * usd_inr)
elif ask == "USD" and ask_2 == "GBP":
    print(how_much * usd_gbp)

elif ask == "EUR" and ask_2 == "USD":
    print(how_much * eur_usd)
elif ask == "EUR" and ask_2 == "EUR":
    print(how_much * eur_eur)
elif ask == "EUR" and ask_2 == "AUD":
    print(how_much * eur_aud)
elif ask == "EUR" and ask_2 == "BDT":
    print(how_much * eur_bdt)
elif ask == "EUR" and ask_2 == "CAD":
    print(how_much * eur_cad)
elif ask == "EUR" and ask_2 == "INR":
    print(how_much * eur_inr)
elif ask == "EUR" and ask_2 == "GBP":
    print(how_much * eur_gbp)

elif ask == "AUD" and ask_2 == "USD":
    print(how_much * aud_usd)
elif ask == "AUD" and ask_2 == "EUR":
    print(how_much * aud_eur)
elif ask == "AUD" and ask_2 == "AUD":
    print(how_much * aud_aud)
elif ask == "AUD" and ask_2 == "BDT":
    print(how_much * aud_bdt)
elif ask == "AUD" and ask_2 == "CAD":
    print(how_much * aud_cad)
elif ask == "AUD" and ask_2 == "INR":
    print(how_much * aud_inr)
elif ask == "AUD" and ask_2 == "GBP":
    print(how_much * aud_gbp)

elif ask == "BDT" and ask_2 == "USD":
    print(how_much * bdt_usd)
elif ask == "BDT" and ask_2 == "EUR":
    print(how_much * bdt_eur)
elif ask == "BDT" and ask_2 == "AUD":
    print(how_much * bdt_aud)
elif ask == "BDT" and ask_2 == "BDT":
    print(how_much * bdt_bdt)
elif ask == "BDT" and ask_2 == "CAD":
    print(how_much * bdt_cad)
elif ask == "BDT" and ask_2 == "INR":
    print(how_much * bdt_inr)
elif ask == "BDT" and ask_2 == "GBP":
    print(how_much * bdt_gbp)

elif ask == "CAD" and ask_2 == "USD":
    print(how_much * cad_usd)
elif ask == "CAD" and ask_2 == "EUR":
    print(how_much * cad_eur)
elif ask == "CAD" and ask_2 == "AUD":
    print(how_much * cad_aud)
elif ask == "CAD" and ask_2 == "BDT":
    print(how_much * cad_bdt)
elif ask == "CAD" and ask_2 == "CAD":
    print(how_much * cad_cad)
elif ask == "CAD" and ask_2 == "INR":
    print(how_much * cad_inr)
elif ask == "CAD" and ask_2 == "GBP":
    print(how_much * cad_gbp)

elif ask == "INR" and ask_2 == "USD":
    print(how_much * inr_usd)
elif ask == "INR" and ask_2 == "EUR":
    print(how_much * inr_eur)
elif ask == "INR" and ask_2 == "AUD":
    print(how_much * inr_aud)
elif ask == "INR" and ask_2 == "BDT":
    print(how_much * inr_bdt)
elif ask == "INR" and ask_2 == "CAD":
    print(how_much * inr_cad)
elif ask == "INR" and ask_2 == "INR":
    print(how_much * inr_inr)
elif ask == "INR" and ask_2 == "GBP":
    print(how_much * inr_gbp)

elif ask == "GBP" and ask_2 == "USD":
    print(how_much * gbp_usd)
elif ask == "GBP" and ask_2 == "EUR":
    print(how_much * gbp_eur)
elif ask == "GBP" and ask_2 == "AUD":
    print(how_much * gbp_aud)
elif ask == "GBP" and ask_2 == "BDT":
    print(how_much * gbp_bdt)
elif ask == "GBP" and ask_2 == "CAD":
    print(how_much * gbp_cad)
elif ask == "GBP" and ask_2 == "INR":
    print(how_much * gbp_inr)
elif ask == "GBP" and ask_2 == "GBP":
    print(how_much * gbp_gbp)

else:
    print("Invalid input or currency code!")