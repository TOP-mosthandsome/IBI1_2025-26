This folder contains a completed Python script for Practical 14.
- `go_depth.py` - main script. It reads `go_obo.xml`, analyses it using both DOM and SAX, prints the GO term with the greatest number of `<is_a>` elements in each ontology, prints the time taken by each API, and reports which one was fastest.
- `go_obo_.xml` - small test file for checking that the script runs.
How to run with the real practical file

Put the `go_obo.xml` file in this same folder, then run:
bash
python go_depth.py go_obo.xml
Or, if the XML file is somewhere else:
bash
python go_depth.py /path/to/go_obo.xml

Important note
The practical PDF asks for a script that reads `go_obo.xml`, but the actual `go_obo.xml` data file was not included in the upload. Therefore, this folder contains the complete script and a small sample XML file for testing. When the real `go_obo.xml` is added, the same script will produce the real portfolio results.