from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    """
    Extract video ID from YouTube URL.
    """
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    elif query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query).get('v', [None])[0]
    return None

def get_transcript(video_url, languages=['tr']):
    """
    Fetch transcript using YouTube API for the requested languages.
    Tries to get the transcript in the specified languages, otherwise defaults to available options.
    """
    video_id = get_video_id(video_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")

    try:
        # Kullanıcının belirttiği dillerden transkripti döndür
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    except NoTranscriptFound:
        # Belirtilen dilde transkript bulunamazsa, videonun desteklediği dilleri döndür
        available_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        return {
            "error": f"Transcript not available in {languages}.",
            "available_languages": available_transcripts._manually_created_transcripts.keys()
        }
    except TranscriptsDisabled:
        # Eğer videoda transkriptler devre dışıysa hata döndür
        return {"error": "Transcripts are disabled for this video."}

    return transcript