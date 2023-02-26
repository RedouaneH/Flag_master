class color:

    def __init__(self):
        self.cpt=75
        self.back=0
        self.slow=0

    def update(self):
        self.slow+=1
        self.slow=self.slow%10

        if self.cpt == 110:
            self.back = 1
        if self.cpt == 75:
            self.back = 0

        if self.slow%5==0:
            if self.back:
                self.cpt-=1
            else:
                self.cpt+=1

    def get(self):
        return self.cpt