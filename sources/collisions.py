# detect collisions of two different rectangles
def iscollision(AposX, AposY, AsizeX, AsizeY, BposX, BposY, BsizeX, BsizeY):
    if ((AposX + AsizeX <= BposX + BsizeX
         and AposX + AsizeX >= BposX)
        or
        (AposX <= BposX + BsizeX
         and AposX + AsizeX >=  BposX ))\
    \
        and ((AposY + AsizeY <= BposY + BsizeY
              and AposY + AsizeY > BposY)
             or
             (AposY <= BposY + BsizeY
              and AposY > BposY)):
        return True
    else:
        return False
