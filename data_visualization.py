import re
import matplotlib.pyplot as plt

def find_lines_starting_with(start_string, filename="./scalability_test_data/scalability_test_final_results.txt"):
    with open(filename, "r") as file:
        content = file.readlines()
    pattern = re.compile(f"^{re.escape(start_string)}.*")
    return [line for line in content if pattern.match(line)]

def get_value(string):
    return round(float(string.split("=")[1]), 5)
proportion_lines = find_lines_starting_with("!proportion")

proportions = list(map(get_value, proportion_lines))

times_of_interest_strings = [
    "!song_metadata_preprocessing",
    "!merged_df_time",
    "!time_elapsed",
    "!hdfs_user_data_read_time"
]
times_labels = [
    "Song metadata processing",
    "Merging of metadata and user data",
    "Total time",
    "Reading user data from hdfs"
]

times_of_interest = [list(map(get_value, find_lines_starting_with(time_str))) for time_str in times_of_interest_strings]
times_of_interest = [list(map(lambda x: round(x / 60, 2), times)) for times in times_of_interest]
print(times_of_interest)
print(proportions)


for i, (times, label) in enumerate(zip(times_of_interest, times_labels)):
    if i == 3:
        plt.plot(proportions, times, label=label, marker='x', linestyle='--')
    else:
        plt.plot(proportions, times, label=label, marker='o')


plt.xlabel("Proportion size")
plt.xticks([round(p, 3) for p in proportions])
plt.ylabel("Time (minutes)")
plt.title("Scalability plot (using all workers)")
plt.legend()
plt.show()