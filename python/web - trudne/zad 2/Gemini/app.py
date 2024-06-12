from flask import Flask, render_template, request

app = Flask(__name__)

komentarze = []

@app.route('/')
def index():
  """Strona główna ze wszystkimi komentarzami."""
  return render_template('index.html', komentarze=komentarze)

@app.route('/dodaj_komentarz', methods=['POST'])
def dodaj_komentarz():
  """Dodaj nowy komentarz."""
  imie = request.form['imie']
  komentarz = request.form['komentarz']

  komentarze.append({
      'imie': imie,
      'komentarz': komentarz,
  })

  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)
