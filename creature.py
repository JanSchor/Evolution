
class Creature:
    def __init__(self, pos, genes, stepAction, cId, numOfInternals):
        self.pos = pos
        self.genes = genes
        self.step = stepAction
        self.cId = cId

        self.internalNeurons = [1 for i in range(numOfInternals)] # changed, might throw some errors

        self.dead = False
        self.eliminated = False
        self.coat = False
        self.color = (255, 0, 0)
        self.facing = None
    
    def __str__(self):
        return "1"


    
