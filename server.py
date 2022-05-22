from flask import *
import os, sys

app = Flask(__name__, static_folder='static')

args = sys.argv[1:]

try:
    if args[0] == "local" or args[0] == "L":
        host = "0.0.0.0"
    elif args[0] == "online" or args[0] == "O":
        host = "127.0.0.1"
except:
    print("Use argument [[local|online]|[L|O]]")
    exit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#@app.route('/weather/', methods=('GET', 'POST'))
#def my_link():
#    where = request.args.get("where")
#    if not where:
#        where = "vucja luka"
#    return display_wdata(where)

if __name__ == '__main__':    
    app.run(debug=True, host=host, port="12345")
