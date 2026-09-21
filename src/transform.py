import pandas as pd
import os


def transform():

    df = pd.read_json("data/raw/products.json")

    # Extract nested rating information
    df["rating_rate"] = df["rating"].apply(lambda x: x["rate"])
    df["rating_count"] = df["rating"].apply(lambda x: x["count"])

    # Remove original nested column
    df = df.drop(columns=["rating"])

    # Data quality checks
    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate IDs:")
    print(df["id"].duplicated().sum())

    print("\nInvalid prices:")
    print((df["price"] <= 0).sum())

    print("\nUnique categories:")
    print(df["category"].unique())

    # Data quality validation
    assert df["id"].notna().all(), "Missing product IDs found"
    assert df["id"].is_unique, "Duplicate product IDs found"
    assert (df["price"] > 0).all(), "Invalid product prices found"
    assert df["category"].notna().all(), "Missing categories found"
    assert df["rating_rate"].between(0, 5).all(), "Invalid ratings found"
    assert (df["rating_count"] >= 0).all(), "Invalid rating counts found"

    print("\nData quality validation passed.")

    # Derived column
    df["rating_score"] = df["rating_rate"] * df["rating_count"]

    print("\nDerived column added:")
    print(
        df[
            ["title", "rating_rate", "rating_count", "rating_score"]
        ].head()
    )

    # Save processed data
    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(
        "data/processed/products_clean.csv",
        index=False
    )

    print("\nProcessed data saved successfully.")


if __name__ == "__main__":
    transform()