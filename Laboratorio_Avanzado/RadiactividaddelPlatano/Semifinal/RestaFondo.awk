BEGIN {
    print "Channel\tNet_Counts"
}

# Procesar primer archivo (Cs-137)
FILENAME == ARGV[1] {
    if (NF >= 3 && $1 + 0 == $1 && $3 + 0 == $3) {
        cesio[$1] = $3 + 0
        orden[++total] = $1
    }
}

# Procesar segundo archivo (Fondo)
FILENAME == ARGV[2] {
    if (NF >= 2 && $1 + 0 == $1 && $2 + 0 == $2) {
        fondo[$1] = $2 + 0
    }
}

END {
    # Ordenar canales
    n = asort(orden, canales_ordenados)
    
    for (i = 1; i <= n; i++) {
        canal = canales_ordenados[i]
        if (canal in cesio && canal in fondo) {
            neto = cesio[canal] - fondo[canal]
            if (neto < 0) neto = 0
            print canal "\t" neto
        }
    }
}