from flask import Flask, url_for, send_from_directory
import random

app = Flask(__name__)

# list of fortune cookie quotes
fortunes = [
    "A closed mouth gathers no feet.",
    "Actions speak louder than words.",
    "An eye for an eye only ends up making the whole world blind.",
    "Be the change you wish to see in the world.",
    "Happiness is not something ready made. It comes from your own actions.",
    "Luck is what happens when preparation meets opportunity.",
    "The only way to do great work is to love what you do.",
    "The road to success is always under construction.",
    "Today is a new day. Make the most of it.",
    "You miss 100% of the shots you don't take.",
    "Guerra is a mexican wiseman"
]

# list of image file names
images = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    "image4.jpg",
    "image5.jpg",
    "Image6.jpg"
]

@app.route('/')
def fortune():
    # choose a random fortune cookie quote
    quote = random.choice(fortunes)
    
    # choose a random color (purple or blue)
    colors = ["purple", "blue"]
    color = random.choice(colors)
    
    # choose a random image file name
    image = random.choice(images)
    
    # generate the URL of the image using the `url_for()` function
    image_url = url_for('serve_image', filename=image)
    
    # generate HTML code for the fortune cookie quote with the chosen color, doubled font size, and background image
    html = """
    <html>
        <body style='background-image: url({});'>
            <p style='color: {}; font-size: 24px;'>{}</p>
        </body>
    </html>
    """.format(image_url, color, quote)
    return html

# use the `send_from_directory()` function to serve the images from the `background` folder
@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(port=5000)
