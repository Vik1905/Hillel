import unittest
from homework_14 import TeamLead


class TestTeamLead(unittest.TestCase):
    def test_teamlead_attributes(self):
        team_lead = TeamLead("Alexandr", 5600, "Engineering", "Python", 7)

        self.assertEqual(team_lead.name, "Alexandr")
        self.assertEqual(team_lead.salary, 5600)
        self.assertEqual(team_lead.department, "Engineering")
        self.assertEqual(team_lead.programming_language, "Python")
        self.assertEqual(team_lead.team_size, 7)


if __name__ == '__main__':
    unittest.main()