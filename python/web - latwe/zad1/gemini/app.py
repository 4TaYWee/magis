from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  # Define your content
  headline = "Welcome to My Website!"
  paragraph = "This is a simple website created using Python's Flask framework. It displays a headline, paragraph, and an image."
  # Assuming your image is named "image.jpg" and stored in the same directory as this script
  image_filename = "image.jpg"  
  return render_template("index.html", headline=headline, paragraph=paragraph, image_filename=image_filename)

if __name__ == "__main__":
  app.run(debug=True)
