def cel_para_fahr(tem_cel):
    return(temp_cel * 9/5)+32
def fahr_para_cel(temp_fahr):
    return(temp_fahr - 32)* 5/9

temp_cel = float(input("Digite a temperatura em celsius: "))
temp_fahr = float(input("Digite a temperatura em Fahrenhei: "))

print(temp_cel, "Graus Celsius equivalem a", cel_para_fahr(temp_cel), "Graus Fahr.")
print(temp_fahr, "Graus Fahrenheit equivalem a ", fahr_para_cel(temp_fahr)," Graus Celsius")

