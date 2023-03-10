articles = [
    '<h1>Уроки ПайтонБ</h1>',
    '<h1>C++ lessons</h1>'
]

def blog_article(id):
    return """
    <html>
        <head><title>Article</title></head>
    """ + articles[id] + """

    </html>
    """

print(blog_article(0))