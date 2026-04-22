import unittest
import sys
import os

# 1. Climb up to find the src/ folder so it can import the engine
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, "../src"))
if src_dir not in sys.path:
    sys.path.append(src_dir)

from risk_engine import calculate_risk_score

class TestRiskEngine(unittest.TestCase):
    
    def test_zero_reports(self):
        #Case 1: Zero reports, should output 0.0
        score = calculate_risk_score(reports_48h=0, total_severity=0, traffic_multiplier=1.0)
        self.assertEqual(score, 0.0)
        
    def test_single_low_severity(self):
        #Case 2: Single low-severity report
        #Math: (1/1 avg severity + 1 * 1.2 volume penalty) * 1.0 multiplier = 2.2
        
        score = calculate_risk_score(reports_48h=1, total_severity=1, traffic_multiplier=1.0)
        self.assertAlmostEqual(score, 2.2)
        
    def test_clustered_high_severity_escalation(self):
        #Case 3: Clustered high-severity triggering escalation (> 10.0)
        #3 reports, total severity 15 (avg 5). Multiplier 1.5.
        #Math: (5 avg severity + 3.6 volume penalty) * 1.5 multiplier = 12.9
        
        score = calculate_risk_score(reports_48h=3, total_severity=15, traffic_multiplier=1.5)
        self.assertGreater(score, 10.0) # Proves it triggers escalation
        self.assertAlmostEqual(score, 12.9) # Proves the math is exact
        
    def test_boundary_exactly_ten(self):
        #Case 4: A boundary case hitting exactly 10.0
        #5 reports, total severity 20 (avg 4). Multiplier 1.0.
        #Math: (4 avg severity + 6.0 volume penalty) * 1.0 multiplier = 10.0
        
        score = calculate_risk_score(reports_48h=5, total_severity=20, traffic_multiplier=1.0)
        self.assertEqual(score, 10.0)

if __name__ == '__main__':
    unittest.main()
