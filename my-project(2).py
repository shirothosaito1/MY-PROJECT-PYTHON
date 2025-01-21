print ("Mass Calculator")

# Conversion rates for weight

# gm to all weight
gm_gm = 1 
gm_kg = 0.001
gm_t = 0.000001
gm_mt = 0.000000001
gm_gt = 0.000000000001
gm_mg = 1000
gm_μg = 1000000
gm_ng = 1000000000
gm_pg = 1000000000000
gm_uston = 0.00000110231
gm_ukton = 0.000000984207
gm_lb = 0.00220462
gm_oz = 0.035274

# kg to all weight
kg_gm = 1000
kg_kg = 1
kg_t = 0.001
kg_mt = 0.000001
kg_gt = 0.000000001
kg_mg = 1000000
kg_μg = 1000000000
kg_ng = 1000000000000
kg_pg = 1000000000000000
kg_uston = 0.00110231
kg_ukton = 0.000984207
kg_lb = 2.20462
kg_oz = 35.274

# t to all weight
t_gm = 1000000
t_kg = 1000
t_t = 1
t_mt = 0.001
t_gt = 0.000001
t_mg = 1000000000
t_μg = 1000000000000
t_ng = 1000000000000000
t_pg = 1000000000000000000
t_uston = 1.10231
t_ukton = 0.984207
t_lb = 2204.62
t_oz = 35274

# mt (megaton) to all weight
mt_gm = 1000000000000
mt_kg = 1000000000
mt_t = 1000000
mt_mt = 1
mt_gt = 0.001
mt_mg = 1000000000000000
mt_μg = 1000000000000000000
mt_ng = 1000000000000000000000
mt_pg = 1000000000000000000000000
mt_uston = 1102310
mt_ukton = 984207
mt_lb = 2204620000
mt_oz = 35274000000

# gt (gigaton) to all weight
gt_gm = 1000000000000000
gt_kg = 1000000000000
gt_t = 1000000000
gt_mt = 1000
gt_gt = 1
gt_mg = 1000000000000000000
gt_μg = 1000000000000000000000
gt_ng = 1000000000000000000000000
gt_pg = 1000000000000000000000000000
gt_uston = 1102310000
gt_ukton = 984207000
gt_lb = 2204620000000
gt_oz = 35274000000000

# mg to all weight
mg_gm = 0.001
mg_kg = 0.000001
mg_t = 0.000000001
mg_mt = 0.000000000001
mg_gt = 0.000000000000001
mg_mg = 1
mg_μg = 1000
mg_ng = 1000000
mg_pg = 1000000000
mg_uston = 0.00000000110231
mg_ukton = 0.000000000984207
mg_lb = 0.00000220462
mg_oz = 0.000035274

# μg (microgram) to all weight
μg_gm = 0.000001
μg_kg = 0.000000001
μg_t = 0.000000000001
μg_mt = 0.000000000000001
μg_gt = 0.000000000000000001
μg_mg = 0.001
μg_μg = 1
μg_ng = 1000
μg_pg = 1000000
μg_uston = 0.00000000000110231
μg_ukton = 0.000000000000984207
μg_lb = 0.00000000220462
μg_oz = 0.000000035274

# ng (nanogram) to all weight
ng_gm = 0.000000001
ng_kg = 0.000000000001
ng_t = 0.000000000000001
ng_mt = 0.000000000000000001
ng_gt = 0.000000000000000000001
ng_mg = 0.000001
ng_μg = 0.001
ng_ng = 1
ng_pg = 1000
ng_uston = 0.00000000000000110231
ng_ukton = 0.000000000000000984207
ng_lb = 0.00000000000220462
ng_oz = 0.000000000035274

