# an object of WSGI application

from flask import Flask

app = Flask(__name__)  # Flask constructor


# A decorator used to tell the application

# which URL is associated function

@app.route('/')
def hello():
    return 'HELLO'


if __name__ == '__main__':
    app.run()


# decorator to route URL

@app.route(

‘ / hello’)

# binding to the function of route

def hello_world():
    return ‘hello
    world’

    def hello_world():
        return ‘hello
        world’

        app.add_url_rule(‘ / ’, ‘hello’, hello_world)

        from flask import Flask

        app = Flask(__name__)

        # routing the decorator function hello_name

        @app.route('/hello/<name>')
        def hello_name(name):
            return 'Hello %s!' % name

        if __name__ == '__main__':
            app.run(debug=True)
