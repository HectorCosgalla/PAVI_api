import os

from dotenv import load_dotenv
load_dotenv()

# set variables
os.environ['PYTHONPATH'] = os.getcwd()
os.environ['PROJECT_PATH'] = os.getcwd()
os.environ['PROJECT_MODULE_NAME'] = 'pavi'
os.environ['PROJECT_MODULE_PATH'] = os.path.join(os.getcwd(), os.getenv('PROJECT_MODULE_NAME'))


from pavi.blueprints.basic_endpoints import blueprint as basic_endpoints
from pavi.blueprints.documented_endpoints import blueprint as documented_endpoint
from pavi.app import app

app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(basic_endpoints)
app.register_blueprint(documented_endpoint)
app.run()