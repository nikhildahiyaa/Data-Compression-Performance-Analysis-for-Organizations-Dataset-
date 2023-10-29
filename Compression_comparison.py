import pandas as pd
import gzip
import snappy
import lz4.frame as lz4frame
import time
import io

# Cleanup
def delete_columns_with_empty_cells(csv_file_path):
    # Read the CSV into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Check for empty cells in each column
    empty_columns = df.columns[df.isnull().any()]

    # Delete columns with empty cells
    df = df.drop(columns=empty_columns)

    # Save the updated DataFrame back to a CSV file
    updated_csv_file = csv_file_path[:-4] + "_updated.csv"  # Add "_updated" to the file name
    df.to_csv(updated_csv_file, index=False)

    return updated_csv_file

def compress_to_gzip(input_csv_file, output_gzip_file):
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(input_csv_file)

    # Write the DataFrame to a CSV file (in-memory buffer)
    csv_buffer = df.to_csv(index=False)

    # Compress the CSV data using gzip
    with gzip.open(output_gzip_file, 'wt', compresslevel=9) as gz_file:
        gz_file.write(csv_buffer)

    return output_gzip_file

def decompress_gzip_csv(gzip_csv_file):
    # Output file path for the decompressed CSV
    decompressed_csv_file = gzip_csv_file[:-3]  # Removing the '.gz' extension

    # Decompress the gzip file
    with gzip.open(gzip_csv_file, 'rb') as gz_file:
        with open(decompressed_csv_file, 'wb') as csv_file:
            csv_file.write(gz_file.read())

    return decompressed_csv_file


def compress_to_snappy(input_csv_file, output_snappy_file):
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(input_csv_file)

    # Write the DataFrame to a CSV file (in-memory buffer)
    csv_buffer = df.to_csv(index=False)

    # Compress the CSV data using Snappy
    compressed_data = snappy.compress(csv_buffer.encode())

    with open(output_snappy_file, 'wb') as snappy_file:
        snappy_file.write(compressed_data)

    return output_snappy_file

def decompress_snappy_csv(snappy_csv_file):
    # Output file path for the decompressed CSV
    decompressed_csv_file = snappy_csv_file[:-7]  # Removing the '.snappy' extension

    # Decompress the snappy file
    with open(snappy_csv_file, 'rb') as snappy_file:
        compressed_data = snappy_file.read()
        decompressed_data = snappy.uncompress(compressed_data)

    with open(decompressed_csv_file, 'wb') as csv_file:
        csv_file.write(decompressed_data)

    return decompressed_csv_file

def compress_to_lz4(input_csv_file, output_lz4_file):
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(input_csv_file)

    # Write the DataFrame to a CSV file (in-memory buffer)
    csv_buffer = df.to_csv(index=False)

    # Compress the CSV data using lz4
    compressed_data = lz4frame.compress(csv_buffer.encode())

    with open(output_lz4_file, 'wb') as lz4_file:
        lz4_file.write(compressed_data)

    return output_lz4_file

def decompress_lz4_csv(lz4_csv_file):
    # Output file path for the decompressed CSV
    decompressed_csv_file = lz4_csv_file[:-4]  # Removing the '.lz4' extension

    # Decompress the lz4 file
    with open(lz4_csv_file, 'rb') as lz4_file:
        decompressed_data = lz4frame.decompress(lz4_file.read())

    with open(decompressed_csv_file, 'wb') as csv_file:
        csv_file.write(decompressed_data)

    return decompressed_csv_file


# Example usage
orig_file = "/Users/nikkusmac/Desktop/project/orig_file.csv"
delete_columns_with_empty_cells(orig_file)

# Time for compression
start_time = time.time()
gzip_file = compress_to_gzip(orig_file, "gzip_dataset.csv.gz")
end_time = time.time()
print("Time for gzip compression: ", end_time - start_time)

start_time = time.time()
snappy_file = compress_to_snappy(orig_file, "snappy_dataset.csv.snappy")
end_time = time.time()
print("Time for snappy compression: ", end_time - start_time)

