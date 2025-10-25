BEGIN {
    FS=" "  # Define el separador de campo como un espacio
    OFS="," # Define el separador de salida como una coma
}

{
    # Guarda el número de la primera columna ($1) en el array
    # correspondiente a la dificultad de la tercera columna ($3)
    if ($3 == "Accesible") {
        ac[++count_ac] = $1
    } else if ($3 == "Intermedio") {
        inter[++count_inter] = $1
    } else if ($3 == "Dificil") {
        di[++count_di] = $1
    } else if ($3 == "Imposibler") {
        im[++count_im] = $1
    }
}

END {
    # Encuentra la cantidad máxima de elementos en cualquier columna
    max_count = count_ac
    if (count_inter > max_count) max_count = count_inter
    if (count_di > max_count) max_count = count_di
    if (count_im > max_count) max_count = count_im

    # Imprime los encabezados
    print "Accesible", "Intermedio", "Dificil", "Imposible"

    # Itera hasta el número máximo de elementos e imprime cada columna
    for (i = 1; i <= max_count; i++) {
        print ac[i], inter[i], di[i], im[i]
    }
}