'''
Accept any city from the user and display monument of that city
City           Monument
Delhi          Red Fort
Agra           Taj Mahal
Jaipur         Jal Mahal
'''
ct = input("Enter the name of city: ")
if (ct.lower() == "delhi"):
    print("Red Fort")
elif (ct.lower() == "agra"):
    print("Taj Mahal")
elif (ct.lower() == "jaipur"):
    print("Jai Mahal")
