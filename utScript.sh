echo "UTSCRIPT - Run OCR Unit Tests!!!"

echo "set CHROME_BIN"
set CHROME_BIN="/bin/google-chrome"
echo "starting pytest"


coverage run -m pytest

coverage report -m

coverage xml

echo "Testing ends!!!"