def save_upload_picture(picture):
    """
    func for saving picture when uploading
    :param picture: file to be uploaded
    :return: None if wrong type file, otherwise path of uploaded picture in uploads folder
    """
    # checking file extension
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ['jpeg', 'jpg', 'bmp', 'svg']:
        return
    # saving picture
    picture.save(f'./uploads/{filename}')
    return f'uploads/{filename}'
