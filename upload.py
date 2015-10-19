
import bottle
from bottle import route, request, run, template
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024 * 5

@route('/', method='GET')
def index_page():
    return template("index")

@route('/upload', method='POST')
def do_upload():
    data = request.files.data

    if data and data.file:
        raw = data.file.read() # This is dangerous for big files
        filename = data.filename
        return "Hello ! You uploaded %s (%d bytes)." % (filename, len(raw))
    return "You missed a field."

run(host='localhost', port=8080)

