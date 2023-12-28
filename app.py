from flask import Flask,jsonify
from pyservicebinding import binding

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"

@app.route('/bindings')
def return_bindings():
  try:
    sb = binding.ServiceBinding()
    return jsonify(sb.all_bindings())
  except binding.ServiceBindingRootMissingError as msg:
    return "SERVICE_BINDING_ROOT env var not set"

if __name__ == "__main__":
  port = int(os.getenv("PORT", 8080))
  app.run(host='0.0.0.0', port=port, debug=True)
