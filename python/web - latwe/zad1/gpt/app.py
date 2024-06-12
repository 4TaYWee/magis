from pyinstrument import Profiler

profiler = Profiler()
profiler.start()
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    headline = "Welcome to My Website"
    paragraph = "This is a simple website created using Python and Flask."
    image_url = "static/image.jpg"  # Path to your local image file

    return render_template('index.html', headline=headline, paragraph=paragraph, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
profiler.stop()
print(profiler.output_text())