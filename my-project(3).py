print("Height Calculator")

# Meter to all
m_m = 1
m_km = 0.001
m_dm = 10
m_cm = 100
m_mm = 1000
m_μm = 1000000
m_nm = 1000000000
m_mi = 0.000621371
m_yd = 1.09361
m_ft = 3.28084
m_in = 39.3701
m_nmi = 0.000539957

# Kilometer to all
km_m = 1000
km_km = 1
km_dm = 10000
km_cm = 100000
km_mm = 1000000
km_μm = 1000000000
km_nm = 1000000000000
km_mi = 0.621371
km_yd = 1093.61
km_ft = 3280.84
km_in = 39370.1
km_nmi = 0.539957

# Decimeter to all
dm_m = 0.1
dm_km = 0.0001
dm_dm = 1
dm_cm = 10
dm_mm = 100
dm_μm = 100000
dm_nm = 100000000
dm_mi = 0.0000621371
dm_yd = 0.109361
dm_ft = 0.328084
dm_in = 3.93701
dm_nmi = 0.0000539957

# Centimeter to all
cm_m = 0.01
cm_km = 0.00001
cm_dm = 0.1
cm_cm = 1
cm_mm = 10
cm_μm = 10000
cm_nm = 10000000
cm_mi = 0.00000621371
cm_yd = 0.0109361
cm_ft = 0.0328084
cm_in = 0.393701
cm_nmi = 0.00000539957

# Millimeter to all
mm_m = 0.001
mm_km = 0.000001
mm_dm = 0.01
mm_cm = 0.1
mm_mm = 1
mm_μm = 1000
mm_nm = 1000000
mm_mi = 0.000000621371
mm_yd = 0.00109361
mm_ft = 0.00328084
mm_in = 0.0393701
mm_nmi = 0.000000539957

# Micrometer to all
μm_m = 0.000001
μm_km = 0.000000001
μm_dm = 0.00001
μm_cm = 0.0001
μm_mm = 0.001
μm_μm = 1
μm_nm = 1000
μm_mi = 0.000000000621371
μm_yd = 0.00000109361
μm_ft = 0.00000328084
μm_in = 0.0000393701
μm_nmi = 0.000000000539957

# Nanometer to all
nm_m = 0.000000001
nm_km = 0.000000000001
nm_dm = 0.00000001
nm_cm = 0.0000001
nm_mm = 0.000001
nm_μm = 0.001
nm_nm = 1
nm_mi = 0.000000000000621371
nm_yd = 0.00000000109361
nm_ft = 0.00000000328084
nm_in = 0.0000000393701
nm_nmi = 0.000000000000539957

# Mile to all
mi_m = 1609.34
mi_km = 1.60934
mi_dm = 16093.4
mi_cm = 160934
mi_mm = 1609340
mi_μm = 1609340000
mi_nm = 1609340000000
mi_mi = 1
mi_yd = 1760
mi_ft = 5280
mi_in = 63360
mi_nmi = 0.868976

# Yard to all
yd_m = 0.9144
yd_km = 0.0009144
yd_dm = 9.144
yd_cm = 91.44
yd_mm = 914.4
yd_μm = 914400
yd_nm = 914400000
yd_mi = 0.000568182
yd_yd = 1
yd_ft = 3
yd_in = 36
yd_nmi = 0.000493737

# Foot to all
ft_m = 0.3048
ft_km = 0.0003048
ft_dm = 3.048
ft_cm = 30.48
ft_mm = 304.8
ft_μm = 304800
ft_nm = 304800000
ft_mi = 0.000189394
ft_yd = 0.333333
ft_ft = 1
ft_in = 12
ft_nmi = 0.000164579

# Inch to all
in_m = 0.0254
in_km = 0.0000254
in_dm = 0.254
in_cm = 2.54
in_mm = 25.4
in_μm = 25400
in_nm = 25400000
in_mi = 0.000015783
in_yd = 0.0277778
in_ft = 0.0833333
in_in = 1
in_nmi = 0.000013715

