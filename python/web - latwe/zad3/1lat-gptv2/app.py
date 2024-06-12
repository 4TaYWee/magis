from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    headline = "Welcome to My Website"
    paragraph = "This is a simple website created using Python and Flask."
    image_url = "static/image.jpg"  # Path to your local image file

    return render_template('index.html', headline=headline, paragraph=paragraph, image_url=image_url)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Here you can process the form data (e.g., send an email, save to a database, etc.)
    # For now, let's just print the data to the console
    print(f"Name: {name}, Email: {email}, Message: {message}")
    
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
