import requests, json
from lib.AESCrypto256 import AESCipher
from lib.CustomException import CustomException
from lib.gatewayDTO import gatewayDTO

IV = '0123456789abcdef'
playback_policy = {}
security_policy = {}
external_key = {}
license_ruls = {}
package_ruls = {}
package_ruls_json = ''
license_ruls_json = ''

class RIRequest:


	def __init__(self, key, iv):
		self.key = key
		self.iv = iv

	def parser_request_service_manager(self, params):
		params = json.loads(params)
		requestDTO = gatewayDTO()
		if isinstance(params, dict):
			if 'mode' in params:
				requestDTO.mode = params['mode']
			else:
				requestDTO.mode = ''

			if 'site_id' in params:
				requestDTO.site_id = params['site_id']
			else:
				requestDTO.site_id = ''

			if 'user_id' in params:
				requestDTO.user_id = params['user_id']
			else:
				requestDTO.user_id = ''

			if 'device_id' in params:
				requestDTO.device_id = params['device_id']
			else:
				requestDTO.device_id = ''

			if 'date' in params:
				requestDTO.date = params['date']
			else:
				requestDTO.date = ''

			if 'date' in params:
				requestDTO.date = params['date']
			else:
				requestDTO.date = ''

			if 'category_name' in params:
				requestDTO.category_name = params['category_name']
			else:
				requestDTO.category_name = ''

			if 'content_name' in params:
				requestDTO.content_name = params['content_name']
			else:
				requestDTO.content_name = ''

			if 'info_order_id' in params:
				requestDTO.info_order_id = params['info_order_id']
			else:
				requestDTO.info_order_id = ''

			if 'info_one' in params:
				requestDTO.info_one = params['info_one']
			else:
				requestDTO.info_one = ''

			if 'info_two' in params:
				requestDTO.info_two = params['info_two']
			else:
				requestDTO.info_two = ''

			if 'info_three' in params:
				requestDTO.info_three = params['info_three']
			else:
				requestDTO.info_three = ''

			if 'info_four' in params:
				requestDTO.info_four = params['info_four']
			else:
				requestDTO.info_four = ''

			if 'last_play_time' in params:
				requestDTO.last_play_time = params['last_play_time']
			else:
				requestDTO.last_play_time = ''

			if 'lms_percent' in params:
				requestDTO.lms_percent = params['lms_percent']
			else:
				requestDTO.lms_percent = ''

			if 'lms_sections' in params:
				requestDTO.lms_sections = params['lms_sections']
			else:
				requestDTO.lms_sections = ''
		else:
			raise CustomException('paramter Type is not invalid!')

		return requestDTO


	def parser_decode(self, params):
		cipher = AESCipher(self.key, self.iv, 256)
		afterCipher = cipher.decrypt(params)
		temp = json.loads(afterCipher)
		return json.dumps(temp)


	def parser_encode(self, params):
		cipher = AESCipher(self.key, self.iv, 256)
		afterCipher = cipher.encrypt(params)
		return afterCipher

	def creat_package_info(self, object = gatewayDTO):
		global package_ruls
		global package_ruls_json
		error_code = "0000"
		error_message = "success"
		if isinstance(object, gatewayDTO):
			if isinstance(object.nonce, str):
				package_ruls['nonce'] = object.nonce
			else:
				error_code = "0001"
				error_message = "nonce is not invalid!"

			if isinstance(object.cid, str):
				package_ruls['cid'] = object.cid
			else:
				error_code = "0002"
				error_message = "cid is not invalid!"

		else:
			error_code = "0003"
			error_message = "paramter Type is not invalid!!"

		package_ruls['error_code'] = error_code
		package_ruls['error_message'] = error_message
		package_ruls_json = json.dumps(package_ruls)
		afterCipher = self.parser_encode(package_ruls_json)
		return afterCipher


	def get_package_info(self):
		global package_ruls
		return json.dumps(package_ruls, indent=4)


	def create_playback_policy(self, limit=False, persistent=False, duration=0, expire_date=None):
		global playback_policy
		if isinstance(limit, bool):
			playback_policy['limit'] = limit
		else:
			raise CustomException('limit paramter Type is not invalid!')

		if isinstance(persistent, bool):
			playback_policy['persistent'] = persistent
		else:
			raise CustomException('persistent paramter Type is not invalid!')
				
		if limit == True:
			if expire_date is None:
				if isinstance(duration, int):
					playback_policy['duration'] = duration
				else:
					raise CustomException('duration paramter Type is not invalid!')

			else:
				if isinstance(expire_date, str):
					playback_policy['expire_date'] = expire_date
				else:
					raise CustomException('expire date paramter Type is not invalid!')


	def create_security_policy(self, hardware_drm=False, allow_external_display=False, control_hdcp=0, allow_mobile_abnormal_device=False):
		global security_policy
		output_protect = {}
		if isinstance(hardware_drm, bool):
			security_policy['hardware_drm'] = hardware_drm
		else:
			raise CustomException('hardware drm paramter Type is not invalid!')

		if isinstance(allow_mobile_abnormal_device, bool):
			security_policy['allow_mobile_abnormal_device'] = allow_mobile_abnormal_device
		else:
			raise CustomException('abnormal device paramter Type is not invalid!')
			
		if isinstance(allow_external_display, bool):
			output_protect['allow_external_display'] = allow_external_display
		else:
			raise CustomException('external display paramter Type is not invalid!')
			
		if isinstance(control_hdcp, int):
			output_protect['control_hdcp'] = control_hdcp
		else:
			raise CustomException('hdcp paramter Type is not invalid!')

		security_policy['output_protect'] = output_protect


	def create_external_key(self, key_id=None, cenc_key=None, cenc_iv=None, hls_key=None, hls_iv=None, cek=None):
		global external_key
		mpeg_cenc = {}
		hls_aes = {}
		ncg = {}
		if key_id is not None:
			if isinstance(key_id, str):
				mpeg_cenc['key_id'] = key_id
			else:
				raise CustomException('key id paramter Type is not invalid!')

		if cenc_key is not None:
			if isinstance(cenc_key, str):
				mpeg_cenc['key'] = cenc_key
			else:
				raise CustomException('cenc key paramter Type is not invalid!')

		if cenc_iv is not None:
			if isinstance(cenc_iv, str):
				mpeg_cenc['iv'] = cenc_iv
			else:
				raise CustomException('cenc iv paramter Type is not invalid!')

		if hls_key is not None:
			if isinstance(hls_key, str):
				hls_aes['key'] = hls_key
			else:
				raise CustomException('hls key paramter Type is not invalid!')

		if hls_iv is not None:
			if isinstance(hls_iv, str):
				hls_aes['iv'] = hls_iv
			else:
				raise CustomException('hls iv paramter Type is not invalid!')

		if cek is not None:
			if isinstance(cek, str):
				ncg['cek'] = cek
			else:
				raise CustomException('cek paramter Type is not invalid!')

		if len(mpeg_cenc.keys()) != 0:
			external_key['mpeg_cenc'] = mpeg_cenc

		if len(hls_aes.keys()) != 0:
			external_key['hls_aes'] = hls_aes

		if len(ncg.keys()) != 0:
			external_key['ncg'] = ncg


	def create_license_rule(self, object = gatewayDTO):
		global license_ruls
		global playback_policy
		global security_policy
		global external_key
		global license_ruls_json
		if isinstance(object, gatewayDTO):
			error_code = '0000'
			error_message = 'success'
			if object.nonce is None:
				error_code = '1001'
				error_message = 'nonce is not invalid!'
			else:
				license_ruls['nonce'] = object.nonce
				self.create_playback_policy(limit=object.limit, persistent=object.persistent, duration=object.duration, expire_date=object.expire_date)
				self.create_security_policy(hardware_drm=object.hardware_drm, allow_external_display=object.allow_external_display, control_hdcp=object.control_hdcp, allow_mobile_abnormal_device=object.allow_mobile_abnormal_device)
				self.create_external_key(key_id=object.key_id, cenc_key=object.cenc_key, cenc_iv=object.cenc_iv, hls_key=object.hls_key, hls_iv=object.hls_iv, cek=object.cek)
				cenc = external_key.get('mpeg_cenc')
				if cenc is not None:
					if (cenc.get('key_id') is None) ^ (cenc.get('key') is None):
						error = '1002'
						error_message = 'mpeg cenc paramter Type is not invalid'

				hls = external_key.get('hls_aes')
				if hls is not None:
					if (hls.get('key') is None) ^ (hls.get('iv') is None):
						error = '1003'
						error_message = 'hls aes paramter is not invalid'

				if len(external_key.keys()) != 0:
					license_ruls['external_key'] = external_key

				if len(playback_policy.keys()) != 0:
					license_ruls['playback_policy'] = playback_policy

				if len(security_policy.keys()) != 0:
					license_ruls['security_policy'] = security_policy

			license_ruls['error_code'] = error_code
			license_ruls['error_message'] = error_message
			license_ruls_json = json.dumps(license_ruls)
			afterCipher = self.parser_encode(license_ruls_json)
			return afterCipher
		else:
			raise CustomException('Paramter Type is not invalid!')


	def get_license_rule(self):
		global license_ruls
		return json.dumps(license_ruls, indent=4)


	def ri_http_request(self, url, params):
		payload = {'data' : params}
		req = requests.get(url, params=payload)
		code = req.status_code
		if code == 200:
			return req.text
		else:
			return json.dumps({'code' : '0001', 'message' : 'request not found.'})


	def ri_http_request_decrypt(self, url, params):
		payload = {'data' : params}
		req = requests.get(url, params=payload)
		code = req.status_code
		if code == 200:
			cipher = AESCipher(self.key, self.iv, 256)
			afterCipher = cipher.decrypt(req.text)
			return json.dumps(afterCipher.decode())
		else:
			return json.dumps({'code' : '0001', 'message' : 'request not found.'})