# Nautical Mile to all
nmi_m = 1852
nmi_km = 1.852
nmi_dm = 18520
nmi_cm = 185200
nmi_mm = 1852000
nmi_μm = 1852000000
nmi_nm = 1
nmi_mi = 1.15078
nmi_yd = 2025.37
nmi_ft = 6076.12
nmi_in = 72913.5
nmi_nmi = 1


#ask for unit 

ask = input('Select your unit: "METER" or "KILOMETER" or "DECIMETER" or "CENTIMETER" or "MILLIMETER" or "MICROMETER" or "NANOMETER" or "MILE" or "YARD" or "FEET" or "INCH" or "NAUTICAL MILE" ').upper()


#ask for convert unit
ask_convert = input ('Select your unit for convert : "METER" or "KILOMETER" or "DECIMETER" or "CENTIMETER" or "MILLIMETER" or "MICROMETER" or "NANOMETER" or "MILE" or "YARD" or "FEET" or "INCH" or "NAUTICAL MILE" ').upper()


#ask for amount 

ask_amount = float(input("Enter your base unit amount: "))



if ask == "METER" and ask_convert == "METER":
    print(ask_amount * m_m)
elif ask == "METER" and ask_convert == "KILOMETER":
    print(ask_amount * m_km)
elif ask == "METER" and ask_convert == "DECIMETER":
    print(ask_amount * m_dm)
elif ask == "METER" and ask_convert == "CENTIMETER":
    print(ask_amount * m_cm)
elif ask == "METER" and ask_convert == "MILLIMETER":
    print(ask_amount * m_mm)
elif ask == "METER" and ask_convert == "MICROMETER":
    print(ask_amount * m_μm)
elif ask == "METER" and ask_convert == "NANOMETER":
    print(ask_amount * m_nm)
elif ask == "METER" and ask_convert == "MILE":
    print(ask_amount * m_mi)
elif ask == "METER" and ask_convert == "YARD":
    print(ask_amount * m_yd)
elif ask == "METER" and ask_convert == "FEET":
    print(ask_amount * m_ft)
elif ask == "METER" and ask_convert == "INCH":
    print(ask_amount * m_in)
elif ask == "METER" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * m_nmi)
elif ask == "KILOMETER" and ask_convert == "METER":
    print(ask_amount * km_m)
elif ask == "KILOMETER" and ask_convert == "KILOMETER":
    print(ask_amount * km_km)
elif ask == "KILOMETER" and ask_convert == "DECIMETER":
    print(ask_amount * km_dm)
elif ask == "KILOMETER" and ask_convert == "CENTIMETER":
    print(ask_amount * km_cm)
elif ask == "KILOMETER" and ask_convert == "MILLIMETER":
    print(ask_amount * km_mm)
elif ask == "KILOMETER" and ask_convert == "MICROMETER":
    print(ask_amount * km_μm)
elif ask == "KILOMETER" and ask_convert == "NANOMETER":
    print(ask_amount * km_nm)
elif ask == "KILOMETER" and ask_convert == "MILE":
    print(ask_amount * km_mi)
elif ask == "KILOMETER" and ask_convert == "YARD":
    print(ask_amount * km_yd)
elif ask == "KILOMETER" and ask_convert == "FEET":
    print(ask_amount * km_ft)
elif ask == "KILOMETER" and ask_convert == "INCH":
    print(ask_amount * km_in)
elif ask == "KILOMETER" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * km_nm)
elif ask == "DECIMETER" and ask_convert == "METER":
    print(ask_amount * dm_m)
elif ask == "DECIMETER" and ask_convert == "KILOMETER":
    print(ask_amount * dm_km)
elif ask == "DECIMETER" and ask_convert == "DECIMETER":
    print(ask_amount * dm_dm)
elif ask == "DECIMETER" and ask_convert == "CENTIMETER":
    print(ask_amount * dm_cm)
elif ask == "DECIMETER" and ask_convert == "MILLIMETER":
    print(ask_amount * dm_mm)
