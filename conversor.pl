use strict;
use warnings;
use DateTime::TimeZone;

# Nombre de la ciudad o país para obtener su diferencia con GMT
my $ubicacion1 = "America/Bogota";  # Cambia esto a la ubicación deseada

# Solicitar al usuario que ingrese la ubicación de la segunda zona horaria
print "Ingresa la ubicacion de la segunda zona horaria (ej. Asia/Tokyo): ";
my $ubicacion2 = <STDIN>;
chomp $ubicacion2;

# Crear un objeto DateTime::TimeZone para la primera ubicación
my $time_zone1 = DateTime::TimeZone->new(name => $ubicacion1);

# Obtener la diferencia con GMT para la primera ubicación
my $offset_to_gmt1 = $time_zone1->offset_for_datetime(DateTime->now) / 3600;
my $hora_actual1 = DateTime->now(time_zone => $time_zone1);

# Crear un objeto DateTime::TimeZone para la segunda ubicación
my $time_zone2 = DateTime::TimeZone->new(name => $ubicacion2);

# Obtener la diferencia con GMT para la segunda ubicación
my $offset_to_gmt2 = $time_zone2->offset_for_datetime(DateTime->now) / 3600;

# Calcular la diferencia en horas entre las dos ubicaciones
my $diferencia_horaria = $offset_to_gmt2 - $offset_to_gmt1;

# Calcular la hora actual en la segunda ubicación
my $hora_actual2 = DateTime->now(time_zone => $time_zone1)->add(hours => $diferencia_horaria);

# Imprimir resultados
print "Diferencia con GMT para $ubicacion1: $offset_to_gmt1 horas\n";
print "Hora actual en $ubicacion1: " . $hora_actual1->strftime("%Y-%m-%d %H:%M:%S") . "\n";
print "Diferencia con GMT para $ubicacion2: $offset_to_gmt2 horas\n";
print "Hora actual en $ubicacion2: " . $hora_actual2->strftime("%Y-%m-%d %H:%M:%S") . "\n";
