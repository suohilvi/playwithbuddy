import os
from app import create_app, db
from app.models import Role, User, Listing
from app import fake

app = create_app('production' if os.environ.get('DYNO') else 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Listing=Listing)