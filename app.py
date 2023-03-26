from flask import Flask,render_template,request,send_file,url_for
from werkzeug.utils import secure_filename
from PIL import Image
from moviepy.video.io.VideoFileClip import VideoFileClip
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/more_options')
def more_options():
    return render_template('more_options.html')

@app.route("/webm_to_mp4",methods=["GET","POST"])
def webm_to_mp4():
    if request.method=="POST":
        f = request.files['file']
        file_name=secure_filename(f.filename)
        if file_name.split('.')[-1]=='webm':
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        else:
            return render_template('webm_to_mp4.html',ft="webm")
    return render_template('webm_to_mp4.html')

@app.route("/wav_to_mp3",methods=["GET","POST"])
def wav_to_mp3():
    if request.method=="POST":
        f = request.files['file']
        file_name=secure_filename(f.filename)
        if file_name.split('.')[-1]=='wav':
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        else:
            return render_template('webm_to_mp4.html',ft="wav")
    return render_template('wav_to_mp3.html')


##########################################################################
"""If you want to add any more also, do the same as done above in function webm_to_mp4
    if request.method=="POST":
        f = request.files['file']
        file_name=secure_filename(f.filename)
        if file_name.split('.')[-1]=='##':      #Here replace ## with file type that user will upload
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        else:
            return render_template('webm_to_mp4.html',ft="webm")    #replace the url as per requirement
    return render_template('webm_to_mp4.html')    #Replace here also
"""
##########################################################################

@app.route("/png_to_jpg",methods=["GET","POST"])
def png_to_jpg():
    if request.method=="POST":
        f = request.files['file']
        file_name=secure_filename(f.filename)
        if file_name.split('.')[-1]=='png':
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        else:
            return render_template('png_to_jpg.html',ft="png")

    return render_template('png_to_jpg.html')

@app.route("/webp_to_png",methods=["GET","POST"])
def webp_to_png():
    if request.method=="POST":
        f = request.files['file']
        file_name=secure_filename(f.filename)
        if file_name.split('.')[-1]=='webp':
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        else:
            return render_template('webp_to_png.html',ft="webp")

    return render_template('webp_to_png.html')

@app.route("/webp_to_jpg",methods=["GET","POST"])
def webp_to_jpg():
    if request.method=="POST":
        f = request.files['file']
        file_name=secure_filename(f.filename)
        if file_name.split('.')[-1]=='webp':
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        else:
            return render_template('webp_to_jpg.html',ft="webp")

    return render_template('webp_to_jpg.html')

@app.route('/downl/<id>')
def downl(id):
    print(id)
    file_name=id.split("&&")[1]
    type_conversion=id.split("&&")[0]
    if type_conversion=="png_to_jpg":
        try:
            img_fmt1 = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            if img_fmt1.mode != 'RGB':
                img_fmt1 = img_fmt1.convert('RGB')
            img_fmt1.save("converts/"+file_name.replace('.png','.jpg'))
            return send_file('converts/'+file_name.replace('.png','.jpg'), as_attachment=True) 
        except:
            return render_template('png_to_jpg.html',error='cant_convert')
    elif type_conversion=="webm_to_mp4":
        try:
            clip = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            video = VideoFileClip(clip)
            output_file = file_name.replace('.webm','.mp4')
            video.write_videofile('converts/'+output_file, codec="libx264")
            print("HELOO")
            return send_file('converts/'+file_name.replace('.webm','.mp4'), as_attachment=True)
        except:
            return render_template('png_to_jpg.html',error='cant_convert')
    
    elif type_conversion=="webp_to_png":
        try:
            img=Image.open(os.path.join(app.config['UPLOAD_FOLDER'], file_name)).convert('RGB')
            img.save("converts/"+file_name.replace('.webp','.png'),"png")
            print('converts/'+file_name.replace('.webp','.png'))
            return send_file('converts/'+file_name.replace('.webp','.png'), as_attachment=True, mimetype='image/png')
        except:
            return render_template('webp_to_png.html',error='cant_convert')

    elif type_conversion=="webp_to_jpg":
        try:
            img=Image.open(os.path.join(app.config['UPLOAD_FOLDER'], file_name)).convert('RGB')
            img.save("converts/"+file_name.replace('.webp','.jpg'),"jpeg")
            return send_file('converts/'+file_name.replace('.webp','.jpg'), as_attachment=True) 
        except:
            return render_template('webp_to_jpg.html',error='cant_convert')
    
    else:
        return render_template('index.html')

    
if __name__ == '__main__':
    app.run()
