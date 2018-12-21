from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

reports = []
class Status:
    def __init__(self, status):
        self.status = 'pending'
    def changestatus(self):
        self.status = input("enter status: ")

class Comment:
    def __init__(self, comment):

        self.comment = 'no comment'
    def entercomment(self):
        self.status = input("enter comment: ")

class Incident:
    def __init__(self, status=[], comment=[]):
        self.status = status
        self.comment = comment

    def getdic(self):
        return{
            'status': self.status,
            'comment': self.comment

        }
    def createreport(self):
        report = {
            
            "status" :self.status,
            "comment" : self.comment
        }

        reports.append(report)
  
tempcomments = [Comment("this staff is hard")]
temp_status = [Status("not pending any more")]
incident = Incident(tempcomments, temp_status)

@app.route('/api/v1/tyr', methods=['POST'])
def create_report():
    user_data = request.get_json()
    status = user_data.get('status')
    comment = user_data.get ('comment')
    incident = Incident(status, comment)
    incident.createreport()

    return jsonify({'report':incident.getdic()})

if __name__ == '__main__':
    app.run(debug = True)



    



