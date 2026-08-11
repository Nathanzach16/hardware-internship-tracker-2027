# tracker_stats.py
import re

def summarize_tracker():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        applied = len(re.findall(r"🟡", content))
        assessment = len(re.findall(r"🔵", content))
        interviews = len(re.findall(r"🟣", content))
        offers = len(re.findall(r"🟢", content))

        print("==========================================")
        print("  HARDWARE INTERNSHIP PIPELINE SUMMARY    ")
        print("==========================================")
        print(f"  🟡 Applications Submitted : {applied}")
        print(f"  🔵 Online Assessments     : {assessment}")
        print(f"  🟣 Technical Interviews   : {interviews}")
        print(f"  🟢 Offers Received        : {offers}")
        print("==========================================")

    except FileNotFoundError:
        print("Error: README.md file not found in current directory.")

if __name__ == "__main__":
    summarize_tracker()
