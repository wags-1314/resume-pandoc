#!/opt/homebrew/bin/python3
import argparse, subprocess

parser = argparse.ArgumentParser()
parser.add_argument("markdown_file", help="input markdown file")
parser.add_argument("pdf_file", help="output pdf file")
args = parser.parse_args()

subprocess.run(f"pandoc {args.markdown_file} -f markdown+yaml_metadata_block \
--template templates/jb2resume.latex \
-o {args.pdf_file}".split()) 
