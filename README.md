# PDF Handling 
Programatically merge and write over pdf files with python.

## Install Dependencies
```
pip install reportlab
pip install pypdf2
```

## Usage
### pdf_writing_merging.py
The script takes as input three file names, declared at the beginning of the file:
- Input pdf file name (original pdf to handle)
- Watermark file name (file to be merged into pdf)
- Output pdf file name 

The script will programatically draw over the pdf and merge it with the watermark. 
To run the script:
```
python pdf_writing_merging.py
```
