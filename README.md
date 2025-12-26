# ai-text-cleaner-cli

This project is a command line automation tool that leverages OpenAI to clean and summarize large volumes of text files. It demonstrates real-world API integration, CLI tooling, and batch data processing skills applicable to automation, AI tooling, and backend development.

---

## AI Text Cleaner & Summarizer (CLI)

A Python based command line tool that uses OpenAI to **clean, summarize, and structure text files in bulk**.  
It fixes grammar, makes content concise, and generates clear bullet point summaries automatically.

---

## Table of Contents

- Features  
- How It Works  
- Installation  
- Usage  
- Output  
- Tech Stack  
- Use Cases  
- Project Structure   
- Notes  

---

## Features

- Batch processes `.txt` files from a directory  
- Fixes grammar and improves clarity  
- Produces concise bullet point summaries  
- Dry-run mode to preview files without API calls  
- Optional file limit for controlled processing  
- Secure API key handling via `.env`  
- Simple and intuitive CLI interface  

---

## How It Works

1. Reads text files from an input folder  
2. Sends content to OpenAI for cleanup and summarization  
3. Saves cleaned output to a separate folder  
4. Skips empty or invalid files automatically  

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/ai-text-cleaner-cli.git
cd ai-text-cleaner-cli
```

### Install dependencies

```bash
pip install openai python-dotenv
```

### Set up environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Usage

### Basic usage

```bash
python main.py input_texts output_texts
```

### Dry run (no API calls)

```bash
python main.py input_texts output_texts --dry-run
```

### Limit number of files processed

```bash
python main.py input_texts output_texts --max-files 5
```

---

## Output

Processed files are saved using the following naming format:

```text
original_filename_cleaned.txt
```

Each output file contains:

- Cleaned and grammatically corrected text  
- Concise phrasing  
- A bullet-point summary  

---

## Tech Stack

- Python  
- OpenAI API  
- argparse  
- python-dotenv  

---

## Use Cases

- Cleaning lecture notes or study materials  
- Summarizing meeting transcripts or interviews  
- Processing raw or scraped text data
- MORE

---

## Project Structure

```text
.
├── main.py
├── README.md
├── .env.example
└── input/
    └── example.txt
```


---

## Notes

- Only `.txt` files are supported  
- API usage depends on your OpenAI plan  
- Do not commit your `.env` file  
