import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data_import import import_data

pd.options.mode.chained_assignment = None  # default='warn'


def year_dist(data: pd.DataFrame) -> None:
    data = data.dropna(subset=["year"])
    data = data[data["type"].isin(["TV Show", "Album", "Movie"])]
    sns.violinplot(data=data, x="type", y="year")

    plt.xlabel("Media Type")
    plt.ylabel("Release Year")
    plt.title("Media Release Years")

    plt.grid(axis="y", alpha=0.4)

    plt.tight_layout()
    plt.savefig("results/release_year_violin.pdf")
    plt.close()


def duration_dist(data: pd.DataFrame) -> None:
    data = data.dropna(subset=["duration"])
    data = data[~((data["type"] == "Track") & (data["duration"] > 50)) & (data["duration"] > 1)]
    data["log_duration"] = np.log10(data["duration"])
    sns.violinplot(data=data, x="type", y="log_duration")

    yticks_labels = [1, 10, 20, 45, 60, 120, 360]
    yticks = np.log10(yticks_labels)
    plt.yticks(yticks, yticks_labels)

    plt.xlabel("Media Type")
    plt.ylabel("Duration (minutes)")
    plt.title("Media Duration Logplot")

    plt.grid(axis="y", alpha=0.4)

    plt.tight_layout()
    plt.savefig("results/duration_violin.pdf")
    plt.close()


def type_bar(data: pd.DataFrame) -> None:
    data_count = data.groupby("type").count()
    x = data_count.index
    y = data_count["id"].values
    plt.bar(x, y, alpha=0.75)

    plt.xlabel("Media Type")
    plt.ylabel("Count")
    plt.title("Media Type Count")

    plt.grid(alpha=0.4)

    plt.tight_layout()
    plt.savefig(f"results/type_bar.pdf")
    plt.close()


def size_dist(data: pd.DataFrame) -> None:
    data = data.dropna(subset=["size"])
    data["log_size"] = np.log10(data["size"]/1000)
    sns.violinplot(data=data, x="type", y="log_size")

    yticks = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ytick_labels = [f"{size} {unit}" for unit in ["kB", "MB", "GB"] for size in [1, 10, 100]]

    plt.yticks(yticks, ytick_labels)
    plt.ylim(1, 8)

    plt.xlabel("Media Type")
    plt.ylabel("Size (kB)")
    plt.title("File Size Logplot")

    plt.grid(axis='y', alpha=0.4)

    plt.tight_layout()
    plt.savefig("results/size_violin.pdf")
    plt.close()


def bitrate_violin(data: pd.DataFrame) -> None:
    data.dropna(subset=["duration", "size"], inplace=True)
    data["bitrate"] = data["size"] / data["duration"] * 8 / 1000
    data = data[data["bitrate"] < 5e6]
    data["log_bitrate"] = np.log10(data["bitrate"])
    sns.violinplot(data=data, x="type", y="log_bitrate")

    ytick_labels = [f"{val} {unit}" for unit in ["kbps", "Mbps"] for val in [1, 10, 100]]
    yticks = [3, 4, 5, 6, 7, 8]
    plt.yticks(yticks, ytick_labels)

    plt.ylim(2.8, 6.5)

    plt.xlabel("Media Type")
    plt.ylabel("Bitrate")
    plt.title("Media Bitrate Logplot")

    plt.grid(axis="y", alpha=0.4)

    plt.tight_layout()
    plt.savefig("results/bitrate_violin.pdf")
    plt.close()


def main():
    data = import_data()
    year_dist(data)
    duration_dist(data)
    type_bar(data)
    size_dist(data)
    bitrate_violin(data)


if __name__ == "__main__":
    main()
