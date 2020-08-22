from bson.objectid import ObjectId

class Candidate(object):
    def __init__(self, db):
        self.db = db
        return

    def InsertCandidate(self, candidateName):
        self.db.InsertDocument("Candidate", {"name": candidateName, "count": 0})
        return
    
    def AddVote(self, candidateName):
        target = self.db.GetDocument("Candidate", {"name": candidateName})
        target["count"] = target["count"] + 1
        self.db.UpdateDocument("Candidate", {"name": candidateName}, {"count": target["count"]})
        return

    def RemoveVote(self, candidateName):
        target = self.db.GetDocument("Candidate", {"name": candidateName})
        target["count"] = target["count"] - 1
        self.db.UpdateDocument("Candidate", {"name": candidateName}, {"count": target["count"]})
        return

