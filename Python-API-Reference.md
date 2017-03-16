**Gateway Python3.5 Module API**

**( Version 1.0, 2017.01.23 )**



[[TOC]]

1. 개요

PallyCon 서비스 사용 시 pack rule 발급, license rule 발급, application 연동에 필요한 Gateway 페이지를 구성는데 사용 가능한 module 이다.

![image alt text](image_0.png)

1. licenseGateway :  Application 에서 컨텐츠 재생 요청 시 라이센스 룰 발급을 위해 PallyCon license server에서는 licenseGateway 페이지로 license Rule 정보를 요청하게 된다.

2. packageGateway : 패키져에서 컨텐츠 DRM 패키징 시 사용될 key 정보를 PallyCon license server에서는 packageGateway 페이지로 키 정보를 요청하게 된다.

2. API 

## Class RIRequest

	gateway 에 넘어온 data parsing 과 response data를 생성하는데 사용할 수 있다.

1. file path 

: lib/Gateway.py

2. Method 

#### *def *__init__(self, key, iv)

생성자, 전달받은 key와 iv를  이용해 aes 암복호화 객체를 생성.

#### *def* parser_decode ( self, params)

 	AES256(CBC) 암호화 된 데이터를 받아 복호화 한다.

**Parameter**

<table>
  <tr>
    <td>type</td>
    <td>name</td>
    <td>description</td>
  </tr>
  <tr>
    <td>str</td>
    <td>params</td>
    <td>AES256 암호화 된 값.</td>
  </tr>
</table>


**Return ***json*

*Example.*

<table>
  <tr>
    <td>@app.route('/CIDIssue', methods=['POST', 'GET'])
def _CIDIssue():
   request_object = gatewayDTO()
   data = request.form['data']
   ri = RIRequest(key=’aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa’, iv=’0123456789abcdf’)
   decode_data = ri.parser_decode(data)

   request_data = json.loads(decode_data)
   request_object.nonce = request_data['nonce']
   request_object.file_path = request_data['file_path']
   request_object.file_name = request_data['file_name']
   request_object.cid = 'test-sample'

   response_str = ri.creat_package_info(object = request_object)
   return response_str</td>
  </tr>
</table>


#### *def* parser_encode(self, params)

 	암호화할 str 데이터를 받아 AES256(CBC) 로 암호화 한다.

**Parameter**

<table>
  <tr>
    <td>type</td>
    <td>name</td>
    <td>description</td>
  </tr>
  <tr>
    <td>str</td>
    <td>params</td>
    <td>AES256 암호화 할 값.</td>
  </tr>
</table>


**Return ***str*

*Example.*

<table>
  <tr>
    <td>@app.route('/CIDIssue', methods=['POST', 'GET'])
def _CIDIssue():
   request_object = gatewayDTO()
   data = request.form['data']
   ri = RIRequest(key=’aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa’, iv=’0123456789abcdf’)
   decode_data = ri.parser_decode(data)

   request_data = json.loads(decode_data)
   request_object.nonce = request_data['nonce']
   request_object.file_path = request_data['file_path']
   request_object.file_name = request_data['file_name']
   request_object.cid = 'test-sample'

   response_str = ri.creat_package_info(object = request_object)
   return response_str</td>
  </tr>
</table>


#### *def* creat_package_info(self, object = gatewayDTO)

 	package rule 연동 response 규격에 맞춰 값을 생성한다.

**Parameter**

<table>
  <tr>
    <td>type</td>
    <td>name</td>
    <td>description</td>
  </tr>
  <tr>
    <td>gatewayDTO</td>
    <td>O\object</td>
    <td>package rule 발급을 위해 setting 가능한 DTO 객체</td>
  </tr>
</table>


**Return ***str*

*Example.*

<table>
  <tr>
    <td>@app.route('/CIDIssue', methods=['POST', 'GET'])
def _CIDIssue():
   request_object = gatewayDTO()
   data = request.form['data']
   ri = RIRequest(key=’aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa’, iv=’0123456789abcdf’)
   decode_data = ri.parser_decode(data)

   request_data = json.loads(decode_data)
   request_object.nonce = request_data['nonce']
   request_object.file_path = request_data['file_path']
   request_object.file_name = request_data['file_name']
   request_object.cid = 'test-cid'

   response_str = ri.creat_package_info(object = request_object)
   return response_str