start_time = time.time()
lz4_file = compress_to_lz4(orig_file, "lz4_dataset.csv.lz4")
end_time = time.time()
print("Time for lz4 compression: ", end_time - start_time)

# Time for decompression
start_time = time.time()
uncompressed_gzip = decompress_gzip_csv(gzip_file)
end_time = time.time()
print("Time for gzip decompression: ", end_time - start_time)

start_time = time.time()
uncompressed_gzip = decompress_snappy_csv(snappy_file)
end_time = time.time()
print("Time for snappy decompression: ", end_time - start_time)

start_time = time.time()
uncompressed_gzip = decompress_lz4_csv(lz4_file)
end_time = time.time()
print("Time for lz4 decompression: ", end_time - start_time)


# Decompress+read
def total_employees_in_south_asian_countries(csv_file_path):
    start_time = time.time()
    # Read the CSV into a DataFrame
    df = pd.read_csv(csv_file_path)

    # List of South Asian countries
    south_asian_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Filter rows for South Asian countries
    south_asian_df = df[df['Country'].isin(south_asian_countries)]

    # Calculate the total number of employees in South Asian countries
    total_employees_in_south_asia = south_asian_df['Number of employees'].sum()

    end_time = time.time()
    print("Time for reading and processing data: ", end_time - start_time)

    #print(f"Total employees in South Asian countries: {total_employees_in_south_asia}")

def total_employees_in_south_asian_countries_gzip(gzip_compressed_csv_path):
    start_time = time.time()
    # Read the gzip-compressed CSV into a DataFrame
    with gzip.open(gzip_compressed_csv_path, "rt") as file:
        df = pd.read_csv(file)

    # List of South Asian countries
    south_asian_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Filter rows for South Asian countries
    south_asian_df = df[df['Country'].isin(south_asian_countries)]

    # Calculate the total number of employees in South Asian countries
    total_employees_in_south_asia = south_asian_df['Number of employees'].sum()
    end_time = time.time()
    print("Time for decompressing gzip, reading and processing data: ", end_time - start_time)

    #print(f"Total employees in South Asian countries: {total_employees_in_south_asia}")


def total_employees_in_south_asian_countries_snappy(snappy_compressed_csv_path):
    start_time = time.time()
    # Read the snappy-compressed CSV into a DataFrame
    with open(snappy_compressed_csv_path, "rb") as file:
        compressed_data = file.read()
        decompressed_data = snappy.uncompress(compressed_data)
        df = pd.read_csv(io.BytesIO(decompressed_data))

    # List of South Asian countries
    south_asian_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Filter rows for South Asian countries
    south_asian_df = df[df['Country'].isin(south_asian_countries)]

    # Calculate the total number of employees in South Asian countries
    total_employees_in_south_asia = south_asian_df['Number of employees'].sum()

    end_time = time.time()
    print("Time for decompressing snappy, reading and processing data: ", end_time - start_time)

    #print(f"Total employees in South Asian countries: {total_employees_in_south_asia}")


def total_employees_in_south_asian_countries_lz4(lz4_compressed_csv_path):
    start_time = time.time()
    # Read the lz4-compressed CSV into a DataFrame
    with open(lz4_compressed_csv_path, "rb") as file:
        decompressed_data = lz4frame.decompress(file.read())
        df = pd.read_csv(io.BytesIO(decompressed_data))

    # List of South Asian countries
    south_asian_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Filter rows for South Asian countries
    south_asian_df = df[df['Country'].isin(south_asian_countries)]

    # Calculate the total number of employees in South Asian countries
    total_employees_in_south_asia = south_asian_df['Number of employees'].sum()
    
    end_time = time.time()
    print("Time for decompressing lz4, reading and processing data: ", end_time - start_time)

    #print(f"Total employees in South Asian countries: {total_employees_in_south_asia}")

