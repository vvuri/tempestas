from app import app

def print_start():
    print('Run server on Flask')

if __name__ == '__main__':
    print_start()
    app.run()