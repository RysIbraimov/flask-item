from app.models import *
from app import app
if __name__ == "__main__":
    db.create_all()
    from app.urls import *
    app.run(debug=True)
