import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgres://tcrnvgwbzhpweo:rVY1jetgJn-QAz297QeYnkgxRU@ec2-54-243-243-135.compute-1.amazonaws.com:5432/d586q412j76rtc"
    DEBUG = True
    SECRET_KEY = os.environ.get("TEXTER_SECRET_KEY", os.urandom(12))
    
#class ProductionConfig(object):
#    SQLALCHEMY_DATABASE_URI = "postgres://tcrnvgwbzhpweo:rVY1jetgJn-QAz297QeYnkgxRU@ec2-54-243-243-135.compute-1.amazonaws.com:5432/d586q412j76rtc"
#    DEBUG = True
#    SECRET_KEY = os.environ.get("TEXTER_SECRET_KEY", os.urandom(12))
    
    