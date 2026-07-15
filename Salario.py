#Salarios Juan Diego Almanza Veloz

salario_bruto = float(input("Ingresa tu salario bruto: "))
p_impuestos = float(input("Ingrese el porcentaje de impuestos: "))
deducciones = float(input("Ingrese el monto de deducciones: "))
impuestos = salario_bruto * (p_impuestos / 100)
salario_neto = salario_bruto - impuestos - deducciones

print("Su salario neto es de $",salario_neto)