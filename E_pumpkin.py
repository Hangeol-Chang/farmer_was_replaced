def plant_pumpkin():
    pass

def check_growth_pumpkin():
    pass

def replant_pumpkin(bronken_pumpkins):
    pass

def harvest_pumpkin():
    while True:
        bronken_pumpkins = check_growth_pumpkin()
        if bronken_pumpkins:
            replant_pumpkin(bronken_pumpkins)
        else:
            break

    harvest_pumpkin()
    return True