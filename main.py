import webapp2
from helpers import alphabet_position, rotate_character
import logging

from sys import argv
import cgi

page_header = """
<!DOCTYPE html>

<html>
    <head>
        <style type="text/css">
        h1{
            margin-left: 450px;
            font-style: italic;
            margin-bottom: 50px;
            color:blue;
        }
        textarea  {
            width: 400px;
            height: 200px;
            margin-bottom:20px;
            margin-top: 20px;
            margin-left:100px;
            background-color:blue;

        }
        form {
            background-color:rgb(250,0,80);
            margin-right:400px;
            margin-left:300px;
            border-radius:5px;
        }

        input{
        background-color:blue;

        }

        </style>
        <title>Encrypt-A-Message</title>
    <head/>
    <body>
        <h1>Encrypt-A-Message</h1>
    """

page_footer = """
</body>
<html/>

"""



add_form ="""
    <form action="/" method = "post">
        <label>
            Rotate by:
            <input type="text" name="rot" value="0"/>
        </label>
        <label>
            <textarea type="text" name="text" value = "">{}</textarea>
        </label>
            Enter Text Here
            <input type="submit" value ="Click To Encrypt"/>
    </form>

"""

main_page = page_header + add_form + page_footer




def user_input_is_valid(argv):

    if len(argv) < 2:
        return False

    x = argv[1]
    if x.isdigit() == False:
        return False
    return True

def encrypt(escaped_message, rotated_by):
    encrypted =""  # empty sting will hold encrypted message
    for k in escaped_message:
        encrypts = rotate_character(k, rotated_by) # temporarily stores the new encrypted characters within the text
        encrypted = encrypted + encrypts

    return encrypted






class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write(main_page)

    def post(self):
        escaped_message = cgi.escape(self.request.get("text"), quote=True)
        escaped_rot = cgi.escape(self.request.get("rot"), quote=True)

        rotated_by = int(escaped_rot)

        main_page_1 = page_header + add_form.format(encrypt(escaped_message, rotated_by)) + page_footer

        
        self.response.write(main_page_1)











app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
