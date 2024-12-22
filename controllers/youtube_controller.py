from flask import Blueprint, request
from services.youtube_transcript_service import get_transcript
from utils.response_handler import success_response, error_response

youtube_blueprint = Blueprint("youtube", __name__)

@youtube_blueprint.route("/transcript", methods=["POST"])
def transcript():
    try:
        data = request.get_json()
        video_url = data.get("video_url", None)
        languages = data.get("languages", ['tr'])  # Kullanıcı tarafından istenen diller

        if not video_url:
            return error_response("Video URL is required", 400)

        transcript_data = get_transcript(video_url, languages=languages)
        if "error" in transcript_data:
            return error_response(transcript_data["error"], 404, additional_data=transcript_data)

        return success_response(transcript_data)
    except Exception as e:
        return error_response(str(e), 500)
    
@youtube_blueprint.route("/")
def helloworld():
    return "Hello World!"