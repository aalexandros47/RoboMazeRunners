Here's a breakdown of what each command does based on script:

python iengine.py test1.txt TT
This will run the script using the file test.txt and the Truth Table method for reasoning.
python iengine.py test1.txt FC
This will run the script using the file test1.txt and the Forward Chaining method for reasoning.
python iengine.py test2.txt BC
This will run the script using the file test2.txt and the Backward Chaining method for reasoning. Additionally, any output will be redirected to a file because of >>, appending the output to the existing contents of test2.txt (or creating it if it doesn't exist).

For GUI:
python iengine.py test1.txt TT --gui
