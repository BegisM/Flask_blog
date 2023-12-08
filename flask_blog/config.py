import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('285094777088-mn8ooatoe89hb97f2upilk30c1b0s5bf.apps.googleusercontent.com')  # Ваш клиентский идентификатор OAuth 2.0
    MAIL_PASSWORD = os.environ.get('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')  # Ваш секретный ключ OAuth 2.0
    MAIL_DEFAULT_SENDER = 'begis.sm@gmail.com'  # Ваш адрес электронной почты