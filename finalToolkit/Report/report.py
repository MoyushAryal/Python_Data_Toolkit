def generate_report(dataset):
    print("DATASET REPORT")
    print("=" * 45)

    print(f"Rows loaded      : {dataset.rows_loaded}")
    print(f"Rows dropped     : {dataset.rows_dropped}")
    print(f"Rows remaining   : {len(dataset.records)}")

    print("\n--- Dropped Rows ---")
    print(f"Blank rows       : {dataset.blank_rows}")
    print(f"Invalid ages     : {dataset.invalid_ages}")
    print(f"Invalid IDs      : {dataset.invalid_ids}")
    print(f"Duplicate IDs    : {dataset.duplicate_ids}")

    print("\n--- Data Cleaned ---")
    print(f"Word ages fixed  : {dataset.word_ages}")
    print(f"Missing scores   : {dataset.missing_scores}")
    print(f"Missing names    : {dataset.missing_names}")
    print(f"Missing cities   : {dataset.missing_cities}")

    print("\n--- Statistics ---")
    print(f"Average score    : {dataset.average_score():.2f}")
    print(f"Oldest person    : {dataset.oldest()}")
    print(f"Youngest person  : {dataset.youngest()}")
    print(f"People per city  : {dataset.people_per_city()}")

    print("=" * 45)