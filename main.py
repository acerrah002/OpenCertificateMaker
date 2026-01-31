import webview
from pathlib import Path

#The directory to the html file
BASE_DIR = Path(__file__).parent.resolve()

#it's going into the webassets then into the index.html version 2
html_file = BASE_DIR / "webassets" / "index2.html"

#give the title
window = webview.create_window(
    title='CertificateMaker',
    url=str(html_file) 
)

webview.start()