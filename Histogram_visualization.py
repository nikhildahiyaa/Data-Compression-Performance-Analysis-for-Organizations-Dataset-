import matplotlib.pyplot as plt
import numpy as np

# Data for reading times for each file type
NVMe_running_times_decompress_read = [0.30100345611572266, 0.5314416885375977, 0.341874361038208, 0.3412036895751953]
SSD_running_times_decompress_read = [0.3830249309539795, 0.6072402000427246, 0.5279350280761719, 0.42310500144958496]
HDD_running_times_decompress_read = [0.7514752569821562, 1.0072402000427246, 0.8251178960102354, 0.8214035047890245]

NVMe_running_times_write_compress = [0.5614509582519531, 1.6217377185821533, 0.5570104122161865, 0.5492007732391357]
SSD_running_times_write_compress = [0.6876490116119385, 1.7325530052185059, 0.9249448776245117, 0.757343053817749]
HDD_running_times_write_compress = [1.0847154601560324, 2.0354102873014902, 1.3021473028932452, 1.1547520159632057]

# Labels for each file type
file_types = ["uncompressed", "gzip compressed", "snappy compressed", "lz4 compressed"]

# Combine all the data for plotting and transpose the array
all_running_times_read = np.array([NVMe_running_times_decompress_read, SSD_running_times_decompress_read, HDD_running_times_decompress_read]).T
all_running_times_write = np.array([NVMe_running_times_write_compress, SSD_running_times_write_compress, HDD_running_times_write_compress]).T

# Plotting
fig, axes = plt.subplots(2, 1, figsize=(10, 12))

bar_width = 0.2
index = np.arange(len(file_types))

# Plot for decompressing and reading times
axes[0].bar(index - bar_width, all_running_times_read[:, 0], bar_width, label='NVMe', color='red')
axes[0].bar(index, all_running_times_read[:, 1], bar_width, label='SSD', color='green')
axes[0].bar(index + bar_width, all_running_times_read[:, 2], bar_width, label='HDD', color='blue')

axes[0].set_xlabel(" ")
axes[0].set_ylabel("Running Time (seconds)")
axes[0].set_title("Comparison of Decompressing+Reading Speeds for Different File Types in Different Mediums")
axes[0].set_xticks(index)
axes[0].set_xticklabels(file_types, rotation=0)
axes[0].legend()

# Plot for writing and compression times
axes[1].bar(index - bar_width, all_running_times_write[:, 0], bar_width, label='NVMe', color='red')
axes[1].bar(index, all_running_times_write[:, 1], bar_width, label='SSD', color='green')
axes[1].bar(index + bar_width, all_running_times_write[:, 2], bar_width, label='HDD', color='blue')
axes[1].set_xlabel(" ")
axes[1].set_ylabel("Running Time (seconds)")
axes[1].set_title("Comparison of Writing+Compression Speeds for Different File Types in Different Mediums")
axes[1].set_xticks(index)
axes[1].set_xticklabels(file_types, rotation=0)
axes[1].legend()

plt.tight_layout()
plt.show()
