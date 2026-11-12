print("========================================")
print("     WELL LOG RESERVOIR SCREENING")
print("========================================")

depth = float(input("Enter depth (m): "))
porosity = float(input("Enter porosity (%): "))
saturation = float(input("Enter water saturation (%): "))
resistivity = float(input("Enter resistivity (ohm.m): "))


def check_quality(porosity, saturation, resistivity):

    if porosity < 0 or porosity > 50:
        return "Invalid porosity"

    if saturation < 0 or saturation > 100:
        return "Invalid water saturation"

    if resistivity <= 0:
        return "Invalid resistivity"

    return "Valid data"


def check_reservoir(porosity, saturation, resistivity):

    if porosity >= 20 and saturation < 40 and resistivity > 10:
        return "Potential Reservoir"
    else:
        return "Not a Potential Reservoir"


quality = check_quality(porosity, saturation, resistivity)

print()
print("------------- RESULTS -------------")
print("Depth:", depth, "m")
print("Porosity:", porosity, "%")
print("Water Saturation:", saturation, "%")
print("Resistivity:", resistivity, "ohm.m")
print("Data Quality:", quality)

if quality == "Valid data":
    result = check_reservoir(porosity, saturation, resistivity)
    print("Reservoir Status:", result)
else:
    print("Reservoir Status: Cannot be evaluated")

print("------------------------------------")
