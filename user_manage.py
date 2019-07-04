from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
import psycopg2


class Users:
    def __init__(self,DATABASE_URL):
        self.DBURL = DATABASE_URL
        self.info = None
        self.conn = None
    def _startConn(self, databaseURI = None):
        """
        Start connection with PostgresDB and store it in self.conn
        """
        conn = psycopg2.connect(self.DBURL, sslmode='require')
        self.conn = conn
    def QueryUser(self, user):
        if not self.conn:
            self.__startConn()

class InsertUsers(Users):
    """
    Class for users managment.
    createUser to insert new user into the DB
    """
    def __init__(self, DBURL):
        super().__init__(DBURL)
    def __check_info(self):
        """
        Double check user info before submit to the cloud
        """
        if self.info:
            print("Información del usuario:")
            print(self.info)
            ans = input("¿Estas seguro que deseas agregar al usuario a la base? (S/N)")
            if ans.lower() == 's' or ans.lower() == 'si' or ans.lower() == 'yes':
                return True
            else:
                return False
    def __check_duplicate_email(self):
        """
        Prevent email from being duplicate in the DB.
        """
        if not self.conn:
            self._startConn()
        conn = self.conn.cursor()
        conn.execute("SELECT email FROM Users;")
        users = conn.fetchall()
        return self.info['email'] not in list(map(lambda x: x[0],users))

    def __insertUser(self):
        #email varchar, name varchar, lastName varchar, password varchar, date varchar
        if not self.conn:
            self.__startConn()
        self.conn.cursor().execute(
            """
            INSERT INTO Users (email, name, lastname, password, date) VALUES (%s, %s, %s, %s, %s)
            """,
            tuple(new.info.values())
        )
        self.conn.commit()

    def createUser(self,email, nombre, apellido, password):
        """
        insert new user into the DB.
        all vars are str. email must contain @.
        """
        assert "@" in email, "Por favor introduce un email válido"
        self.info = {
            'email':email,
            'nombre':nombre,
            'apellido':apellido,
            'hash_pass': generate_password_hash(password),
            'fecha': format(datetime.today(),"%Y-%m-%d %H:%M")
        }
        assert self.__check_duplicate_email(), "El email existe ya en la base"
        assert self.__check_info(), "Operación cancelada manualmente"
        self.__insertUser()

class ValidateUsers(Users):
    """
    Given a user and password, validate pwd.
    """
    def __init__(self, DBURL, user, password):
        super().__init__(DBURL)
        self.info = {
            'user':user,
            'password': password
        }
    def __check_password(self):
        """
        True if pwd is the same as in our DB else False.
        """
        if not self.conn:
            self._startConn()
        cur = self.conn.cursor()
        cur.execute(f"SELECT password FROM Users WHERE email = '{self.info['user']}';")
        pwd = cur.fetchone()
        if pwd:
            return check_password_hash(pwd[0], self.info['password'])
        else:
            return False
            # assert False, "Usuario inexistente"


    def Validate(self):
        """
        Assert if user has acces else break
        """
        assert self.__check_password(), "Contraseña Inválida"
        return "¡¡¡¡Acceso Concedido!!!!"

if __name__ == "__main__":
    #createUser(DBURL,self,email, nombre, apellido, password)
    print("Proceso para insertar un nuevo usuario: ")
    email = input('Escribe el email a agregar: ')
    nombre = input('Escribe el nomre a agregar: ')
    apellido = input('Escribe el apellido a agregar: ')
    pswd = input('Escribe el password a agregar: ')
    DBURL = input("Pega el URL de la BD: ")
    new = InsertUsers(DBURL)
    new.createUser(email, nombre, apellido, pswd)
