import os, json
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from controller import run_cake

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'bots/'
app.config['LANGUAGES'] = 'languages.json'


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/run", methods=['POST', 'GET'])
def run():
    if request.method == "POST":
        print "POST", request.form
        return run_competition(request.form)
    rtn = []
    with open(app.config["LANGUAGES"]) as f:
        languages = json.load(f)
    for file in os.listdir(app.config["UPLOAD_FOLDER"]):
        assert file in languages
        rtn.append('    <input type="checkbox" name="%s" id="%s" value="%s"/><label for="%s">%s</label><br/>'%(
            file,
            file,
            languages[file],
            file,
            file))
    return """
<form action="run" method="post" enctype="multipart/form-data">
%s
<input type="submit" value="Run">
</form>
"""%"\n".join(rtn)


# Route that will process the file upload
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    # Get the name of the uploaded file
    language = request.form["language"]
    if language == "":
        return "No language selected"
    file = request.files['file']
    if not file:
        return "No file selected"
    # Check if the file is one of the allowed types/extensions
    if not allowed_file(file.filename):
        return "Filename not allowed"
    # Make the filename safe, remove unsupported chars
    filename = secure_filename(file.filename)
    # Move the file form the temporal folder to
    # the upload folder we setup
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    with open(app.config["LANGUAGES"]) as f:
        languages = json.load(f)
    languages[filename] = language
    with open(app.config["LANGUAGES"], "w") as f:
        json.dump(languages, f)
    return redirect("run")


def run_competition(bots_playing):
    rtn = []
    for bot, language in bots_playing.items():
        rtn.append('sh "./commands/%s.sh" "./bots/%s" %s' % (language, bot, bot) + ' %s %s %s %s')
    return str(run_cake(rtn))


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=4343,
        debug=True
    )