‘’’
result : euh3OrEWXGWoJWS4rgy/bvU/6bnIyClZR5tydh0g79AhS1nbh971iJpJuHlrpyaFPPv4/Z7zMLI9UQhsVXvfYRVOdkdIglXFFnt/VNXssqQ=
before encrypt value : {"error_code":"0000","error_message":"success","cid":"test-cid","nonce":null}
‘’’</td>
  </tr>
</table>


#### *def *get_license_info(self)

만들어진 package rule 을 반환한다.

**Return ***json*

#### *def *create_license_rule(self, object = gatewayDTO)

License 발급에 필요한 값을 set 한 gatewayDTO 를 받아 JSON 규격에 맞게 파싱한후 AES256 암호화 한 값을 반환한다.

**Parameter**

<table>
  <tr>
    <td>type</td>
    <td>name</td>
    <td>description</td>
  </tr>
  <tr>
    <td>gatewayDTO</td>
    <td>object</td>
    <td>암호화할 값</td>
  </tr>
</table>


**Return ***str*

*Example.*

<table>
  <tr>
    <td>@app.route('/ContentUsageRightsInfo', methods=['POST', 'GET'])
def _ContentUsageRightsInfo():
   data = request.form['data']

   ri = RIRequest(key=’aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa’, iv=’0123456789abcdf’)
   decode_data = ri.parser_decode(data)
   print('paramter data :: {}'.format(decode_data))

   response_object = gatewayDTO()
   response_object.nonce = 'test'

   response_str = ri.create_license_rule(object=response_object)
   print(ri.get_license_rule())
   return response_str
‘’’
result : 
HpVWTdDNc1K1ACU+SGGQk65MaS4LkGNfO6WYtfI2iNzFr+/Fm/OQ0MY6Z7ts2JiV954TtOjJTkGma9vqQBP4L+DHUamGeTfpWcCsvDxTmp84kQ7wa0WYuQfgEZ/78T5hhiKGuzySK1xtYHeRhqB7JLPKj7HlTkTGjzGwcOZezScJ+QZBsNianw+gi7WbHldiTicXPeUpii3It76RhnCaNTgdW7aEV0ljiSrQyGHnO6StxSMzPxk/M103j3Ly2cQDY1JiFh8TgGJEjsXLp0Rbta4FNgLCtaeMHiJOLyuHQIqyplCGQQ5EcQRY20cJiw5Wk51nSdE3fstABEbyKO36mkzBCAgMQEi3YfgT1SDPF+4=
before encrypt value : {"error_code":"0000","error_message":"success","playback_policy":{"limit":true,"persistent":false,"expire_date":""},"security_policy":{"output_protect":{"allow_external_display":false,"control_hdcp":"0"},"allow_mobile_abnormal_device":false},"nonce":"test”}
‘’’</td>
  </tr>
</table>


#### *def** *get_license_rule (self)

만들어진 license rule 을 반환한다.

**Return ***String*

## Class gatewayDTO

	gateway 와의 통신에 필요한 data 객체. getter와 setter로 구성되어 있다.

1. file path 

: lib/gatewayDTO.py

## Class AESCipher

aes256(CBC) 암호화 모듈.

1. file path

: libs/AESCrypto256.py

2. method

#### 	*def *__init__(self, key, iv, sagment_size=128)

	생성자, 공용으로 사용될 key 와 iv 값, sagment size를(을) 셋팅한다. 

**Parameter**

<table>
  <tr>
    <td>type</td>
    <td>name</td>
    <td>description</td>
  </tr>
  <tr>
    <td>String</td>
    <td>key</td>
    <td>암호화를 풀기위한 key 값</td>
  </tr>
  <tr>
    <td>String</td>
    <td>iv</td>
    <td>암호화를 풀기위한 iv 값</td>
  </tr>
  <tr>
    <td>int</td>
    <td>sagment_size</td>
    <td>암호화 비트값</td>
  </tr>
</table>


#### *def *encrypt(self, enc )

	aes256 (CBC) encrypt -> base64 encode 된 값을  리턴한다.

**Parameter**

<table>
  <tr>
    <td>type</td>
    <td>name</td>
    <td>description</td>
  </tr>
  <tr>
    <td>string</td>
    <td>enc</td>
    <td>암호화할 값</td>
  </tr>
</table>


**Return ***str*

#### *def *decrypt(self, enc_data )

	base64 decode -> aes256 (CBC) decrypt -> 된 값을  리턴한다.

**Parameter**

<table>
  <tr>
    <td>type</td>
    <td>name</td>
    <td>description</td>
  </tr>
  <tr>
    <td>string</td>
    <td>enc_data</td>
    <td>암호화를 풀기 위한 값</td>
  </tr>
</table>


**Return ***str*

