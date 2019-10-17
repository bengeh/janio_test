class ApprovalState(object):
    name = "state"
    allowed = []
    def switch(self, state):
        if (state.name == "PENDING" and "HOLD" in self.allowed) or state.name in self.allowed:
            print("switching state from: ", self, " to ", state.name)
            self.__class__ = state
        else:
            print("Switching from: ", self, " to ", state.name," is not possible..")

    def __str__(self):
        return self.name

class Approve(ApprovalState):
    name = "APPROVE"
    allowed = ["REJECT", "HOLD"]

class Reject(ApprovalState):
    name ="REJECT"
    allowed = ["HOLD"]

class Pending(ApprovalState):
    name = "PENDING"
    allowed = ["APPROVE", "REJECT"]

class MainClass(object):
    def __init__(self):
        self.state = Pending() #set initial state to pending
    def change(self, state):
        self.state.switch(state)

if __name__ == "__main__": #add more states here 
    isChangeState = MainClass()
    isChangeState.change(Approve)
    isChangeState.change(Pending)
    isChangeState.change(Reject)
    isChangeState.change(Approve) #shouldnt allow change of state as it is not possible
    isChangeState.change(Pending)
    isChangeState.change(Reject)
    isChangeState.change(Pending)


