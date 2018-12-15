import cgi
form = cgi.FieldStorage()
user = form.getfirst("user", "").upper()    # This way it's safe.
print form.getlist("item")
for item in form.getlist("item"):
    print item