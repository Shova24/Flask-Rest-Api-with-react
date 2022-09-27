from flask import Flask
from flask_restful import Api, Resource , reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

# args = video_put_args.parse_args()
# print (args)

# names = {   "shova": {"age": 24, "gender": "female"},
#             "niha": {"age": 19, "gender": "male"}
#             }
videos = {}



#     class Videos(Resource):
#         def get(self, video_id):
#             return videos[video_id]
#         def put(self, video_id):
#             args = video_put_args.parse_args()
#             return {video_id : 1}


# api.add_resource(Video, "/video/<int:video_id>")

# class HelloWorld(Resource):
#     def get(self,name):
#         return names[name]

#     def post(self): 
#         return {"data": "posted"}

# api.add_resource(HelloWorld, '/helloworld/<string:name>')

# videos = {
#     1 : "Data 1",
#     2 : "Data 2"
#  }

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video id is not valid...")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID...")

class Videos(Resource):
    def get(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id],200
    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id],201
    def delete(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204



api.add_resource(Videos,'/videos/<int:video_id>')


if __name__ == "__main__": 
    app.run(debug=True)
