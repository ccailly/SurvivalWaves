import j2l.pytactx.agent as pytactx


class arme(pytactx.Agent):

    def __init__(self, x, y, pv_rendu):
        super.__init__()
        self.life = 1
        self.x  = x
        self.y = y
        self.pv_rendu = pv_rendu


