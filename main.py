from app import create_app, db
from app.models import Users, Profile

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':Users, 'Post':Profile}


if __name__ == '__main__':
     app.run()