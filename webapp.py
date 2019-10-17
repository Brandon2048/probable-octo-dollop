from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    if('Won' in request.args):
        USDtoWon = float(request.args['Won'])
        response3 = (USDtoWon) * (1179.46)
        return render_template('home.html', responseFromServer = response3)
    else:
        return render_template('home.html')

@app.route("/p1")
def render_page1():
    if('Dong' in request.args):
        USDtoDong = float(request.args['Dong'])
        response = (USDtoDong) * (23208)
        return render_template('VietnameseDong.html', responseFromServer = response)
    else:
        return render_template('VietnameseDong.html')

@app.route("/p2")
def render_page2():
    if('Rupee' in request.args):
        USDtoRupee = float(request.args['Rupee'])
        response1 = (USDtoRupee) * (71.5)
        return render_template('Rupee.html', responseFromServer = response1)
    else:
        return render_template('Rupee.html')

if __name__=="__main__":
    app.run(debug=False)