# pg (picogram) to all weight
pg_gm = 0.000000000001
pg_kg = 0.000000000000001
pg_t = 0.000000000000000001
pg_mt = 0.000000000000000000001
pg_gt = 0.000000000000000000000001
pg_mg = 0.000000001
pg_μg = 0.000001
pg_ng = 0.001
pg_pg = 1
pg_uston = 0.00000000000000000110231
pg_ukton = 0.000000000000000000984207
pg_lb = 0.00000000000000220462
pg_oz = 0.000000000000035274

# uston (US ton) to all weight
uston_gm = 907184.74
uston_kg = 907.18474
uston_t = 0.90718474
uston_mt = 0.00090718474
uston_gt = 0.00000090718474
uston_mg = 907184740
uston_μg = 907184740000
uston_ng = 907184740000000
uston_pg = 907184740000000000
uston_uston = 1
uston_ukton = 0.892857
uston_lb = 2000
uston_oz = 32000

# ukton (UK ton) to all weight
ukton_gm = 1016046.91
ukton_kg = 1016.04691
ukton_t = 1.01604691
ukton_mt = 0.00101604691
ukton_gt = 0.00000101604691
ukton_mg = 1016046910
ukton_μg = 1016046910000
ukton_ng = 1016046910000000
ukton_pg = 1016046910000000000
ukton_uston = 1.12
ukton_ukton = 1
ukton_lb = 2240
ukton_oz = 35840

# lb (pound) to all weight
lb_gm = 453.592
lb_kg = 0.453592
lb_t = 0.000453592
lb_mt = 0.000000453592
lb_gt = 0.000000000453592
lb_mg = 453592
lb_μg = 453592000
lb_ng = 453592000000
lb_pg = 453592000000000
lb_uston = 0.0005
lb_ukton = 0.000446429
lb_lb = 1
lb_oz = 16

# oz (ounce) to all weight
oz_gm = 28.3495
oz_kg = 0.0283495
oz_t = 0.0000283495
oz_mt = 0.0000000283495
oz_gt = 0.0000000000283495
oz_mg = 28349.5
oz_μg = 28349500
oz_ng = 28349500000
oz_pg = 28349500000000
oz_uston = 0.00003125
oz_ukton = 0.0000279018
oz_lb = 0.0625
oz_oz = 1


#ask for weight
ask = input ('Select base weight \n"GIGATONNE"\n"MEGATONNE"\n"TONNE"\n"KILOGRAM"\n"GRAM"\n"MILLIGRAM"\n"MICROGRAM"\n"NANOGRAM"\n"PICOGRAM",\n"US TONNE"\n"UK TONNE"\n"POUND"\n"OUNCE" ').upper()


ask_convert = input ('Select currency that you want to convert weight \n"GIGATONNE"\n"MEGATONNE"\n"TONNE"\n"KILOGRAM"\n"GRAM"\n"MILLIGRAM"\n"MICROGRAM"\n"NANOGRAM"\n"PICOGRAM",\n"US TONNE"\n"UK TONNE"\n"POUND"\n"OUNCE" ').upper()


amount = float(input("Enter your base weight amount "))
if ask == "GRAM" and ask_convert == "GRAM":
    print(amount * gm_gm)
elif ask == "GRAM" and ask_convert == "KILOGRAM":
    print(amount * gm_kg)
elif ask == "GRAM" and ask_convert == "TONNE":
    print(amount * gm_t)
elif ask == "GRAM" and ask_convert == "MEGATONNE":
    print(amount * gm_mt)
elif ask == "GRAM" and ask_convert == "GIGATONNE":
    print(amount * gm_gt)
elif ask == "GRAM" and ask_convert == "MILLIGRAM":
    print(amount * gm_mg)
elif ask == "GRAM" and ask_convert == "MICROGRAM":
    print(amount * gm_μg)
elif ask == "GRAM" and ask_convert == "NANOGRAM":
    print(amount * gm_ng)
elif ask == "GRAM" and ask_convert == "PICOGRAM":
    print(amount * gm_pg)
