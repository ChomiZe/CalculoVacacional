
"Elaboar sistema vacacional teniendo en cuenta los siguientes puntos:"

"Existen 3 departamentos DTO atencion al cliente(Clave 1)"
"1 año de servicio 6 dias, 2 a 6 años 14 dias, apartir de 7 años 20 dias"

"DTO de Logistica (Clave 2)"
"1 año de servicio 7 dias, 2 a 6 años 15 dias, apartir de 7 años 22 dias"

"Gerencia (Clave 3)"
"1 año de servicio 10 dias, 2 a 6 años 20 dias, apartir de 7 años 30 dias"

"Requerimientos indispensables"
"El sistema debe solicitar *Nombre*, *Clave del departamento* y *Antiguedad del trabajador*"
"Posteriormente el programa debe mostrar el mensaje que contenga el nombre y los dias a los que tiene derecho"

print("****************************************")
print(" *** Sistema de control vacacional *** ")
print("****************************************")

nombre_empleado = input("Por favor ingrese el nombre del empleado: ")
clave_departamento = int(input("Por favor introduce la clave del departamento: "))
antiguedad_empleado = float(input("Por favor introduce los años laborados del empleado: "))

if clave_departamento == 1:
    if antiguedad_empleado == 1 and antiguedad_empleado <2:
        print("El empleado", nombre_empleado,"Tiene derecho a 6 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <=6:
        print("El empleado", nombre_empleado,"Tiene derecho a 14 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado,"Tiene derecho a 20 dias de vacaciones.")
    else:
        print("El empleado", nombre_empleado,"Aun no tiene derecho a vacaciones.")

elif clave_departamento == 2:
    if antiguedad_empleado == 1 and antiguedad_empleado <2:
        print("El empleado", nombre_empleado,"Tiene derecho a 7 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <=6:
        print("El empleado", nombre_empleado,"Tiene derecho a 15 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado,"Tiene derecho a 22 dias de vacaciones.")
    else:
        print("El empleado", nombre_empleado,"Aun no tiene derecho a vacaciones.")

elif clave_departamento ==3:
    if antiguedad_empleado == 1 and antiguedad_empleado <2:
        print("El empleado", nombre_empleado,"Tiene derecho a 10 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <=6:
        print("El empleado", nombre_empleado,"Tiene derecho a 20 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado,"Tiene derecho a 30 dias de vacaciones.")
    else:
        print("El empleado", nombre_empleado,"Aun no tiene derecho a vacaciones.")

else:
    print("La clave de deprtamento no existe, vuelve a intentarlo.")