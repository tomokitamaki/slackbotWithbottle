from bottle import route, run, template, get, HTTPResponse
import json

@route('/hello')
def hello():
  return "Hello World!"

@route('/hello/<name>')
def hello(name):
    if name == 'tamaki':
        return template('Hello {{name}}{{name}}', name=name)
    else:
        return template('Hello {{name}}', name=name)
@route('/post/<id:int>')
def post(id):
    return template('id={{id}}', id=id)

@route('/tags/<tag_name:re:[a-z]+>')
def tags(tag_name):
    return template('tag_name={{tag_name}}', tag_name=tag_name)

@route('/file/<file_path:path>')
def server(file_path):
    return template('file_path={{file_path}}', file_path=file_path)

@get('/plz/memory/<sc:int:re:[0-9]{4}+>')
def returnMemory(sc):
    if sc == 1111:
        return '''this code is ({sc}) insert Memory is 120G'''.format(sc=sc)
    elif sc == 2222:
        return "this code is ({sc}) insert Memory 2TB".format(sc=sc)
    else:
        return "none"
@get('/plz/AH/<alpha:re:[A|B|C|D|E|F|G|H]+>')
def returnMean(alpha):
    fileobj = open('alphabet.json', 'r')
    data = json.load(fileobj)
    fileobj.close()
    body = data[alpha]
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

run(host='0.0.0.0', port=80, debug=True, reloader=True)


