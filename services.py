from utils import upload_image
from repository import get_db_con as dc


def createPost(form, file) -> None:
    name = form['name']
    sourcefile = file['thumbnail']
    filename = upload_image(sourcefile=sourcefile)
    des = form['description']
    query= f" INSERT INTO `products`(`name`,`thumbnail`,`description`) VALUES ('{name}' ,'{filename}' , '{des}')"
    con = dc()
    cursor = con.cursor()
    cursor.execute(query=query)
    con.commit()

def getAllProducts() -> list:
    con = dc()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM `products` ORDER BY `id` DESC")
    products = cursor.fetchall()
    return products


def get_one_product_by_id(id):
    con = dc()
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM `products` WHERE id = {id}")
    product = cursor.fetchall()[0]
    return product

    


def update(form, file, id) -> None:
    con = dc()
    name = form['name']
    
    sourcefile = file['thumbnail']
    if sourcefile:
        filename = upload_image(sourcefile=sourcefile)
    else:
        filename = form['old-thumbnail']
        
    des = form['description']

    query = f"""
        UPDATE `products` SET `name` = '{name}', `thumbnail` = '{filename}', `description` = '{des}'
        WHERE `id` = {id}
    """

    cursor = con.cursor()
    cursor.execute(query=query)
    con.commit()
