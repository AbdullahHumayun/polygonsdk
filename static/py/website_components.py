components = {
    'title': 'Dynamic Web Page',
    'css': 'static/css/styles.css',
    'js': 'staic/js/scripts.js',
    'div_content': '<h1>Welcome to my dynamic web page!</h1><p>Loaded asynchronously.</p>'
}


def load_content():
    with open('content.html', 'r') as file:
        return file.read()