elif ask == "GRAM" and ask_convert == "US TONNE":
    print(amount * gm_uston)
elif ask == "GRAM" and ask_convert == "UK TONNE":
    print(amount * gm_ukton)
elif ask == "GRAM" and ask_convert == "POUND":
    print(amount * gm_lb)
elif ask == "GRAM" and ask_convert == "OUNCE":
    print(amount * gm_oz)
elif ask == "KILOGRAM" and ask_convert == "GRAM":
    print(amount * kg_gm)
elif ask == "KILOGRAM" and ask_convert == "KILOGRAM":
    print(amount * kg_kg)
elif ask == "KILOGRAM" and ask_convert == "TONNE":
    print(amount * kg_t)
elif ask == "KILOGRAM" and ask_convert == "MEGATONNE":
    print(amount * kg_mt)
elif ask == "KILOGRAM" and ask_convert == "GIGATONNE":
    print(amount * kg_gt)
elif ask == "KILOGRAM" and ask_convert == "MILLIGRAM":
    print(amount * kg_mg)
elif ask == "KILOGRAM" and ask_convert == "MICROGRAM":
    print(amount * kg_μg)
elif ask == "KILOGRAM" and ask_convert == "NANOGRAM":
    print(amount * kg_ng)
elif ask == "KILOGRAM" and ask_convert == "PICOGRAM":
    print(amount * kg_pg)
elif ask == "KILOGRAM" and ask_convert == "US TONNE":
    print(amount * kg_uston)
elif ask == "KILOGRAM" and ask_convert == "UK TONNE":
    print(amount * kg_ukton)
elif ask == "KILOGRAM" and ask_convert == "POUND":
    print(amount * kg_lb)
elif ask == "KILOGRAM" and ask_convert == "OUNCE":
    print(amount * kg_oz)
elif ask == "TONNE" and ask_convert == "GRAM":
    print(amount * t_gm)
elif ask == "TONNE" and ask_convert == "KILOGRAM":
    print(amount * t_kg)
elif ask == "TONNE" and ask_convert == "TONNE":
    print(amount * t_t)
elif ask == "TONNE" and ask_convert == "MEGATONNE":
    print(amount * t_mt)
elif ask == "TONNE" and ask_convert == "GIGATONNE":
    print(amount * t_gt)
elif ask == "TONNE" and ask_convert == "MILLIGRAM":
    print(amount * t_mg)
elif ask == "TONNE" and ask_convert == "MICROGRAM":
    print(amount * t_μg)
elif ask == "TONNE" and ask_convert == "NANOGRAM":
    print(amount * t_ng)
elif ask == "TONNE" and ask_convert == "PICOGRAM":
    print(amount * t_pg)
elif ask == "TONNE" and ask_convert == "US TONNE":
    print(amount * t_uston)
elif ask == "TONNE" and ask_convert == "UK TONNE":
    print(amount * t_ukton)
elif ask == "TONNE" and ask_convert == "POUND":
    print(amount * t_lb)
elif ask == "TONNE" and ask_convert == "OUNCE":
    print(amount * t_oz)
elif ask == "MEGATONNE" and ask_convert == "GRAM":
    print(amount * mt_gm)
elif ask == "MEGATONNE" and ask_convert == "KILOGRAM":
    print(amount * mt_kg)
elif ask == "MEGATONNE" and ask_convert == "TONNE":
    print(amount * mt_t)
elif ask == "MEGATONNE" and ask_convert == "MEGATONNE":
    print(amount * mt_mt)
elif ask == "MEGATONNE" and ask_convert == "GIGATONNE":
    print(amount * mt_gt)
elif ask == "MEGATONNE" and ask_convert == "MILLIGRAM":
    print(amount * mt_mg)
elif ask == "MEGATONNE" and ask_convert == "MICROGRAM":
    print(amount * mt_μg)
elif ask == "MEGATONNE" and ask_convert == "NANOGRAM":
    print(amount * mt_ng)