elif ask == "DECIMETER" and ask_convert == "MICROMETER":
    print(ask_amount * dm_μm)
elif ask == "DECIMETER" and ask_convert == "NANOMETER":
    print(ask_amount * dm_nm)
elif ask == "DECIMETER" and ask_convert == "MILE":
    print(ask_amount * dm_mi)
elif ask == "DECIMETER" and ask_convert == "YARD":
    print(ask_amount * dm_yd)
elif ask == "DECIMETER" and ask_convert == "FEET":
    print(ask_amount * dm_ft)
elif ask == "DECIMETER" and ask_convert == "INCH":
    print(ask_amount * dm_in)
elif ask == "DECIMETER" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * dm_nmi)
elif ask == "CENTIMETER" and ask_convert == "METER":
    print(ask_amount * cm_m)
elif ask == "CENTIMETER" and ask_convert == "KILOMETER":
    print(ask_amount * cm_km)
elif ask == "CENTIMETER" and ask_convert == "DECIMETER":
    print(ask_amount * cm_dm)
elif ask == "CENTIMETER" and ask_convert == "CENTIMETER":
    print(ask_amount * cm_cm)
elif ask == "CENTIMETER" and ask_convert == "MILLIMETER":
    print(ask_amount * cm_mm)
elif ask == "CENTIMETER" and ask_convert == "MICROMETER":
    print(ask_amount * cm_μm)
elif ask == "CENTIMETER" and ask_convert == "NANOMETER":
    print(ask_amount * cm_nm)
elif ask == "CENTIMETER" and ask_convert == "MILE":
    print(ask_amount * cm_mi)
elif ask == "CENTIMETER" and ask_convert == "YARD":
    print(ask_amount * cm_yd)
elif ask == "CENTIMETER" and ask_convert == "FEET":
    print(ask_amount * cm_ft)
elif ask == "CENTIMETER" and ask_convert == "INCH":
    print(ask_amount * cm_in)
elif ask == "CENTIMETER" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * cm_nmi)
elif ask == "MILLIMETER" and ask_convert == "METER":
    print(ask_amount * mm_m)
elif ask == "MILLIMETER" and ask_convert == "KILOMETER":
    print(ask_amount * mm_km)
elif ask == "MILLIMETER" and ask_convert == "DECIMETER":
    print(ask_amount * mm_dm)
elif ask == "MILLIMETER" and ask_convert == "CENTIMETER":
    print(ask_amount * mm_cm)
elif ask == "MILLIMETER" and ask_convert == "MILLIMETER":
    print(ask_amount * mm_mm)
elif ask == "MILLIMETER" and ask_convert == "MICROMETER":
    print(ask_amount * mm_μm)
elif ask == "MILLIMETER" and ask_convert == "NANOMETER":
    print(ask_amount * mm_nm)
elif ask == "MILLIMETER" and ask_convert == "MILE":
    print(ask_amount * mm_mi)
elif ask == "MILLIMETER" and ask_convert == "YARD":
    print(ask_amount * mm_yd)
elif ask == "MILLIMETER" and ask_convert == "FEET":
    print(ask_amount * mm_ft)
elif ask == "MILLIMETER" and ask_convert == "INCH":
    print(ask_amount * mm_in)
elif ask == "MILLIMETER" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * mm_nmi)
elif ask == "MICROMETER" and ask_convert == "METER":
    print(ask_amount * μm_m)
elif ask == "MICROMETER" and ask_convert == "KILOMETER":
    print(ask_amount * μm_km)
elif ask == "MICROMETER" and ask_convert == "DECIMETER":
    print(ask_amount * μm_dm)
elif ask == "MICROMETER" and ask_convert == "CENTIMETER":
    print(ask_amount * μm_cm)
elif ask == "MICROMETER" and ask_convert == "MILLIMETER":
    print(ask_amount * μm_mm)
elif ask == "MICROMETER" and ask_convert == "MICROMETER":
    print(ask_amount * μm_μm)
