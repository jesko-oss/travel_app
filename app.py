from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/map')
def create_route():
    return render_template("map_extended.html")

@app.route('/routes')
def view_routes():
    return render_template("routes_list.html")

@app.route('/route-golden-ring')
def golden_route():
    return render_template("route_demo.html")

@app.route('/route-crimea')
def crimea_route():
    return render_template("route_crimea.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
