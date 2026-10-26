import csv

with open('input_asteroid_data.csv', mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    output_headers = ['asteroid_id', 'ore_units', 'crystal_units', 'gas_units', 'total_units', 'cargo_value']

    with open('output_asteroid_data.csv', mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=output_headers)
        writer.writeheader()

        for row in reader:
            ore = int(row['ore_units'])
            crystal = int(row['crystal_units'])
            gas = int(row['gas_units'])

            total_units = ore + crystal + gas
            cargo_value = (ore * 2) + (crystal * 5) + (gas * 3)

            writer.writerow({
                'asteroid_id': row['asteroid_id'],
                'ore_units': ore,
                'crystal_units': crystal,
                'gas_units': gas,
                'total_units': total_units,
                'cargo_value': cargo_value
            })