elif ask == "MICROMETER" and ask_convert == "NANOMETER":
    print(ask_amount * μm_nm)
elif ask == "MICROMETER" and ask_convert == "MILE":
    print(ask_amount * μm_mi)
elif ask == "MICROMETER" and ask_convert == "YARD":
    print(ask_amount * μm_yd)
elif ask == "MICROMETER" and ask_convert == "FEET":
    print(ask_amount * μm_ft)
elif ask == "MICROMETER" and ask_convert == "INCH":
    print(ask_amount * μm_in)
elif ask == "MICROMETER" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * μm_nmi)
elif ask == "NANOMETER" and ask_convert == "METER":
    print(ask_amount * nm_m)
elif ask == "NANOMETER" and ask_convert == "KILOMETER":
    print(ask_amount * nm_km)
elif ask == "NANOMETER" and ask_convert == "DECIMETER":
    print(ask_amount * nm_dm)
elif ask == "NANOMETER" and ask_convert == "CENTIMETER":
    print(ask_amount * nm_cm)
elif ask == "NANOMETER" and ask_convert == "MILLIMETER":
    print(ask_amount * nm_mm)
elif ask == "NANOMETER" and ask_convert == "MICROMETER":
    print(ask_amount * nm_μm)
elif ask == "NANOMETER" and ask_convert == "NANOMETER":
    print(ask_amount * nm_nm)
elif ask == "NANOMETER" and ask_convert == "MILE":
    print(ask_amount * nm_mi)
elif ask == "NANOMETER" and ask_convert == "YARD":
    print(ask_amount * nm_yd)
elif ask == "NANOMETER" and ask_convert == "FEET":
    print(ask_amount * nm_ft)
elif ask == "NANOMETER" and ask_convert == "INCH":
    print(ask_amount * nm_in)
elif ask == "NANOMETER" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * nm_nmi)
elif ask == "MILE" and ask_convert == "METER":
    print(ask_amount * mi_m)
elif ask == "MILE" and ask_convert == "KILOMETER":
    print(ask_amount * mi_km)
elif ask == "MILE" and ask_convert == "DECIMETER":
    print(ask_amount * mi_dm)
elif ask == "MILE" and ask_convert == "CENTIMETER":
    print(ask_amount * mi_cm)
elif ask == "MILE" and ask_convert == "MILLIMETER":
    print(ask_amount * mi_mm)
elif ask == "MILE" and ask_convert == "MICROMETER":
    print(ask_amount * mi_μm)
elif ask == "MILE" and ask_convert == "NANOMETER":
    print(ask_amount * mi_nm)
elif ask == "MILE" and ask_convert == "MILE":
    print(ask_amount * mi_mi)
elif ask == "MILE" and ask_convert == "YARD":
    print(ask_amount * mi_yd)
elif ask == "MILE" and ask_convert == "FEET":
    print(ask_amount * mi_ft)
elif ask == "MILE" and ask_convert == "INCH":
    print(ask_amount * mi_in)
elif ask == "MILE" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * mi_nmi)
elif ask == "YARD" and ask_convert == "METER":
    print(ask_amount * yd_m)
elif ask == "YARD" and ask_convert == "KILOMETER":
    print(ask_amount * yd_km)
elif ask == "YARD" and ask_convert == "DECIMETER":
    print(ask_amount * yd_dm)
elif ask == "YARD" and ask_convert == "CENTIMETER":
    print(ask_amount * yd_cm)
elif ask == "YARD" and ask_convert == "MILLIMETER":
    print(ask_amount * yd_mm)
elif ask == "YARD" and ask_convert == "MICROMETER":
    print(ask_amount * yd_μm)
elif ask == "YARD" and ask_convert == "NANOMETER":
    print(ask_amount * yd_nm)
elif ask == "YARD" and ask_convert == "MILE":
    print(ask_amount * yd_mi)
elif ask == "YARD" and ask_convert == "YARD":
    print(ask_amount * yd_yd)
elif ask == "YARD" and ask_convert == "FEET":
    print(ask_amount * yd_ft)
