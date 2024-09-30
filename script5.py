import random
import math

name = "script5"


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1


def ActPirate(pirate):
    count = pirate.getCurrentFrame()
    print(count)
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    se = pirate.investigate_se()[0]
    sw = pirate.investigate_sw()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    a,b = pirate.getDeployPoint()
    s = pirate.trackPlayers()
    name = int(pirate.getID())
    X = int(pirate.getDimensionX())
    Y = int(pirate.getDimensionY())

    # HUNTER VALUES
    wh1 = 3
    wh2 = 2
    wh3 = 2
    # GATHERER VALUES
    # wgd = dominant direction wgr = recessive direction for gatherers 1,2
    wgd = 2
    wgr = 1
    # wga,wgb = changing values for gatherers 1,2
    # wga should be greater than wgb
    wga = 1
    wgb = 1
    # wgdw = dominant direction wgx = recessive direction for gatherers 1,2
    wgw = 1.5
    wgx = 1
    # wgy,wgz = changing values for gatherers 1,2
    # wgy should be greater than wgz
    wgy = 1
    wgz = 1
    # defining per
    per = 2*X-1
    # occupation settings

    count1 = 2*per + name
    count2 = 3*per + name

    occupation = ''

    if count < count1:
        if name%12 == 0:
            occupation = 'hunter1'
        elif name%12 == 2:
            occupation = 'gatherer1'
        elif name%12 == 4:
            occupation = 'gatherer2'
        elif name%12 == 6:
            occupation = 'hunter1'
        elif name%12 == 8:
            occupation = 'gatherer3'
        elif name%12 == 10:
            occupation = 'gatherer4'
        elif name%8 == 1:
            occupation = 'gatherer1'
        elif name%8 == 3:
            occupation = 'gatherer2'
        elif name%8 == 5:
            occupation = 'gatherer3'
        elif name%8 == 7:
            occupation = 'gatherer4'
        else:
            occupation = 'hunter1'
    elif count < count2:
        if name%6 == 0:
            occupation = 'hunter1'
        elif name%6 == 2:
            occupation = 'hunter2'
        elif name%6 == 4:
            occupation = 'hunter3'
        elif name%8 == 1:
            occupation = 'gatherer1'
        elif name%8 == 3:
            occupation = 'gatherer2'
        elif name%8 == 5:
            occupation = 'gatherer3'
        elif name%8 == 7:
            occupation = 'gatherer4'
        else:
            occupation = 'hunter1'
    else:
        if name%4 == 1:
            occupation = 'hunter1'
        elif name%4 == 2:
            occupation = 'hunter2'
        elif name%4 == 3:
            occupation = 'hunter3'
        else:
            occupation = 'hunter1'
    
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        s = occupation[-1] + up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        s = occupation[-1] + down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")

        or (left == "island3" and s[2] != "myCaptured")
    ):
        s = occupation[-1] + left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        s = occupation[-1] + right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(s)
    if (
        (ne == "island1" and s[0] != "myCaptured")
        or (ne == "island2" and s[1] != "myCaptured")
        or (ne == "island3" and s[2] != "myCaptured")
    ):
        s = occupation[-1] + ne[-1] + str(x+1) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
        (nw == "island1" and s[0] != "myCaptured")
        or (nw == "island2" and s[1] != "myCaptured")
        or (nw == "island3" and s[2] != "myCaptured")
    ):
        s = occupation[-1] + nw[-1] + str(x-1) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
        (se == "island1" and s[0] != "myCaptured")
        or (se == "island2" and s[1] != "myCaptured")
        or (se == "island3" and s[2] != "myCaptured")
    ):
        s = occupation[-1] + se[-1] + str(x + 1) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if (
        (sw == "island1" and s[0] != "myCaptured")
        or (sw == "island2" and s[1] != "myCaptured")
        or (sw == "island3" and s[2] != "myCaptured")
    ):
        s = occupation[-1] + sw[-1] + str(x - 1) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if count < per + name:
        if name<=per:
            for i in range(3000):
                if count < (i+1)*per + name%per:
                    if i%2 == 0:
                        if a<b:
                            if name%2 == 1:
                                rotor = int((name%per - 1)/2)
                                return moveTo(X-1-rotor,0,pirate)
                            else:
                                rotor = int((name%per)/2)
                                return moveTo(X-1,rotor,pirate)
                        elif b<a:
                            if name%2 == 1:
                                rotor = int((name%per - 1)/2)
                                return moveTo(0,Y-1-rotor,pirate)
                            else:
                                rotor = int((name%per)/2)
                                return moveTo(rotor,Y-1,pirate)
                            
                        elif a == b and a<32:
                            if name%2 == 1:
                                rotor = int((name%per - 1)/2)
                                return moveTo(X-1-rotor,Y-1,pirate)
                            else:
                                rotor = int((name%per)/2)
                                return moveTo(X-1,Y-1-rotor,pirate)
                        else:
                            if name%2 == 1:
                                rotor = int((name%per - 1)/2)
                                return moveTo(rotor,0,pirate)
                            else:
                                rotor = int((name%per)/2)
                                return moveTo(0,rotor,pirate)
                    else:
                        if a<b:
                            if name%2 == 1:
                                rotor = int((name%per - 1)/2)
                                return moveTo(rotor,Y-1,pirate)
                            else:
                                rotor = int((name%per)/2)
                                return moveTo(0,Y-1-rotor,pirate)
                        elif b<a:
                            if name%2 == 1:
                                rotor = int((name%per - 1)/2)
                                return moveTo(X-1,rotor,pirate)
                            else:
                                rotor = int((name%per)/2)
                                return moveTo(X-1-rotor,0,pirate)
                            
                        elif a == b and a<32:
                            if name%2 == 1:
                                rotor = int((name%per - 1)/2)
                                return moveTo(rotor,0,pirate)
                            else:
                                rotor = int((name%per)/2)
                                return moveTo(0,rotor,pirate)
                        else:
                            if name%2 == 1:
                                rotor = int((name%per - 1)/2)
                                return moveTo(X-1-rotor,Y-1,pirate)
                            else:
                                rotor = int((name%per)/2)
                                return moveTo(X-1,Y-1-rotor,pirate)
    else:
        if pirate.getTeamSignal() != "" and (occupation == "hunter1" or occupation == 'hunter2' or occupation == 'hunter3' ):
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][2:])
            y = int(l[1])
            if occupation == 'hunter' + l[0][0]:
                return moveTo(x, y, pirate)
            else:
                if occupation == 'hunter1':
                    if a<b:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [wh1,wh1,1,1]
                        else:
                            weights = [1,1,wh1,wh1]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                    if b<a:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [1,1,wh1,wh1]
                        else:
                            weights = [wh1,wh1,1,1]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                    elif a==b and a<20:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [1,wh1,wh1,1]
                        else:
                            weights = [wh1,1,1,wh1]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                    else:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [wh1,1,1,wh1]
                        else:
                            weights = [1,wh1,wh1,1]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                elif occupation == 'hunter2':
                    if a<b:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [wh2,1,0,1]
                        else:
                            weights = [0,1,wh2,1]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                    if b<a:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [0,1,wh2,1]
                        else:
                            weights = [wh2,1,0,1]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                    elif a==b and a<20:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [0,1,wh2,1]
                        else:
                            weights = [wh2,1,0,1]   
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                    else:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [wh2,1,0,1]
                        else:
                            weights = [0,1,wh2,1]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                elif occupation == 'hunter3':
                    if a<b:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [1,wh3,1,0]
                        else:
                            weights = [1,0,1,wh3]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                    if b<a:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [1,0,1,wh3]
                        else:
                            weights = [1,wh3,1,0]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                    elif a==b and a<20:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [1,wh3,1,0]
                        else:
                            weights = [1,0,1,wh3]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                    else:
                        elements = [1, 2, 3, 4]
                        if ((count - 2*per - name)//per)%4 in [0,1]:
                            weights = [1,0,1,wh3]
                        else:
                            weights = [1,wh3,1,0]
                        random_integer = random.choices(elements, weights)[0]
                        return random_integer
                else:
                    random_integer = random.randint(1,4)
                    return random_integer
        elif occupation == 'hunter1':
            if a<b:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [wh1,wh1,1,1]
                else:
                    weights = [1,1,wh1,wh1]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            if b<a:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [1,1,wh1,wh1]
                else:
                    weights = [wh1,wh1,1,1]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            elif a==b and a<20:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [1,wh1,wh1,1]
                else:
                    weights = [wh1,1,1,wh1]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            else:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [wh1,1,1,wh1]
                else:
                    weights = [1,wh1,wh1,1]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
        elif occupation == 'hunter2':
            if a<b:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [wh2,1,0,1]
                else:
                    weights = [0,1,wh2,1]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            if b<a:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [0,1,wh2,1]
                else:
                    weights = [wh2,1,0,1]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            elif a==b and a<20:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [0,1,wh2,1]
                else:
                    weights = [wh2,1,0,1]   
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            else:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [wh2,1,0,1]
                else:
                    weights = [0,1,wh2,1]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
        elif occupation == 'hunter3':
            if a<b:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [1,wh3,1,0]
                else:
                    weights = [1,0,1,wh3]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            if b<a:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [1,0,1,wh3]
                else:
                    weights = [1,wh3,1,0]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            elif a==b and a<20:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [1,wh3,1,0]
                else:
                    weights = [1,0,1,wh3]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            else:
                elements = [1, 2, 3, 4]
                if ((count - 2*per - name)//per)%4 in [0,1]:
                    weights = [1,0,1,wh3]
                else:
                    weights = [1,wh3,1,0]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
        elif occupation == 'gatherer1':
            if a<b:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [0,wgb,wgd,wga]
                else:
                    weights = [wgd,wgr,0,0]
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            if b<a:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgd,wga,0,wgb]
                else:
                    weights = [0,0,wgd,wgr]                  
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            elif a==b and a<20:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgd,wgb,0,wga]
                else:
                    weights = [0,wgr,wgd,0]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            else:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [0,wga,wgd,wgb]
                else:
                    weights = [wgd,0,0,wgr]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
        elif occupation == 'gatherer2':
            if a<b:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgb,0,wga,wgd]
                else:
                    weights = [wgr,wgd,0,0]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            if b<a:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wga,wgd,wgb,0]
                else:
                    weights = [0,0,wgr,wgd]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            elif a==b and a<20:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wga,0,wgb,wgd]
                else:
                    weights = [0,wgd,wgr,0]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            else:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgb,wgd,0,wga]
                else:
                    weights = [wgr,0,0,wgd]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
        elif occupation == 'gatherer3' :
            if a<b:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [0,wgz,wgw,wgy]
                else:
                    weights = [wgw,wgx,0,0]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            if b<a:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgw,wgy,0,wgz]
                else:
                    weights = [0,0,wgw,wgx]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            elif a==b and a<20:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgw,wgz,0,wgy]
                else:
                    weights = [0,wgx,wgw,0]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            else:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [0,wgy,wgw,wgz]
                else:
                    weights = [wgw,0,0,wgx]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
        elif occupation == 'gatherer4':
            if a<b:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgz,0,wgy,wgw]
                else:
                    weights = [wgx,wgw,0,0]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            if b<a:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgy,wgw,wgz,0]
                else:
                    weights = [0,0,wgx,wgw]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            elif a==b and a<20:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgy,0,wgz,wgw]
                else:
                    weights = [0,wgw,wgx,0]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
            else:
                elements = [1, 2, 3, 4]
                if count < count1:
                    weights = [wgz,wgw,wgy,0]
                else:
                    weights = [wgx,0,0,wgw]
                    
                random_integer = random.choices(elements, weights)[0]
                return random_integer
        else:
            random_integer = random.randint(1,4)
            return random_integer
        
    



def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    if s:
        island_no = int(s[1])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")