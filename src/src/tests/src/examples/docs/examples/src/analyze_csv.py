import csv

def analyze(file_path):
    print("Cybrick CSV Analyzer")
    print("-" * 30)

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        total = 0
        suspicious = 0

        for row in reader:
            total += 1

            if row["status"] == "Suspicious":
                suspicious += 1
                print(
                    f"[!] Suspicious Traffic: "
                    f"{row['source_ip']} -> {row['destination_ip']} "
                    f"(Function {row['function_code']})"
                )

    print("\nSummary")
    print(f"Total Packets: {total}")
    print(f"Suspicious: {suspicious}")


if __name__ == "__main__":
    analyze("examples/modbus_sample.csv")
