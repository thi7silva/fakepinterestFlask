from SiteFlask import database, app
from SiteFlask.models import Usuario, Foto

with app.app_context():
    database.create_all()