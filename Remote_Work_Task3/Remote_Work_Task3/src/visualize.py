
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data" / "analysis_ready.csv"
FIGURES = BASE / "figures"


def visualize():

    df = pd.read_csv(DATA)

    FIGURES.mkdir(parents=True, exist_ok=True)

    # Figure 1: Remote Work Intensity vs Burnout
    plt.figure(figsize=(8, 5))

    sns.regplot(
        data=df,
        x="remote_intensity",
        y="burnout_score",
        scatter_kws={"alpha": 0.7}
    )

    plt.title("Remote Work Intensity vs Emotional Burnout")
    plt.xlabel("Estimated Remote Work Intensity (%)")
    plt.ylabel("Emotional Burnout Score")

    plt.tight_layout()

    plt.savefig(
        FIGURES / "fig1_remote_intensity_vs_burnout.png",
        dpi=300
    )

    plt.close()

    # Figure 2: Burnout by Work Arrangement
    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="work_arrangement",
        y="burnout_score",
        order=["Fully on-site", "Hybrid", "Fully remote"]
    )

    plt.title("Burnout Distribution by Work Arrangement")
    plt.xlabel("Work Arrangement")
    plt.ylabel("Emotional Burnout Score")

    plt.tight_layout()

    plt.savefig(
        FIGURES / "fig2_burnout_by_arrangement.png",
        dpi=300
    )

    plt.close()

    print("Visualizations completed!")
    print("Figures saved in:", FIGURES)


if __name__ == "__main__":
    visualize()
