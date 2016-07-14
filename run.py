# -*- coding: utf-8 -*-
from app import appFlask, socketio
# appFlask.run(debug=True, host='0.0.0.0')  # appFlask экземпляр класса Flask(__name__)

socketio.run(appFlask, debug=True, host='0.0.0.0')

