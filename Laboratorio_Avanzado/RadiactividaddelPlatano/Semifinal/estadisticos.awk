BEGIN {
    sum = 0
    sum2 = 0
    total_counts = 0
}
$1 >= min_canal && $1 <= max_canal && $2 + 0 == $2 {
    sum += $1 * $2
    sum2 += $1 * $1 * $2
    total_counts += $2
}
END {
    if (total_counts > 0) {
        media = sum / total_counts
        varianza = (sum2 / total_counts) - (media * media)
        desviacion = sqrt(varianza)
        print "mu =", media
        print "sigma =", desviacion
    } else {
        print "No hay datos en el rango"
    }
}