from flask import Flask, request
from flask import render_template
import json
from lib.Gateway import RIRequest
from lib.gatewayDTO import gatewayDTO
import config
app = Flask(__name__)

@app.context_processor
def utility_processor():
	def format_encrypt(value, currency=u'€'):
		ri = RIRequest(key=config.site_key, iv='0123456789abcdef')
		return_str = ri.parser_encode(value)
		return return_str
	return dict(format_encrypt=format_encrypt)

@app.route('/encryptAes', methods=['POST', 'GET'])
def _encryptAes():
	data = request.form['jsonstr']
	ri = RIRequest(key=config.site_key, iv='0123456789abcdef')
	response_str = ri.parser_encode(data)
	return response_str

@app.route('/CIDIssue', methods=['POST', 'GET'])
def _CIDIssue():
	request_object = gatewayDTO()
	data = request.form['data']
	ri = RIRequest(key=config.site_key, iv='0123456789abcdef')
	decode_data = ri.parser_decode(data)

	request_data = json.loads(decode_data)
	request_object.nonce = request_data['nonce']
	request_object.file_path = request_data['file_path']
	request_object.file_name = request_data['file_name']
	request_object.cid = 'test-sample'

	response_str = ri.creat_package_info(object = request_object)
	return response_str

@app.route('/ContentUsageRightsInfo', methods=['POST', 'GET'])
def _ContentUsageRightsInfo():
	data = request.form['data']

	ri = RIRequest(key=config.site_key, iv='0123456789abcdef')
	decode_data = ri.parser_decode(data)
	print('paramter data :: {}'.format(decode_data))
	
	response_object = gatewayDTO()
	response_object.nonce = 'test'
	response_object.cek = 'asd'

	response_str = ri.create_license_rule(object=response_object)
	print(ri.get_license_rule())
	return response_str


if __name__ == '__main__':
	app.debug = True
	app.run(port=8080)
