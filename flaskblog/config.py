
class config:
    SECRET_KEY = '426161ca57b7f9a97093f28ede89d356'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    #MAIL_SERVER = 'smtp.gmail.com'
    #MAIL_PORT = 465
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = os.environ.get('EMAIL_USER')
    #MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'cd9d553e1c11f6'
    MAIL_PASSWORD = '7b19e9c1610b9e'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
