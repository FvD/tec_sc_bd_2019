CSV_PART_BASE_NAME = "mov_mig_cr_parts/moving_mig_cr_part_{0}.csv"
CSV_HEADER = "PUE_ID_PUESTO_MIGRATORIO,DET_FECHA_MOVIMIENTO,DET_MOV_CICLO_MIGRATORIO,DET_DOCUMENTO," \
             "DET_FECHA_NACIMIENTO,DET_MOV_NOMBRE,DET_MOV_PRIMER_APELLIDO,DET_MOV_SEGUNDO_APELLIDO,DET_MOV_SEXO," \
             "NAC_ID,PROV_ID,DET_MOV_TIPO_PERMANENCIA,DET_MOV_PERMANENCIA,DET_MOV_OCUPACION\n"


def split_csv():
    index = 0
    max_lines = 500_000
    lines_read = []
    with open("mov_mig_cr.csv", "r") as file:
        next(file)
        for line in file:
            if len(line.strip()) != 0:
                lines_read.append(line)
                if len(lines_read) == max_lines:
                    with open(CSV_PART_BASE_NAME.format(index), "w+") as csv_part:
                        csv_part.write(CSV_HEADER)
                        for line_read in lines_read:
                            csv_part.write(line_read)
                    lines_read.clear()
                    index += 1
        if len(lines_read):
            with open(CSV_PART_BASE_NAME.format(index), "w+") as csv_part:
                csv_part.write(CSV_HEADER)
                for line_read in lines_read:
                    csv_part.write(line_read)


split_csv()
