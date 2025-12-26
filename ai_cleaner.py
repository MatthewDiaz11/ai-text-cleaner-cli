import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(raw_text: str) -> str:
    prompt = f"""
    Clean and summarize the following text.
    - Fix grammar
    - Make it concise
    - Provide bullet summary

    TEXT:
    {raw_text}
    """
    response = client.responses.create(
        model = "gpt-5",
        input = prompt
    )
    return response.output_text

def main():
    parser = argparse.ArgumentParser(description="Batch clean and summarize text files using AI.")
    parser.add_argument("input_dir", help="Folder containing .txt files to process")
    parser.add_argument("output_dir", help="Folder where cleaned files will be saved")
    parser.add_argument("--dry-run", action="store_true", help="Preview files without calling AI")
    parser.add_argument("--max-files", type=int, default=None, help="Limit number of files processed")

    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    dry_run = args.dry_run
    max_files = args.max_files

    if not os.path.isdir(input_dir):
        print(f"Error: input_dir '{input_dir}' does not exist or is not a folder.")
        return

    os.makedirs(output_dir, exist_ok=True)

    processed = 0
    skipped = 0

    for filename in sorted(os.listdir(input_dir)):
        
        if not filename.endswith(".txt"):
            continue

        if max_files is not None and processed >= max_files:
            print(f"Reached max-files limit ({max_files}). Stopping.")
            break

        input_path = os.path.join(input_dir, filename)

        with open(input_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        if not raw_text.strip():
            print(f"Skipped empty file: {filename}")
            skipped += 1
            continue

        if dry_run:
            print(f"[DRY RUN] Would Process {filename}")
            continue

        result = ask_ai(raw_text)

        out_name = filename.replace(".txt", "_cleaned.txt")
        output_path = os.path.join(output_dir, out_name)

        with open(output_path, "w", encoding="utf-8") as out_f:
            out_f.write(result)

        print(f"Processed {filename} -> {out_name}")
        processed += 1

    print(f"\nDone. Processed: {processed}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
