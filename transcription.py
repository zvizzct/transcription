import whisper
import youtube_dl
import os


# Ask the user to enter the YouTube video URL
video_url = input("Please enter the YouTube video URL to transcribe: ")

# check if audio.mp3 exists in the audio directory, and if it does, remove it

if os.path.exists("audio/my_audio.mp3"):
    os.remove("audio/my_audio.mp3")
    
# Create results if not exist
if not os.path.exists("results"):
    os.makedirs("results")

# download the audio from the YouTube link
ydl_opts = {
    "format": "bestaudio/worst",
    "outtmpl": f"audio/my_audio.mp3",
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    # Download the video and extract its title
    video_info = ydl.extract_info(video_url, download=True)
    video_title = video_info["title"]
    ydl_opts["outtmpl"] = ydl_opts["outtmpl"].format(video_title=video_title)


# load the Whisper model and transcribe the audio file
model = whisper.load_model("small")
result = model.transcribe("audio/my_audio.mp3")

# Use the video title as the file name when saving the result
with open(os.path.join("results", f"{video_title}.txt"), "w") as file:
    file.write(result["text"])