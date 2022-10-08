from datetime import datetime

def getPrice(target):
    totalPrice = 0
    for v in target:
        totalPrice += v.total
    return totalPrice
# expiration date status of drugs in DrugIN
def getExpiringItems(items):
    expired = {}
    today = datetime.now().date()
    # check if drug is expired
    for item in items:
        exp_date = item.expiration_data # typo
        delta_days = (exp_date - today).days
        print(delta_days)
        # if less than 60 days -> Expired
        if delta_days <= 60:
            expired[item] = f"{delta_days} days"
    return expired

def getItembyDestination(items):
    itemsByDestination = {}
    for item in items:
        if item.destination in itemsByDestination:
            itemsByDestination[item.destination] += 1
        else:
            itemsByDestination[item.destination] = 1
    return itemsByDestination
   


