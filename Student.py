from bson.objectid import ObjectId
from Candidate import Candidate

class Student(object):
    def __init__(self, db):
        self.db = db
        return

    def InsertStudent(self, data):
        data["voted"] = False
        self.db.InsertDocument("Student", data)
        return

    def UpdateStudent(self, inpID, data):
        self.db.UpdateDocument("Student", {"_id":inpID}, data)
        return

    def SetVote(self, inpID, isTrue):
        self.db.UpdateDocument("Student", {"_id":inpID}, {"voted":isTrue})
        return

    def Login(self, studentID, pw):
        target = self.db.GetDocument("Student", {"nim":studentID, "password":pw})
        if target is not None:
            return target
        else:
            None

    def Vote(self, inpID, candidate):
        voter = self.db.GetDocument("Student", {"_id":inpID})
        if (voter["voted"]):
            return
        else:
            self.db.UpdateDocument("Student", {"_id":inpID}, {"voted":True})
            c = Candidate(self.db)
            c.AddVote(candidate)
            return

