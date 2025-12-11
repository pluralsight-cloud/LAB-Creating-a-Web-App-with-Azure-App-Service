from flask import Flask, send_from_directory

app = Flask(__name__)
WEBPAGES_FOLDER = 'globomantics-asset-bundle/web-pages'

@app.route('/')
def index():
    return send_from_directory(WEBPAGES_FOLDER, 'index.html')

@app.route('/index.html') # Added route for index.html explicitly
def index_page(): # Added separate function for index.html route
    return send_from_directory(WEBPAGES_FOLDER, 'index.html')

@app.route('/media.html') # Changed route to '/media.html'
def media():
    return send_from_directory(WEBPAGES_FOLDER, 'media.html')

@app.route('/our-story.html') # Changed route to '/our-story.html'
def our_story():
    return send_from_directory(WEBPAGES_FOLDER, 'our-story.html')

@app.route('/robotics.html') # Changed route to '/robotics.html'
def robotics():
    return send_from_directory(WEBPAGES_FOLDER, 'robotics.html')

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(f'{WEBPAGES_FOLDER}/css', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(f'{WEBPAGES_FOLDER}/js', filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(f'{WEBPAGES_FOLDER}/images', filename)

@app.route('/fonts/<path:filename>')
def serve_fonts(filename):
    return send_from_directory(f'{WEBPAGES_FOLDER}/fonts', filename)

if __name__ == '__main__':
    app.run(debug=True)