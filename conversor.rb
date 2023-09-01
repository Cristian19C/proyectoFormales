require 'tzinfo'
require 'date'

# Nombre de la ciudad o país para obtener su diferencia con GMT
ubicacion1 = "America/Bogota"  # Cambia esto a la ubicación deseada

# Solicitar al usuario que ingrese la ubicación de la segunda zona horaria
print "Ingresa la ubicación de la segunda zona horaria (ej. Asia/Tokyo): "
ubicacion2 = gets.chomp

# Crear un objeto TZInfo::Timezone para la primera ubicación
time_zone1 = TZInfo::Timezone.get(ubicacion1)

# Obtener la diferencia con GMT para la primera ubicación
offset_to_gmt1 = time_zone1.current_period.utc_total_offset / 3600
hora_actual1 = DateTime.now.new_offset(time_zone1.current_period.utc_total_offset)

# Crear un objeto TZInfo::Timezone para la segunda ubicación
time_zone2 = TZInfo::Timezone.get(ubicacion2)

# Obtener la diferencia con GMT para la segunda ubicación
offset_to_gmt2 = time_zone2.current_period.utc_total_offset / 3600

# Calcular la diferencia en horas entre las dos ubicaciones
diferencia_horaria = offset_to_gmt2 - offset_to_gmt1

# Calcular la hora actual en la segunda ubicación
hora_actual2 = DateTime.now.new_offset(time_zone1.current_period.utc_total_offset + diferencia_horaria * 3600)

# Imprimir resultados
puts "Diferencia con GMT para #{ubicacion1}: #{offset_to_gmt1} horas"
puts "Hora actual en #{ubicacion1}: #{hora_actual1.strftime('%Y-%m-%d %H:%M:%S')}"
puts "Diferencia con GMT para #{ubicacion2}: #{offset_to_gmt2} horas"
puts "Hora actual en #{ubicacion2}: #{hora_actual2.strftime('%Y-%m-%d %H:%M:%S')}"
