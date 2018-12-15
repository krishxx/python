import os
import re
import form

variable = ""
value = ""
r = ""
for key in form.keys():
        variable = str(key)
        value = str(form.getvalue(variable))
        r += "<p>"+ variable +", "+ value +"</p>\n" 

fields = "<p>"+ str(r) +"</p>"

print fields