elif ask == "MEGATONNE" and ask_convert == "PICOGRAM":
    print(amount * mt_pg)
elif ask == "MEGATONNE" and ask_convert == "US TONNE":
    print(amount * mt_uston)
elif ask == "MEGATONNE" and ask_convert == "UK TONNE":
    print(amount * mt_ukton)
elif ask == "MEGATONNE" and ask_convert == "POUND":
    print(amount * mt_lb)
elif ask == "MEGATONNE" and ask_convert == "OUNCE":
    print(amount * mt_oz)
elif ask == "GIGATONNE" and ask_convert == "GRAM":
    print(amount * gt_gm)
elif ask == "GIGATONNE" and ask_convert == "KILOGRAM":
    print(amount * gt_kg)
elif ask == "GIGATONNE" and ask_convert == "TONNE":
    print(amount * gt_t)
elif ask == "GIGATONNE" and ask_convert == "MEGATONNE":
    print(amount * gt_mt)
elif ask == "GIGATONNE" and ask_convert == "GIGATONNE":
    print(amount * gt_gt)
elif ask == "GIGATONNE" and ask_convert == "MILLIGRAM":
    print(amount * gt_mg)
elif ask == "GIGATONNE" and ask_convert == "MICROGRAM":
    print(amount * gt_μg)
elif ask == "GIGATONNE" and ask_convert == "NANOGRAM":
    print(amount * gt_ng)
elif ask == "GIGATONNE" and ask_convert == "PICOGRAM":
    print(amount * gt_pg)
elif ask == "GIGATONNE" and ask_convert == "US TONNE":
    print(amount * gt_uston)
elif ask == "GIGATONNE" and ask_convert == "UK TONNE":
    print(amount * gt_ukton)
elif ask == "GIGATONNE" and ask_convert == "POUND":
    print(amount * gt_lb)
elif ask == "GIGATONNE" and ask_convert == "OUNCE":
    print(amount * gt_oz)
elif ask == "MILLIGRAM" and ask_convert == "GRAM":
    print(amount * mg_gm)
elif ask == "MILLIGRAM" and ask_convert == "KILOGRAM":
    print(amount * mg_kg)
elif ask == "MILLIGRAM" and ask_convert == "TONNE":
    print(amount * mg_t)
elif ask == "MILLIGRAM" and ask_convert == "MEGATONNE":
    print(amount * mg_mt)
elif ask == "MILLIGRAM" and ask_convert == "GIGATONNE":
    print(amount * mg_gt)
elif ask == "MILLIGRAM" and ask_convert == "MILLIGRAM":
    print(amount * mg_mg)
elif ask == "MILLIGRAM" and ask_convert == "MICROGRAM":
    print(amount * mg_μg)
elif ask == "MILLIGRAM" and ask_convert == "NANOGRAM":
    print(amount * mg_ng)
elif ask == "MILLIGRAM" and ask_convert == "PICOGRAM":
    print(amount * mg_pg)
elif ask == "MILLIGRAM" and ask_convert == "US TONNE":
    print(amount * mg_uston)
elif ask == "MILLIGRAM" and ask_convert == "UK TONNE":
    print(amount * mg_ukton)
elif ask == "MILLIGRAM" and ask_convert == "POUND":
    print(amount * mg_lb)
elif ask == "MILLIGRAM" and ask_convert == "OUNCE":
    print(amount * mg_oz)
elif ask == "NANOGRAM" and ask_convert == "GRAM":
    print(amount * ng_gm)
elif ask == "NANOGRAM" and ask_convert == "KILOGRAM":
    print(amount * ng_kg)
elif ask == "NANOGRAM" and ask_convert == "TONNE":
    print(amount * ng_t)
elif ask == "NANOGRAM" and ask_convert == "MEGATONNE":
    print(amount * ng_mt)
