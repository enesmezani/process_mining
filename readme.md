Heuristic

DataFrame:
     Case_ID               Activity   Resource           Timestamp        Status
0   Case_001          Ticket Review  Developer 2024-12-18 09:00:00     Completed
1   Case_001  Clarification Meeting  Team Lead 2024-12-18 10:00:00     Completed
2   Case_001  Start Working on Task  Developer 2024-12-18 11:00:00     Completed
3   Case_001   Runs Automated Tests  Developer 2024-12-18 13:00:00        Passed
4   Case_001   Creates Pull Request  Developer 2024-12-18 13:30:00     Completed
5   Case_001             QA Testing         QA 2024-12-18 14:00:00      Approved
6   Case_001            Code Review  Team Lead 2024-12-18 15:00:00      Approved
7   Case_001     Merge Pull Request  Team Lead 2024-12-18 15:30:00     Completed
8   Case_002          Ticket Review  Developer 2024-12-18 09:30:00     Completed
9   Case_002  Start Working on Task  Developer 2024-12-18 10:00:00     Completed
10  Case_002   Runs Automated Tests  Developer 2024-12-18 12:00:00        Failed
11  Case_002             Fix Issues  Developer 2024-12-18 12:30:00     Completed
12  Case_002   Runs Automated Tests  Developer 2024-12-18 13:00:00        Passed
13  Case_002   Creates Pull Request  Developer 2024-12-18 13:30:00     Completed
14  Case_002             QA Testing         QA 2024-12-18 14:30:00  Issues Found
15  Case_002             Fix Issues  Developer 2024-12-18 15:00:00     Completed
16  Case_002             QA Testing         QA 2024-12-18 15:30:00      Approved
17  Case_002            Code Review  Team Lead 2024-12-18 16:00:00      Approved
18  Case_002     Merge Pull Request  Team Lead 2024-12-18 16:30:00     Completed
19  Case_003          Ticket Review  Developer 2024-12-18 10:00:00     Completed
20  Case_003  Start Working on Task  Developer 2024-12-18 10:30:00     Completed
21  Case_003   Runs Automated Tests  Developer 2024-12-18 12:00:00        Passed
22  Case_003   Creates Pull Request  Developer 2024-12-18 12:30:00     Completed
23  Case_003             QA Testing         QA 2024-12-18 13:00:00  Issues Found
24  Case_003             Fix Issues  Developer 2024-12-18 14:00:00     Completed
25  Case_003             QA Testing         QA 2024-12-18 15:00:00  Issues Found
26  Case_003             Fix Issues  Developer 2024-12-18 16:00:00     Completed
27  Case_003             QA Testing         QA 2024-12-18 17:00:00      Approved
28  Case_003            Code Review  Team Lead 2024-12-18 17:30:00      Approved
29  Case_003     Merge Pull Request  Team Lead 2024-12-18 18:00:00     Completed
30  Case_004          Ticket Review  Developer 2024-12-18 10:00:00     Completed
31  Case_004  Start Working on Task  Developer 2024-12-18 11:00:00     Completed
32  Case_004   Runs Automated Tests  Developer 2024-12-18 13:00:00        Passed
33  Case_004   Creates Pull Request  Developer 2024-12-18 13:30:00     Completed
34  Case_004             QA Testing         QA 2024-12-18 14:00:00      Approved
35  Case_004            Code Review  Team Lead 2024-12-18 15:00:00  Issues Found
36  Case_004             Fix Issues  Developer 2024-12-18 16:00:00     Completed
37  Case_004   Creates Pull Request  Developer 2024-12-18 16:30:00     Completed
38  Case_004             QA Testing         QA 2024-12-18 16:50:00      Approved
39  Case_004            Code Review  Team Lead 2024-12-18 17:20:00      Approved
40  Case_004     Merge Pull Request  Team Lead 2024-12-18 17:30:00     Completed
Log Summary:
Total number of cases: 4
Total number of events: 41
Activity distribution:
Activity
QA Testing               8
Fix Issues               5
Creates Pull Request     5
Code Review              5
Runs Automated Tests     5
Ticket Review            4
Start Working on Task    4
Merge Pull Request       4
Clarification Meeting    1
Name: count, dtype: Int64

