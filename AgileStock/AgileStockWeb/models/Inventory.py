

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy(app)

class Inventory(db.Model):
    itemNum = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	
	def __repr__(self):
		return f'<Inventory name:{self.name:s}, itemNum:{self.itemNum}>'