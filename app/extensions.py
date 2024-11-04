from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect

moment = Moment()
csrf = CSRFProtect()