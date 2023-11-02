import os

# this function is used to check whether a given filename has an allow file extension

# abc.jpg

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf','png','jpg','jpeg','gif'}


# this function is used to save an uploaded file to a specified directory if it has an allowed file extension

def save_uploaded_file(file):
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        return filename
    
    else:
        return None