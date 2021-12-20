from py3cw.request import Py3CW
import a_config


p3cw = Py3CW(
    key = a_config.API_public,
    secret = a_config.API_secret
)

def getDealData():
    error, data = p3cw.request(
        entity='deals',
        action='',
        payload={
            "scope": 'active',
            "account_id" : a_config.account_id
        }
        )
    return data

def getEnabledBot():
    error, data = p3cw.request(
        entity='bots',
        action='',
        payload={
            "scope": 'enabled',
            "account_id" : a_config.account_id
        }
        )
    return data

def getDisabledBot():
    error, data = p3cw.request(
        entity='bots',
        action='',
        payload={
            "scope": 'disabled',
            "account_id" : a_config.account_id
        }
        )
    return data   

def StartBot():
    bots = getDisabledBot()
    for bot in bots:
        error, data = p3cw.request(
            entity='bots',
            action='enable',
            action_id = str(bot['id']),
            )
        print(error)
        print ("bot " + str(bot['id']) + " started")

def StopBot():
    bots = getEnabledBot()
    for bot in bots:
        error, data = p3cw.request(
            entity='bots',
            action='disable',
            action_id = str(bot['id']),
            )
        print(error)
        print ("bot " + str(bot['id']) + " stoped")

dealsList = getDealData()
current_active_deals = len(dealsList)
print("Current active deals : " + str(current_active_deals))

if (float(current_active_deals) >= float(a_config.max_deals)):
    StopBot()
else :
    StartBot()
