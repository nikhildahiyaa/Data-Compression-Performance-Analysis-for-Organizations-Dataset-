import numpy as np
from scipy.stats import f_oneway

# Running times for NVMe, SSD, and HDD for decompressing and reading times
NVMe_running_times_decompress_read = [0.30100345611572266, 0.5314416885375977, 0.341874361038208, 0.3412036895751953]
SSD_running_times_decompress_read = [0.3830249309539795, 0.6072402000427246, 0.5279350280761719, 0.42310500144958496]
HDD_running_times_decompress_read = [0.7514752569821562, 1.0072402000427246, 0.8251178960102354, 0.8214035047890245]

# Combine the data for the ANOVA test for decompressing and reading times
all_running_times_decompress_read = np.array(NVMe_running_times_decompress_read + SSD_running_times_decompress_read + HDD_running_times_decompress_read)
labels_decompress_read = ['NVMe'] * len(NVMe_running_times_decompress_read) + ['SSD'] * len(SSD_running_times_decompress_read) + ['HDD'] * len(HDD_running_times_decompress_read)

# Perform the ANOVA test for decompressing and reading times
f_stat_decompress_read, p_value_decompress_read = f_oneway(NVMe_running_times_decompress_read, SSD_running_times_decompress_read, HDD_running_times_decompress_read)

print(f"One-way ANOVA test for decompressing and reading times:")
print(f"F-statistic: {f_stat_decompress_read:.4f}")
print(f"P-value: {p_value_decompress_read:.4f}")

# Running times for NVMe, SSD, and HDD for writing and compression times
NVMe_running_times_write_compress = [0.5614509582519531, 1.6217377185821533, 0.5570104122161865, 0.5492007732391357]
SSD_running_times_write_compress = [0.6876490116119385, 1.7325530052185059, 0.9249448776245117, 0.757343053817749]
HDD_running_times_write_compress = [1.0847154601560324, 2.0354102873014902, 1.3021473028932452, 1.1547520159632057]

# Combine the data for the ANOVA test for writing and compression times
all_running_times_write_compress = np.array(NVMe_running_times_write_compress + SSD_running_times_write_compress + HDD_running_times_write_compress)
labels_write_compress = ['NVMe'] * len(NVMe_running_times_write_compress) + ['SSD'] * len(SSD_running_times_write_compress) + ['HDD'] * len(HDD_running_times_write_compress)

# Perform the ANOVA test for writing and compression times
f_stat_write_compress, p_value_write_compress = f_oneway(NVMe_running_times_write_compress, SSD_running_times_write_compress, HDD_running_times_write_compress)

print(f"One-way ANOVA test for writing and compression times:")
print(f"F-statistic: {f_stat_write_compress:.4f}")
print(f"P-value: {p_value_write_compress:.4f}")

