pacific_division = [ 'LAL', 'LAC', 'SAC', 'GSW', 'PHX' ]

database = 'nba_database.accdb'
path = 'D:/Универ/Управление базами данных/Лабораторная 1'
constr = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=%s\%s;'
    ) % (path, database)

fields = {
    'teams': (
        {'column': 'id', 'type': 'NUMERIC'},
        {'column': 'full_name', 'type': 'VARCHAR(255)'},
        {'column': 'abbreviation', 'type': 'VARCHAR(25)'},
        {'column': 'nickname', 'type': 'VARCHAR(255)'},
        {'column': 'city', 'type': 'VARCHAR(255)'},
        {'column': 'state', 'type': 'VARCHAR(255)'},
        {'column': 'year_founded', 'type': 'INTEGER'},
    ),
    'players': (
        {'column': 'id', 'type': 'NUMERIC'},
        {'column': 'full_name', 'type': 'VARCHAR(255)'},
        {'column': 'last_Name', 'type': 'VARCHAR(255)'},
    )
}
TEAMS_TABLE_FIELDS = (
    'id',
    'full_name',
    'abbreviation',
    'nickname',
    'city',
    'state',
    'year_founded'
)