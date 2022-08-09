from pykiwoom.kiwoom import *

kiwoom = Kiwoom(login=True)

account = kiwoom.GetLoginInfo("ACCNO")[0]              # 전체 계좌 리스트
user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명

# 신규 매수
kiwoom.SendOrder('SAMSUNG) Buy Request', '1019', account, 1, '005930', 10, 0, '03', '')

# 신규 매도
kiwoom.SendOrder('SAMSUNG) Sell Request', '1019', account, 2, '005930', 10, 0, '03', '')