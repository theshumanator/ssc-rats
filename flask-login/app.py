from flask import Flask, request

app = Flask(__name__)

@app.route('/query-example')
def query_example():
    language = request.args.get('language')
    return '''<h1>The language value is: {}</h1>'''.format(language)

@app.route('/form-example', methods=['GET', 'POST'])
def formexample():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                     <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/json-example', methods=['POST'])
def jsonexample():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    example = req_data['examples'][0] #an index is needed because of the array
    boolean_test = req_data['boolean_test']
    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)

@app.route("/")
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)