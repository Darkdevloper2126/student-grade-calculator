import json
from pathlib import Path


def load_scores(file_path: str):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Could not find file: {file_path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def calculate_sgpa(subjects):
    total_weighted_points = 0
    total_credits = 0

    for subject in subjects:
        credit = subject["credit"]
        grade_point = subject["grade_point"]
        total_weighted_points += credit * grade_point
        total_credits += credit

    if total_credits == 0:
        return 0, 0, 0

    sgpa = total_weighted_points / total_credits
    return total_weighted_points, total_credits, round(sgpa, 2)


def print_report(subjects, total_weighted_points, total_credits, sgpa):
    print("=" * 72)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 72)
    print(f"{'Subject':35} {'Credit':>8} {'Grade Point':>14} {'Points':>10}")
    print("-" * 72)

    for subject in subjects:
        name = subject["name"]
        credit = subject["credit"]
        grade_point = subject["grade_point"]
        points = credit * grade_point
        print(f"{name:35} {credit:>8} {grade_point:>14} {points:>10}")

    print("-" * 72)
    print(f"{'Total':35} {total_credits:>8} {'':>14} {total_weighted_points:>10}")
    print("=" * 72)
    print(f"SGPA: {sgpa}")
    print("=" * 72)


def main():
    try:
        subjects = load_scores("sample_scores.json")
        total_weighted_points, total_credits, sgpa = calculate_sgpa(subjects)
        print_report(subjects, total_weighted_points, total_credits, sgpa)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in sample_scores.json")
    except KeyError as e:
        print(f"Error: Missing required key in JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
