import tempfile

filename = tempfile.mktemp() # Noncompliant
tmp_file = open(filename, "w+")

@app.route("/")  # this sets the route to this page
def home():
	return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html