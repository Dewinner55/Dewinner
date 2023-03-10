def about():
    with open('templates/about.html', 'r') as template:
        return template.read()


def image():
    with open('templates/image.html', 'r') as template:
        return template.read()


def contact():
    with open('templates/contact.html', 'r') as template:
        return template.read()


def video():
    with open('templates/video.html', 'r') as template:
        return template.read()


def profile():
    with open('templates/profile.html', 'r') as template:
        return template.read()