elif ask == "YARD" and ask_convert == "INCH":
    print(ask_amount * yd_in)
elif ask == "YARD" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * yd_nmi)
elif ask == "FEET" and ask_convert == "METER":
    print(ask_amount * ft_m)
elif ask == "FEET" and ask_convert == "KILOMETER":
    print(ask_amount * ft_km)
elif ask == "FEET" and ask_convert == "DECIMETER":
    print(ask_amount * ft_dm)
elif ask == "FEET" and ask_convert == "CENTIMETER":
    print(ask_amount * ft_cm)
elif ask == "FEET" and ask_convert == "MILLIMETER":
    print(ask_amount * ft_mm)
elif ask == "FEET" and ask_convert == "MICROMETER":
    print(ask_amount * ft_μm)
elif ask == "FEET" and ask_convert == "NANOMETER":
    print(ask_amount * ft_nm)
elif ask == "FEET" and ask_convert == "MILE":
    print(ask_amount * ft_mi)
elif ask == "FEET" and ask_convert == "YARD":
    print(ask_amount * ft_yd)
elif ask == "FEET" and ask_convert == "FEET":
    print(ask_amount * ft_ft)
elif ask == "FEET" and ask_convert == "INCH":
    print(ask_amount * ft_in)
elif ask == "FEET" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * ft_nmi)
elif ask == "INCH" and ask_convert == "METER":
    print(ask_amount * in_m)
elif ask == "INCH" and ask_convert == "KILOMETER":
    print(ask_amount * in_km)
elif ask == "INCH" and ask_convert == "DECIMETER":
    print(ask_amount * in_dm)
elif ask == "INCH" and ask_convert == "CENTIMETER":
    print(ask_amount * in_cm)
elif ask == "INCH" and ask_convert == "MILLIMETER":
    print(ask_amount * in_mm)
elif ask == "INCH" and ask_convert == "MICROMETER":
    print(ask_amount * in_μm)
elif ask == "INCH" and ask_convert == "NANOMETER":
    print(ask_amount * in_nm)
elif ask == "INCH" and ask_convert == "MILE":
    print(ask_amount * in_mi)
elif ask == "INCH" and ask_convert == "YARD":
    print(ask_amount * in_yd)
elif ask == "INCH" and ask_convert == "FEET":
    print(ask_amount * in_ft)
elif ask == "INCH" and ask_convert == "INCH":
    print(ask_amount * in_in)
elif ask == "INCH" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * in_nmi)
elif ask == "NAUTICAL MILE" and ask_convert == "METER":
    print(ask_amount * nmi_m)
elif ask == "NAUTICAL MILE" and ask_convert == "KILOMETER":
    print(ask_amount * nmi_km)
elif ask == "NAUTICAL MILE" and ask_convert == "DECIMETER":
    print(ask_amount * nmi_dm)
elif ask == "NAUTICAL MILE" and ask_convert == "CENTIMETER":
    print(ask_amount * nmi_cm)
elif ask == "NAUTICAL MILE" and ask_convert == "MILLIMETER":
    print(ask_amount * nmi_mm)
elif ask == "NAUTICAL MILE" and ask_convert == "MICROMETER":
    print(ask_amount * nmi_μm)
elif ask == "NAUTICAL MILE" and ask_convert == "NANOMETER":
    print(ask_amount * nmi_nm)
elif ask == "NAUTICAL MILE" and ask_convert == "MILE":
    print(ask_amount * nmi_mi)
elif ask == "NAUTICAL MILE" and ask_convert == "YARD":
    print(ask_amount * nmi_yd)
elif ask == "NAUTICAL MILE" and ask_convert == "FEET":
    print(ask_amount * nmi_ft)
elif ask == "NAUTICAL MILE" and ask_convert == "INCH":
    print(ask_amount * nmi_in)
elif ask == "NAUTICAL MILE" and ask_convert == "NAUTICAL MILE":
    print(ask_amount * nmi_nmi)
else:
    print("Invalid input. Please check your unit selections.")
