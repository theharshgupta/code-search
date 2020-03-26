from website import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    function_name = db.Column(db.String(1000), nullable=False)
    filepath = db.Column(db.String(1000), nullable=False)
    function_docstring = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f"Function({self.function_name}) \n Filepath:({self.filepath}))"
