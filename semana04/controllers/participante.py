from flask_restful import Resource

class ParticipanteController(Resource):
    # esta clase se comportara como si fuese un controlador, es decir que si definimos un metodo llamado get
    def get(self):
         return {
            'message': 'Ingreso al get'
            }
        