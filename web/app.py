from flask import Flask, abort, send_from_directory

app = Flask(__name__)

@app.route('/<path:url>')
def file(url):
    if ".." in url or "~" in url or "//" in url:
        abort(403)
    if url.find('/') > 0:
        slashLoc = url.rindex('/')
        return send_from_directory(url[0:slashLoc], url[slashLoc+1:]), 200
    else:
        return send_from_directory('./', url), 200

@app.errorhandler(404)
def not_found(e):
    return send_from_directory('/templates', '404.html'), 404

@app.errorhandler(403)
def forbbiden(e):
    return send_from_directory('/templates', '403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
