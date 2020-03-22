from app import db
from app.utils import populate_db


def register(app):
    @app.cli.command()
    def db_populate():
        """Populate db with data from bioinformatics_posts_se.xml."""
        populate_db(db, "app/bioinformatics_posts_se.xml")
