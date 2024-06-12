from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    headline = "Welcome to My Website"
    paragraph = "This is a simple website created using Python and Flask."
    image_url = "static/image.jpg"  # Path to your local image file
    return render_template('index.html', headline=headline, paragraph=paragraph, image_url=image_url)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process the form data here (e.g., send email)
        return f"Thank you, {name}! We have received your message."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
