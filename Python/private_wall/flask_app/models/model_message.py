from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import session
from flask_app.models import model_message, model_user

class Message:
    def __init__( self , data ):
        self.id = data['id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.recepient_id = data['recepient_id']
        self.counter = []
    
    @classmethod
    def get_messages_for_user(cls, data):
        query = "SELECT * FROM messages JOIN users ON sender_id = users.id WHERE recepient_id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        messages = []

        if results:
            for item in results:
                user_data = {
                    'id': item['users.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'email': item['email'],
                    'password': item['password'],
                    'created_at': item['users.created_at'],
                    'updated_at': item['users.updated_at']
                }
                temp_message = model_message.Message(item)
                temp_message.sender = model_user.User(user_data)
                messages.append(temp_message)

        return messages

    @classmethod
    def get_message_count(cls, data):
        query = "SELECT *, count(*) AS message_count FROM messages JOIN users ON sender_id = users.id WHERE recepient_id = %(id)s GROUP BY recepient_id;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            return results[0]['message_count']

        return 0

    @classmethod
    def send_message_to_user(cls, data):
        query = "INSERT INTO messages (message, recepient_id, sender_id) VALUES (%(message)s, %(recepient)s, %(id)s);"
        session['sent_counter'] += 1
        print(session['sent_counter'])
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)