elif ask == "NANOGRAM" and ask_convert == "GIGATONNE":
    print(amount * ng_gt)
elif ask == "NANOGRAM" and ask_convert == "MILLIGRAM":
    print(amount * ng_mg)
elif ask == "NANOGRAM" and ask_convert == "MICROGRAM":
    print(amount * ng_μg)
elif ask == "NANOGRAM" and ask_convert == "NANOGRAM":
    print(amount * ng_ng)
elif ask == "NANOGRAM" and ask_convert == "PICOGRAM":
    print(amount * ng_pg)
elif ask == "NANOGRAM" and ask_convert == "US TONNE":
    print(amount * ng_uston)
elif ask == "NANOGRAM" and ask_convert == "UK TONNE":
    print(amount * ng_ukton)
elif ask == "NANOGRAM" and ask_convert == "POUND":
    print(amount * ng_lb)
elif ask == "NANOGRAM" and ask_convert == "OUNCE":
    print(amount * ng_oz)

elif ask == "PICOGRAM" and ask_convert == "GRAM":
    print(amount * pg_gm)
elif ask == "PICOGRAM" and ask_convert == "KILOGRAM":
    print(amount * pg_kg)
elif ask == "PICOGRAM" and ask_convert == "TONNE":
    print(amount * pg_t)
elif ask == "PICOGRAM" and ask_convert == "MEGATONNE":
    print(amount * pg_mt)
elif ask == "PICOGRAM" and ask_convert == "GIGATONNE":
    print(amount * pg_gt)
elif ask == "PICOGRAM" and ask_convert == "MILLIGRAM":
    print(amount * pg_mg)
elif ask == "PICOGRAM" and ask_convert == "MICROGRAM":
    print(amount * pg_μg)
elif ask == "PICOGRAM" and ask_convert == "NANOGRAM":
    print(amount * pg_ng)
elif ask == "PICOGRAM" and ask_convert == "PICOGRAM":
    print(amount * pg_pg)
elif ask == "PICOGRAM" and ask_convert == "US TONNE":
    print(amount * pg_uston)
elif ask == "PICOGRAM" and ask_convert == "UK TONNE":
    print(amount * pg_ukton)
elif ask == "PICOGRAM" and ask_convert == "POUND":
    print(amount * pg_lb)
elif ask == "PICOGRAM" and ask_convert == "OUNCE":
    print(amount * pg_oz)

elif ask == "US TONNE" and ask_convert == "GRAM":
    print(amount * uston_gm)
elif ask == "US TONNE" and ask_convert == "KILOGRAM":
    print(amount * uston_kg)
elif ask == "US TONNE" and ask_convert == "TONNE":
    print(amount * uston_t)
elif ask == "US TONNE" and ask_convert == "MEGATONNE":
    print(amount * uston_mt)
elif ask == "US TONNE" and ask_convert == "GIGATONNE":
    print(amount * uston_gt)
elif ask == "US TONNE" and ask_convert == "MILLIGRAM":
    print(amount * uston_mg)
elif ask == "US TONNE" and ask_convert == "MICROGRAM":
    print(amount * uston_μg)
elif ask == "US TONNE" and ask_convert == "NANOGRAM":
    print(amount * uston_ng)
elif ask == "US TONNE" and ask_convert == "PICOGRAM":
    print(amount * uston_pg)
elif ask == "US TONNE" and ask_convert == "US TONNE":
    print(amount * uston_uston)
elif ask == "US TONNE" and ask_convert == "UK TONNE":
    print(amount * uston_ukton)
elif ask == "US TONNE" and ask_convert == "POUND":
    print(amount * uston_lb)
elif ask == "US TONNE" and ask_convert == "OUNCE":
    print(amount * uston_oz)

elif ask == "UK TONNE" and ask_convert == "GRAM":
    print(amount * ukton_gm)
elif ask == "UK TONNE" and ask_convert == "KILOGRAM":
    print(amount * ukton_kg)
