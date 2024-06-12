from flask import Flask, render_template, request

app = Flask(__name__)

def validate_contact_form(name, email, message):
  """
  This function validates the contact form data.

  Args:
      name: User's name entered in the form.
      email: User's email entered in the form.
      message: User's message entered in the form.

  Returns:
      A list of error messages if validation fails, otherwise an empty list.
  """
  errors = []
  if not name:
    errors.append("Name is required.")
  if not email or not email.strip():
    errors.append("Email is required.")
  elif not ("@" in email and "." in email):
    errors.append("Invalid email format.")
  if not message:
    errors.append("Message is required.")
  return errors

@app.route('/')
def index():
    headline = "Welcome to My Website"
    paragraph = "This is a simple website created using Python and Flask."
    image_url = "static/image.jpg"  # Path to your local image file

    return render_template('index.html', headline=headline, paragraph=paragraph, image_url=image_url)

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    errors = validate_contact_form(name, email, message)
    if errors:
        # Validation failed, display errors in the template
        return render_template('index.html', headline="Contact Us", errors=errors, 
                                name=name, email=email, message=message)

    # Form data is valid, process it (e.g., send email, save to database)
    print(f"Name: {name}, Email: {email}, Message: {message}")
    
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
