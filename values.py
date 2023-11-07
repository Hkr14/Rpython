def save_live(ccs):
    file = open('plugins/files/cvvs/cvv.txt', 'a+') 
    if str(ccs) + "\n" not in file.readlines():
        file.write(str(ccs) + "\n")
        file.close()

def save_ccn(ccs):
    file = open('plugins/files/cvvs/ccn.txt', 'a+') 
    if str(ccs) + "\n" not in file.readlines():
        file.write(str(ccs) + "\n")
        file.close()