Heuristic net created successfully.
Heuristic net visualization saved as heuristic.png

Alphaminer

DataFrame:
     Case_ID               Activity   Resource           Timestamp        Status
0   Case_001          Ticket Review  Developer 2024-12-18 09:00:00     Completed
1   Case_001  Clarification Meeting  Team Lead 2024-12-18 10:00:00     Completed
2   Case_001  Start Working on Task  Developer 2024-12-18 11:00:00     Completed
3   Case_001   Runs Automated Tests  Developer 2024-12-18 13:00:00        Passed
4   Case_001   Creates Pull Request  Developer 2024-12-18 13:30:00     Completed
5   Case_001             QA Testing         QA 2024-12-18 14:00:00      Approved
6   Case_001            Code Review  Team Lead 2024-12-18 15:00:00      Approved
7   Case_001     Merge Pull Request  Team Lead 2024-12-18 15:30:00     Completed
8   Case_002          Ticket Review  Developer 2024-12-18 09:30:00     Completed
9   Case_002  Start Working on Task  Developer 2024-12-18 10:00:00     Completed
10  Case_002   Runs Automated Tests  Developer 2024-12-18 12:00:00        Failed
11  Case_002             Fix Issues  Developer 2024-12-18 12:30:00     Completed
12  Case_002   Runs Automated Tests  Developer 2024-12-18 13:00:00        Passed
13  Case_002   Creates Pull Request  Developer 2024-12-18 13:30:00     Completed
14  Case_002             QA Testing         QA 2024-12-18 14:30:00  Issues Found
15  Case_002             Fix Issues  Developer 2024-12-18 15:00:00     Completed
16  Case_002             QA Testing         QA 2024-12-18 15:30:00      Approved
17  Case_002            Code Review  Team Lead 2024-12-18 16:00:00      Approved
18  Case_002     Merge Pull Request  Team Lead 2024-12-18 16:30:00     Completed
19  Case_003          Ticket Review  Developer 2024-12-18 10:00:00     Completed
20  Case_003  Start Working on Task  Developer 2024-12-18 10:30:00     Completed
21  Case_003   Runs Automated Tests  Developer 2024-12-18 12:00:00        Passed
22  Case_003   Creates Pull Request  Developer 2024-12-18 12:30:00     Completed
23  Case_003             QA Testing         QA 2024-12-18 13:00:00  Issues Found
24  Case_003             Fix Issues  Developer 2024-12-18 14:00:00     Completed
25  Case_003             QA Testing         QA 2024-12-18 15:00:00  Issues Found
26  Case_003             Fix Issues  Developer 2024-12-18 16:00:00     Completed
27  Case_003             QA Testing         QA 2024-12-18 17:00:00      Approved
28  Case_003            Code Review  Team Lead 2024-12-18 17:30:00      Approved
29  Case_003     Merge Pull Request  Team Lead 2024-12-18 18:00:00     Completed
30  Case_004          Ticket Review  Developer 2024-12-18 10:00:00     Completed
31  Case_004  Start Working on Task  Developer 2024-12-18 11:00:00     Completed
32  Case_004   Runs Automated Tests  Developer 2024-12-18 13:00:00        Passed
33  Case_004   Creates Pull Request  Developer 2024-12-18 13:30:00     Completed
34  Case_004             QA Testing         QA 2024-12-18 14:00:00      Approved
35  Case_004            Code Review  Team Lead 2024-12-18 15:00:00  Issues Found
36  Case_004             Fix Issues  Developer 2024-12-18 16:00:00     Completed
37  Case_004   Creates Pull Request  Developer 2024-12-18 16:30:00     Completed
38  Case_004             QA Testing         QA 2024-12-18 16:50:00      Approved
39  Case_004            Code Review  Team Lead 2024-12-18 17:20:00      Approved
40  Case_004     Merge Pull Request  Team Lead 2024-12-18 17:30:00     Completed
Alpha Miner applied successfully.
Petri net visualization saved as alpha_miner_petri_net.png