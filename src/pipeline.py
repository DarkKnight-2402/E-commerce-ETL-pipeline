from extract import extract
from transform import transform
from load import load


def run_pipeline():

    print("========== ETL PIPELINE STARTED ==========")

    try:
        print("\n[1/3] Starting extraction...")
        extract()

        print("\n[2/3] Starting transformation...")
        transform()

        print("\n[3/3] Starting load...")
        load()

        print("\n========== ETL PIPELINE COMPLETED ==========")

    except Exception as e:
        print("\n========== ETL PIPELINE FAILED ==========")
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()