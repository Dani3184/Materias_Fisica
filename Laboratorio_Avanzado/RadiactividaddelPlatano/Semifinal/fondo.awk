# Versión ordenada - promedio_fondo.awk
BEGIN {
    print "Channel\tAverage_Counts"
}

# Procesar solo líneas con datos de canales
NF == 3 && $1 ~ /^[0-9]+$/ && $2 ~ /^[0-9.]+$/ && $3 ~ /^[0-9]+$/ {
    if (FILENAME == ARGV[1]) {
        counts1[$1] = $3
        # Guardar el orden de los canales
        channels[++count] = $1
    }
    else if (FILENAME == ARGV[2]) {
        counts2[$1] = $3
    }
}

END {
    # Ordenar los canales numéricamente
    n = asort(channels, sorted_channels)
    
    # Imprimir en orden
    for (i = 1; i <= n; i++) {
        channel = sorted_channels[i]
        if (channel in counts2) {
            avg = int((counts1[channel] + counts2[channel]) / 2)
            print channel "\t" avg
        }
    }
}