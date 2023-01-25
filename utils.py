from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('426661484B477875596B57327A57755270596448726C6657765574466D4F434442697759754C4A313149453D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'your verification code: {code}'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)