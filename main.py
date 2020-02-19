from packages import *
from constants import *
from base_actions import BaseApi


def build_division(division):
    rosters = []
    for team in division:
        rosters.append(teams.find_team_by_abbreviation(team))
    return rosters


build_division(pacific_division)


# TeamsBaseApi = BaseApi('teams')
# print(TeamsBaseApi.get_all_data())

class Main:
    def __init__(self):
        self.TeamsApi = BaseApi('teams')
        self.PlayersApi = BaseApi('players')
        self.players = []

    def get_division(self, division):
        for team in division:
            self.TeamsApi.add_record(teams.find_team_by_abbreviation(team))

    def get_roster(self):
        teams_list = self.TeamsApi.get_all_data()
        self.PlayersApi.open_connaction()
        for team in teams_list:
            team_info = api.commonteamroster.CommonTeamRoster(season='2019-20', team_id=team['id'])
            response = team_info.common_team_roster.get_dict()
            self.PlayersApi.set_roster(response['headers'], response['data'])


App = Main()
# App.get_division(pacific_division)
# App.get_roster()
