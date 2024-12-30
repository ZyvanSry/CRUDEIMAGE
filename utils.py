import os
import uuid

def upload_image(sourcefile=None):
    if sourcefile is not None:
        upload_dir = "static/uploads"

        _, ext = os.path.splitext(sourcefile.filename)

        safe_file_name = str(uuid.uuid1()) + ext

        sourcefile.save( os.path.join(upload_dir, safe_file_name) )

        return safe_file_name