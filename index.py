from flask import Flask,render_template
#inicializamos
app=Flask(__name__)
#creamos rutas
@app.route('/')
def home():
    #return 'Home R2G'
    return render_template('home.html')
@app.route('/about')

def about():
    return render_template('about.html')
#que escuche siempre
if __name__=='__main__':
    app.run(debug=True)


