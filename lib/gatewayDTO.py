class gatewayDTO:

	def __init__(self):
		'''
			gateway
		'''
		self._limit = False
		self._persistent = False
		self._duration = 0
		self._expire_date = None
		self._hardware_drm = False
		self._allow_external_display = False
		self._control_hdcp = 0
		self._allow_mobile_abnormal_device = False
		self._key_id = None
		self._cenc_key = None
		self._cenc_iv = None
		self._hls_key = None
		self._hls_iv = None
		self._nonce = None
		self._cek = None
		'''
			packager
		'''
		self._file_name = None
		self._file_path = None
		self._cid = None
		'''
			service manager
		'''
		self._mode = None
		self._site_id = None
		self._user_id = None
		self._device_id = None
		self._date = None
		self._category_name = None
		self._content_name = None
		self._info_order_id = None
		self._info_one = None
		self._info_two = None
		self._info_three = None
		self._info_four = None
		self._last_play_time = None
		self._lms_percent = None
		self._lms_sections = None

	@property
	def lms_sections(self):
		return self._lms_sections

	@lms_sections.setter
	def lms_sections(self, value):
		if isinstance(value, str):
			self._lms_sections  = value
		else:
			raise ValueError('Invalid lms_sections value')

	@property
	def lms_percent(self):
		return self._lms_percent

	@lms_percent.setter
	def lms_percent(self, value):
		if isinstance(value, str):
			self._lms_percent  = value
		else:
			raise ValueError('Invalid lms_percent value')

	@property
	def last_play_time(self):
		return self._last_play_time

	@last_play_time.setter
	def last_play_time(self, value):
		if isinstance(value, str):
			self._last_play_time  = value
		else:
			raise ValueError('Invalid last_play_time value')

	@property
	def info_four(self):
		return self._info_four

	@info_four.setter
	def info_four(self, value):
		if isinstance(value, str):
			self._info_four  = value
		else:
			raise ValueError('Invalid info_four value')

	@property
	def info_three(self):
		return self._info_three

	@info_three.setter
	def info_three(self, value):
		if isinstance(value, str):
			self._info_three  = value
		else:
			raise ValueError('Invalid info_three value')

	@property
	def info_two(self):
		return self._info_two

	@info_two.setter
	def info_two(self, value):
		if isinstance(value, str):
			self._info_two  = value
		else:
			raise ValueError('Invalid info_two value')

	@property
	def info_one(self):
		return self._info_one

	@info_one.setter
	def info_one(self, value):
		if isinstance(value, str):
			self._info_one  = value
		else:
			raise ValueError('Invalid info_one value')

	@property
	def info_order_id(self):
		return self._info_order_id

	@info_order_id.setter
	def info_order_id(self, value):
		if isinstance(value, str):
			self._info_order_id  = value
		else:
			raise ValueError('Invalid info_order_id value')

	@property
	def content_name(self):
		return self._content_name

	@content_name.setter
	def content_name(self, value):
		if isinstance(value, str):
			self._content_name  = value
		else:
			raise ValueError('Invalid content_name value')

	@property
	def category_name(self):
		return self._category_name

	@category_name.setter
	def category_name(self, value):
		if isinstance(value, str):
			self._category_name  = value
		else:
			raise ValueError('Invalid category_name value')


	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, value):
		if isinstance(value, str):
			self._date  = value
		else:
			raise ValueError('Invalid date value')

	@property
	def device_id(self):
		return self._device_id

	@device_id.setter
	def device_id(self, value):
		if isinstance(value, str):
			self._device_id  = value
		else:
			raise ValueError('Invalid device_id value')

	@property
	def user_id(self):
		return self._user_id

	@user_id.setter
	def user_id(self, value):
		if isinstance(value, str):
			self._user_id  = value
		else:
			raise ValueError('Invalid user_id value')

	@property
	def site_id(self):
		return self._site_id

	@site_id.setter
	def site_id(self, value):
		if isinstance(value, str):
			self._site_id  = value
		else:
			raise ValueError('Invalid site_id value')

	@property
	def mode(self):
		return self._mode

	@mode.setter
	def mode(self, value):
		if isinstance(value, str):
			self._mode  = value
		else:
			raise ValueError('Invalid mode value')

	@property
	def cid(self):
		return self._cid

	@cid.setter
	def cid(self, value):
		if isinstance(value, str):
			self._cid  = value
		else:
			raise ValueError('Invalid cid value')

	@property
	def file_path(self):
		return self._file_path

	@file_path.setter
	def file_path(self, value):
		if isinstance(value, str):
			self._file_path  = value
		else:
			raise ValueError('Invalid file path value')

	@property
	def file_name(self):
		return self._file_name

	@file_name.setter
	def file_name(self, value):
		if isinstance(value, str):
			self._file_name  = value
		else:
			raise ValueError('Invalid file name value')

	@property
	def cek(self):
		return self._cek

	@cek.setter
	def cek(self, value):
		if isinstance(value, str):
			self._cek  = value
		else:
			raise ValueError('Invalid cek value')

	@property
	def nonce(self):
		return self._nonce

	@nonce.setter
	def nonce(self, value):
		if isinstance(value, str):
			self._nonce  = value
		else:
			raise ValueError('Invalid nonce value')

	@property
	def hls_iv(self):
		return self._hls_iv

	@hls_iv.setter
	def hls_iv(self, value):
		if isinstance(value, str):
			self._hls_iv  = value
		else:
			raise ValueError('Invalid hls iv value')

	@property
	def hls_key(self):
		return self._hls_key

	@hls_key.setter
	def hls_key(self, value):
		if isinstance(value, str):
			self._hls_key  = value
		else:
			raise ValueError('Invalid hls key value')

	@property
	def cenc_iv(self):
		return self._cenc_iv

	@cenc_iv.setter
	def cenc_iv(self, value):
		if isinstance(value, str):
			self._cenc_iv  = value
		else:
			raise ValueError('Invalid cenc iv value')

	@property
	def cenc_key(self):
		return self._cenc_key

	@cenc_key.setter
	def cenc_key(self, value):
		if isinstance(value, str):
			self._cenc_key  = value
		else:
			raise ValueError('Invalid cenc key  value')

	@property
	def limit(self):
		return self._limit

	@limit.setter
	def limit(self, value):
		if isinstance(value, bool):
			self._limit = value
		else:
			raise ValueError('Invalid limit value')

	@property
	def persistent(self):
		return self._persistent

	@persistent.setter
	def persistent(self, value):
		if isinstance(value, bool):
			self._persistent = value
		else:
			raise ValueError('Invalid persistent value')

	@property
	def duration(self):
		return self._duration

	@duration.setter
	def duration(self, value):
		if isinstance(value, int):
			self._duration = value
		else:
			raise ValueError('Invalid duration value')

	@property
	def expire_date(self):
		return self._expire_date

	@expire_date.setter
	def expire_date(self, value):
		if isinstance(value, str):
			self._expire_date = value
		else:
			raise ValueError('Invalid exprie date value')

	@property
	def hardware_drm(self):
		return self._hardware_drm

	@hardware_drm.setter
	def hardware_drm(self, value):
		if isinstance(value, bool):
			self._hardware_drm = value
		else:
			raise ValueError('Invalid hardware drm value')

	@property
	def allow_external_display(self):
		return self._allow_external_display

	@allow_external_display.setter
	def allow_external_display(self, value):
		if isinstance(value, bool):
			self._allow_external_display = value
		else:
			raise ValueError('Invalid external display drm value')

	@property
	def control_hdcp(self):
		return self._control_hdcp

	@control_hdcp.setter
	def control_hdcp(self, value):
		if isinstance(value, int):
			self._control_hdcp = value
		else:
			raise ValueError('Invalid control hdcp drm value')

	@property
	def allow_mobile_abnormal_device(self):
		return self._allow_mobile_abnormal_device

	@allow_mobile_abnormal_device.setter
	def allow_mobile_abnormal_device(self, value):
		if isinstance(value, bool):
			self._allow_mobile_abnormal_device = value
		else:
			raise ValueError('Invalid control hdcp drm value')

	@property
	def key_id(self):
		return self._key_id

	@key_id.setter
	def key_id(self, value):
		if isinstance(value, str):
			self._key_id = value
		else:
			raise ValueError('Invalid key id drm value')