elif ask == "UK TONNE" and ask_convert == "TONNE":
    print(amount * ukton_t)
elif ask == "UK TONNE" and ask_convert == "MEGATONNE":
    print(amount * ukton_mt)
elif ask == "UK TONNE" and ask_convert == "GIGATONNE":
    print(amount * ukton_gt)
elif ask == "UK TONNE" and ask_convert == "MILLIGRAM":
    print(amount * ukton_mg)
elif ask == "UK TONNE" and ask_convert == "MICROGRAM":
    print(amount * ukton_μg)
elif ask == "UK TONNE" and ask_convert == "NANOGRAM":
    print(amount * ukton_ng)
elif ask == "UK TONNE" and ask_convert == "PICOGRAM":
    print(amount * ukton_pg)
elif ask == "UK TONNE" and ask_convert == "US TONNE":
    print(amount * ukton_uston)
elif ask == "UK TONNE" and ask_convert == "UK TONNE":
    print(amount * ukton_ukton)
elif ask == "UK TONNE" and ask_convert == "POUND":
    print(amount * ukton_lb)
elif ask == "UK TONNE" and ask_convert == "OUNCE":
    print(amount * ukton_oz)

elif ask == "POUND" and ask_convert == "GRAM":
    print(amount * lb_gm)
elif ask == "POUND" and ask_convert == "KILOGRAM":
    print(amount * lb_kg)
elif ask == "POUND" and ask_convert == "TONNE":
    print(amount * lb_t)
elif ask == "POUND" and ask_convert == "MEGATONNE":
    print(amount * lb_mt)
elif ask == "POUND" and ask_convert == "GIGATONNE":
    print(amount * lb_gt)
elif ask == "POUND" and ask_convert == "MILLIGRAM":
    print(amount * lb_mg)
elif ask == "POUND" and ask_convert == "MICROGRAM":
    print(amount * lb_μg)
elif ask == "POUND" and ask_convert == "NANOGRAM":
    print(amount * lb_ng)
elif ask == "POUND" and ask_convert == "PICOGRAM":
    print(amount * lb_pg)
elif ask == "POUND" and ask_convert == "US TONNE":
    print(amount * lb_uston)
elif ask == "POUND" and ask_convert == "UK TONNE":
    print(amount * lb_ukton)
elif ask == "POUND" and ask_convert == "POUND":
    print(amount * lb_lb)
elif ask == "POUND" and ask_convert == "OUNCE":
    print(amount * lb_oz)

elif ask == "OUNCE" and ask_convert == "GRAM":
    print(amount * oz_gm)
elif ask == "OUNCE" and ask_convert == "KILOGRAM":
    print(amount * oz_kg)
elif ask == "OUNCE" and ask_convert == "TONNE":
    print(amount * oz_t)
elif ask == "OUNCE" and ask_convert == "MEGATONNE":
    print(amount * oz_mt)
elif ask == "OUNCE" and ask_convert == "GIGATONNE":
    print(amount * oz_gt)
elif ask == "OUNCE" and ask_convert == "MILLIGRAM":
    print(amount * oz_mg)
elif ask == "OUNCE" and ask_convert == "MICROGRAM":
    print(amount * oz_μg)
elif ask == "OUNCE" and ask_convert == "NANOGRAM":
    print(amount * oz_ng)
elif ask == "OUNCE" and ask_convert == "PICOGRAM":
    print(amount * oz_pg)
elif ask == "OUNCE" and ask_convert == "US TONNE":
    print(amount * oz_uston)
elif ask == "OUNCE" and ask_convert == "UK TONNE":
    print(amount * oz_ukton)
elif ask == "OUNCE" and ask_convert == "POUND":
    print(amount * oz_lb)
elif ask == "OUNCE" and ask_convert == "OUNCE":
    print(amount * oz_oz)
else:
    print ("something wrong")