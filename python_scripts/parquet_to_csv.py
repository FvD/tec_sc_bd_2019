import fastparquet

pfile = fastparquet.ParquetFile('C:\\Users\\Brian\\Desktop\\dataScience\\mov_mig_cr.parquet')
with open('mov_mig_cr.csv', 'w') as fp:
    for i, df in enumerate(pfile.iter_row_groups()):
        write_header = (i == 0)
        df.to_csv(fp, index=False, header=write_header)
        break
