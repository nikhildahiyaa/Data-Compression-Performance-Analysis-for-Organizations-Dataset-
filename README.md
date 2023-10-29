
# Data Compression Performance Analysis


The initial problem posed was to explore data compression techniques including gzip, snappy, and lz4, and evaluate their performance. To make this analysis more practical and relevant, we chose to work with an organizations dataset. This dataset comprises 100,000 records of organizations, each with various attributes such as Organization Id, Name, Website, Country, Description, Founded Year, Industry, and Number of employees.

## Installing Required Libraries

Before running the project, make sure you have the following Python libraries installed:

- [pandas](https://pandas.pydata.org/): For data manipulation and analysis.
- [gzip](https://docs.python.org/3/library/gzip.html): For Gzip compression.
- [python-snappy](https://pypi.org/project/python-snappy/): For Snappy compression.
- [lz4](https://pypi.org/project/lz4/): For LZ4 compression.
- [numpy](https://numpy.org/): For numerical operations.
- [scipy](https://www.scipy.org/): For scientific and statistical computations.
- [matplotlib](https://matplotlib.org/): For creating visualizations.

You can install these libraries using the following command:

`pip install pandas gzip python-snappy lz4 numpy scipy matplotlib`

## Index

### Compression_comparison.py

This script performs compression and decompression using various algorithms (gzip, Snappy, and lz4) on a given CSV file.
It also includes functions to clean the CSV file by removing columns with empty cells, and to calculate statistics on
the total number of employees in South Asian countries.

Usage:
1. Replace 'orig_file' with the path to your input CSV file.
2. Run the script to see compression and decompression times for gzip, Snappy, and lz4.
3. The script also calculates and displays the time taken to read and process data for different compression formats.
4. The script creates and displays a new CSV with modified columns for South Asian countries.
5. You can adjust the compression functions' output file names according to your preference.

Libraries Used:
- pandas: For data manipulation and analysis.
- gzip: For Gzip compression.
- python-snappy: For Snappy compression.
- lz4: For LZ4 compression.
- io: For handling file buffers.
- time: For measuring time durations.

Output:
The script generates compressed files for each compression algorithm and decompressed files for each of these formats.
Additionally, it displays the time taken for compression, decompression, and data processing operations.

For example, to run the script:
1. Ensure you have the required libraries installed by following the instructions in the 'Installing Required Libraries' section of README.md.
2. Replace 'orig_file' with the path to your input CSV file.
3. Run the script in your terminal: 
`python Compression_comparison.py`

### ANOVA_test.py


This script performs a one-way ANOVA test on running times data collected from different storage devices (NVMe, SSD, HDD) for two scenarios:
1. Decompressing and reading times
2. Writing and compression times

The script uses the scipy library to perform the ANOVA test, which helps determine if there are any significant differences
in the means of the running times between the different storage devices for each scenario.

Usage:
1. Replace the running times data (NVMe, SSD, HDD) for decompressing and reading times and writing and compression times.
2. Run the script to see the results of the ANOVA tests for both scenarios.
3. The script calculates the F-statistic and p-value for each scenario and prints the results.

Libraries Used:
- numpy: For numerical operations.
- scipy.stats.f_oneway: For performing the one-way ANOVA test.

Output:
The script displays the F-statistic and p-value for both scenarios:
1. Decompressing and reading times ANOVA test.
2. Writing and compression times ANOVA test.

For example, to run the script:
1. Replace the running times data in the script with your actual data.
2. Run the script in your terminal: `python ANOVA_test.py`

### Histogram_visualization.py



This script generates histograms to visually compare the running times for different file types across different storage mediums.
It plots two histograms: one for decompressing and reading times, and another for writing and compression times.

Usage:
1. Replace the running times data for decompressing and reading times and writing and compression times.
2. Run the script to see the histograms comparing the running times.
3. The script generates separate histograms for both scenarios, showing the running times for each file type on different storage mediums.

Libraries Used:
- matplotlib.pyplot: For creating visualizations.
- numpy: For numerical operations.

Output:
The script generates two histograms:
1. Decompressing and reading times histogram.
2. Writing and compression times histogram.


For example, to run the script:
1. Replace the running times data in the script with your actual data.
2. Run the script in your terminal: 
`python Histogram_visualization.py`







## References 
https://www.datablist.com/learn/csv/download-sample-csv-files




