import pyodbc
from constants import constr, fields

class BaseApi:
    connect = pyodbc.connect(constr)
    cursor = connect.cursor()
    table = ''

    def __init__(self, table):
        self.table = table
        self.fields = fields[table]

    def open_connaction(self):
        self.connect = pyodbc.connect(constr)
        self.cursor = self.connect.cursor()

    def close_connection(self, connection, connection_cursor):
        connection_cursor.close()
        connection.close()

    def parse_data (self, data):
        parsed_data = []
        keys = []
        for field in fields[self.table]:
            keys.append(field['column'])
        for team in data:
            team = list(team[1:])
            parsed_team = {}
            for index in range(len(team)):
                parsed_team[keys[index]] = team[index]
            parsed_data.append(parsed_team)
        return parsed_data

    def get_all_data(self):
        try:
            action = "SELECT * FROM %s" % self.table
            self.cursor.execute(action)
            result = self.cursor.fetchall()
            self.close_connection(self.connect, self.cursor)
            return self.parse_data(result)
        except pyodbc.ProgrammingError as error:
            print('Таблица базы не найдена')
            print(error)
            self.close_connection(self.connect, self.cursor)

    def add_record (self, record):
        fields_values = ', '.join('\'{}\''.format(str(field)) for field in record.values())
        fields_keys = ', '.join(str(field) for field in record.keys())
        action = 'INSERT INTO {} ({}) VALUES ({});'.format(self.table, fields_keys, fields_values)
        print(action)
        self.cursor.execute(action)
        self.connect.commit()

    def set_roster (self, headers, roster):
        for player in roster:
            headers_value = ', '.join('{}'.format(str(field)) for field in headers)
            player_value = ', '.join('\'{}\''.format(str(field).replace("'", '\"')) for field in player)
            action = 'INSERT INTO players ({}) VALUES ({})'.format(headers_value, player_value)
            print(action)
            self.cursor.execute(action)
            self.connect.commit()