# Writing+compress
def add_columns_to_csv(csv_file_path):
    # Read the CSV into a DataFrame
    df = pd.read_csv(csv_file_path)

    # List of South Asian countries
    south_asian_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Filter rows for South Asian countries
    south_asian_df = df[df['Country'].isin(south_asian_countries)]

    start_time = time.time()


    # Concatenate the original DataFrame and the modified DataFrame
    df_with_new_columns = pd.concat([df, south_asian_df], ignore_index=True)

    # Return the DataFrame as a CSV string
    updated_csv = df_with_new_columns.to_csv(index=False)
    end_time = time.time()
    print("Time for writing: ", end_time - start_time)

    return updated_csv


def add_columns_and_compress_gzip(csv_gzip_compressed_path):
    # Read the snappy-compressed CSV into a DataFrame
    with gzip.open(csv_gzip_compressed_path, "rt") as file:
        df = pd.read_csv(file)
    # List of South Asian countries
    south_asian_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Filter rows for South Asian countries
    south_asian_df = df[df['Country'].isin(south_asian_countries)]

    start_time = time.time()

    # Concatenate the original DataFrame and the modified DataFrame
    df_with_new_columns = pd.concat([df, south_asian_df], ignore_index=True)

    # Compress the DataFrame to gzip format
    with io.StringIO() as output_buffer:
        df_with_new_columns.to_csv(output_buffer, index=False)
        compressed_data = gzip.compress(output_buffer.getvalue().encode())

    # Write the compressed data to a new file
    output_file = "output_compressed_csv.gz"
    with open(output_file, "wb") as file:
        file.write(compressed_data)

    end_time = time.time()
    print("Time for writing and gzip compression: ", end_time - start_time)

    return output_file

def add_columns_and_compress_snappy(csv_file_path):
    df = pd.read_csv(csv_file_path)

    # List of South Asian countries
    south_asian_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Filter rows for South Asian countries
    south_asian_df = df[df['Country'].isin(south_asian_countries)]

    start_time = time.time()

    # Concatenate the original DataFrame and the modified DataFrame
    df_with_new_columns = pd.concat([df, south_asian_df], ignore_index=True)

    # Compress the DataFrame to snappy format
    compressed_data = snappy.compress(df_with_new_columns.to_csv(index=False).encode())

    # Write the compressed data to a new file
    output_file = "output_compressed_csv.snappy"
    with open(output_file, "wb") as file:
        file.write(compressed_data)

    end_time = time.time()
    print("Time for writing and snappy compression: ", end_time - start_time)

    return output_file

def add_columns_and_compress_lz4(csv_lz4_compressed_path):
    # Read the lz4-compressed CSV into a DataFrame
    with open(csv_lz4_compressed_path, "rb") as file:
        decompressed_data = lz4frame.decompress(file.read())
        df = pd.read_csv(io.BytesIO(decompressed_data))

    # List of South Asian countries
    south_asian_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

    # Filter rows for South Asian countries
    south_asian_df = df[df['Country'].isin(south_asian_countries)]

    start_time = time.time()

    # Concatenate the original DataFrame and the modified DataFrame
    df_with_new_columns = pd.concat([df, south_asian_df], ignore_index=True)

    # Compress the DataFrame to lz4 format
    compressed_data = lz4frame.compress(df_with_new_columns.to_csv(index=False).encode())

    # Write the compressed data to a new file
    output_file = "output_compressed_csv.lz4"
    with open(output_file, "wb") as file:
        file.write(compressed_data)

    end_time = time.time()
    print("Time for writing and lz4 compression: ", end_time - start_time)

    return output_file

total_employees_in_south_asian_countries(orig_file)
total_employees_in_south_asian_countries_gzip(gzip_file)
total_employees_in_south_asian_countries_snappy(snappy_file)
total_employees_in_south_asian_countries_lz4(lz4_file)

add_columns_to_csv(orig_file)
add_columns_and_compress_gzip(gzip_file)
add_columns_and_compress_snappy(orig_file)
add_columns_and_compress_lz4(lz4_file)


