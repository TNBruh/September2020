from flask import Blueprint, request, Response

from Student import Student
from Candidate import Candidate
import FractalDatabase

from cryptography.fernet import Fernet

supermagnusmagnusthegreatkingofcomputerkey = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='

crypt = Fernet(supermagnusmagnusthegreatkingofcomputerkey)

controller = Blueprint("controller", __name__)

@controller.route("/login", methods=["POST"])
def login():
    if (request.method == "POST"):
        userM = Student(FractalDatabase.GetDB())
        data = request.get_json()
        result = userM.Login(data["nim"], data["password"])
        if result is not None:
            result["nim"] = crypt.encrypt(str(result["nim"]))
            return {"success":"true", "data":result}
        else:
            return {"success":"false", "data":""}

    return Response(response="invalid signature", status=400)


@controller.route("/vote", methods=["PUT"])
def vote():
    if (request.method == "PUT"):
        userM = Student(FractalDatabase.GetDB())
        data = request.get_json()
        decrypted = crypt.decrypt(data["nim"])
        voter = FractalDatabase.GetDB().GetDocument("Student", {"nim":decrypted})
        if (voter is not None):
            if (~voter["voted"]):
                userM.Vote(voter["_id"], data["candidate"])
            else:
                if (data["candidate2"] != "None"):
                    userM.Vote(voter["_id"], data["candidate"])
                    cM = Candidate(FractalDatabase.GetDB())
                    cM.RemoveVote(data["candidate2"])
            return {"success":"true"}

    return Response(response="invalid signature", status=400)



