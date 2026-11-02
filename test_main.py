import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from main import monitor
class StudyTests(unittest.TestCase):
 def test_queries(self):
  s=monitor([{'participant_id':'S1','visit_name':'V1','completed_date':''}],[])
  self.assertEqual(len(s['queries']),1)
 def test_empty(self):self.assertEqual(monitor([],[])['completion_rate_pct'],0)
