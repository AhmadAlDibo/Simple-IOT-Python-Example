"""

Hier is simple code om te laten zien hoe iot werkt 


"""

def server(ip= False, data = [], conect = False, requist = False):
    if conect:
        if ip:
            return "ip: 192.168.4.1"
        data = data
        data = str(data)
        data = data.split()
        if requist == True:
            return data
    else:
        return 'Failed!'
    
def router(ip = False, data = [], conecties = [], requists = []):
    if ip:
        return "192.168.60.3"
    
    elif requists in conecties:
        return data
    

def apparaat(ip= False):
    if ip:
        return "192.168.80.2"
    
Server = server(conect=True, requist= True, data=[1, 2, 4 , 5])
server.data = Server

Router = router(ip = False, data = server.data, requists=apparaat(ip=True), conecties=apparaat(ip=True))
router.data = Router

def show_data(data=False, ip = False):
    if data and ip:
        return f"{data} This is the data requirded from this Ip : {ip}"
    
data = show_data(data=router.data, ip=router(ip=True))
print(data)



"""
Dit code is geschrijven door "Ahmad Al Dibo" maandag 4 december 2023
Contact : 
    Email : 'ahmadaldibo288@gmail.com' of 'youtuba5478@gmail.com'



"""
