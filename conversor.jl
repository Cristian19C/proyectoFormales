using HTTP
using JSON
using Dates

# Nombre de la ciudad o país para obtener su diferencia con GMT
ubicacion1 = "America/Bogota"  # Cambia esto a la ubicación deseada

# Solicitar al usuario que ingrese la ubicación de la segunda zona horaria
println("Ingresa la ubicación de la segunda zona horaria (ej. Asia/Tokyo): ")
ubicacion2 = chomp(readline())

# Obtener la hora actual en la primera ubicación
url1 = "https://worldtimeapi.org/api/timezone/$ubicacion1"
response1 = HTTP.get(url1)
data1 = JSON.parse(String(response1.body))
utc_offset1 = parse(Int, split(data1["utc_offset"], ":")[1]) * 3600 + parse(Int, split(data1["utc_offset"], ":")[2]) * 60

# Obtener la hora actual en la segunda ubicación
url2 = "https://worldtimeapi.org/api/timezone/$ubicacion2"
response2 = HTTP.get(url2)
data2 = JSON.parse(String(response2.body))
utc_offset2 = parse(Int, split(data2["utc_offset"], ":")[1]) * 3600 + parse(Int, split(data2["utc_offset"], ":")[2]) * 60

# Calcular la diferencia en segundos entre las dos ubicaciones
diferencia_horaria = abs(utc_offset2 - utc_offset1)

# Calcular la diferencia en horas entre las dos ubicaciones
diferencia_horaria_horas = diferencia_horaria / 3600

# ... Código anterior para obtener la diferencia horaria ...

# Obtener la hora actual en la primera ubicación
hora_actual1 = now()

# Calcular la hora actual en la segunda ubicación
hora_actual2 = hora_actual1 + Millisecond(diferencia_horaria * 1000)

# Imprimir resultados
println("Diferencia con GMT para $ubicacion1: ", data1["utc_offset"], " Hora: ",Dates.format(hora_actual1, "dd/mm/yyyy HH:MM:SS"))
println("Diferencia con GMT para $ubicacion2: ", data2["utc_offset"], " Hora: ",Dates.format(hora_actual2, "dd/mm/yyyy HH:MM:SS"))

