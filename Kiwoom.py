from pykiwoom.kiwoom import *

kiwoom = Kiwoom(login=True)

account = kiwoom.GetLoginInfo("ACCNO")[0]              # 전체 계좌 리스트
user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명

def buyRequest(stock_code, nb_stocks):
    stock_name = kiwoom.GetMasterCodeName(stock_code)
    rq_name = stock_name + ' x ' + str(nb_stocks) + ' Buy'

    kiwoom.SendOrder(rq_name, '4949', account, 1, '005930', 10, 0, '03', '')

def sellRequest(stock_code, nb_stocks):
    stock_name = kiwoom.GetMasterCodeName(stock_code)
    rq_name = stock_name + ' x ' + str(nb_stocks) + ' Buy'

    kiwoom.SendOrder(rq_name, '8989', account, 2, '005930', 10, 0, '03', '')

def getStockBasicInfo():
    tr_code = 'opt10001'
    stock_code = '005930'
    output = '주식기본정보'
    next = '0'
    name = kiwoom.block_request(tr_code, 종목코드 = stock_code, output = output, next = next)
    
    return name