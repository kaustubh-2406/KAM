from package import db, bcrypt 

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    hash_password = db.Column(db.String(60), nullable=False)
    crops = db.relationship('Crop', backref='farmer', lazy='dynamic')

    @property
    def password(self): 
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.hash_password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def __repr__(self):
        return f'<Farmer {self.id}>: {self.username} has {self.crops}'

class Trader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    hash_password = db.Column(db.String(60), nullable=False)
    def  __repr__(self):
        return f'<Trader {self.id}>: {self.username}'

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isVerified = db.Column(db.Boolean(), default=False)
    desc = db.Column(db.String(150), default="")
    owner = db.Column(db.Integer, db.ForeignKey('farmer.id'))
    def __repr__(self):
        return f'<Crop {self.id}>: {self.name} x {self.qty}'