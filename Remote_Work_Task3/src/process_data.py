
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
INPUT = BASE / "data" / "survey_final1.csv"
OUTPUT = BASE / "data" / "analysis_ready.csv"

GROUPS = {
    "boundary_blurring": ["Q7", "Q8", "Q9", "Q23", "Q24"],
    "burnout_score": ["Q10", "Q11", "Q12", "Q13", "Q25", "Q26"],
    "work_life_balance": ["Q14", "Q15", "Q16"],
    "schedule_autonomy": ["Q17", "Q18", "Q19", "Q27", "Q28"],
    "psychological_detachment": ["Q20", "Q21", "Q22", "Q29", "Q30"]
}

REMOTE_MAPPING = {
    "0": 0,
    "1-25": 12.5,
    "26-50": 38,
    "51-75": 63,
    "76-100": 88
}


def process_data():
    df = pd.read_csv(INPUT)

    # Check duplicate responses
    print("Duplicate rows:", df.duplicated().sum())

    # Check missing values
    print("\nMissing values:")
    print(df.isna().sum())

    # Validate age
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df = df[df["age"].ge(18)].copy()

    # Check remote working days
    df["remote_days"] = pd.to_numeric(
        df["remote_days"], errors="coerce"
    )

    df["invalid_remote_days"] = (
        df["remote_days"].notna()
        & ~df["remote_days"].between(0, 7)
    )

    # Check suspicious weekly hours
    df["weekly_hours"] = pd.to_numeric(
        df["weekly_hours"], errors="coerce"
    )

    df["hours_review"] = (
        df["weekly_hours"].lt(10)
        | df["weekly_hours"].gt(80)
        | df["weekly_hours"].isna()
    )

    # Calculate five construct scores
    for name, questions in GROUPS.items():
        df[questions] = df[questions].apply(
            pd.to_numeric, errors="coerce"
        )

        df[name] = df[questions].mean(axis=1).where(
            df[questions].notna().all(axis=1)
        )

    # Estimated remote work intensity
    df["remote_intensity"] = (
        df["remote_percentage"]
        .astype("string")
        .str.strip()
        .map(REMOTE_MAPPING)
    )

    # Save processed data
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        OUTPUT,
        index=False,
        encoding="utf-8-sig"
    )

    print("\nProcessing completed!")
    print("Final respondents:", len(df))
    print("Saved file:", OUTPUT)

    return df


if __name__ == "__main__":
    process_data()
