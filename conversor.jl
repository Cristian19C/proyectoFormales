using Dates

# Nombre de la ciudad o país para obtener su diferencia con GMT
let ubicacion1 = "America/Bogota"
end  # Cambia esto a la ubicación deseada

# Solicitar al usuario que ingrese la ubicación de la segunda zona horaria
println("Ingresa la ubicacion de la segunda zona horaria (ej. Asia/Tokyo): ")
ubicacion2 = readline()

# Crear un objeto DateTimeZone para la primera ubicación
time_zone1 = DateTimeZone(ubicacion1)

# Obtener la diferencia con GMT para la primera ubicación
offset_to_gmt1 = time_zone1.utc_offset_seconds / 3600
hora_actual1 = now(time_zone1)

# Crear un objeto DateTimeZone para la segunda ubicación
time_zone2 = DateTimeZone(ubicacion2)

# Obtener la diferencia con GMT para la segunda ubicación
offset_to_gmt2 = time_zone2.utc_offset_seconds / 3600

# Calcular la diferencia en horas entre las dos ubicaciones
diferencia_horaria = offset_to_gmt2 - offset_to_gmt1

# Calcular la hora actual en la segunda ubicación
hora_actual2 = now(time_zone1) + seconds(diferencia_horaria)

# Imprimir resultados
println("Diferencia con GMT para $ubicacion1: $offset_to_gmt1 horas")
println("Hora actual en $ubicacion1: ", hora_actual1)
println("Diferencia con GMT para $ubicacion2: $offset_to_gmt2 horas")
println("Hora actual en $ubicacion2: ", hora_actual2)
