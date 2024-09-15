## Folder Structure

``````
└───Meeting
│
└───PilotData
│
└───RawData

``````


- Meeting records the meeting minutes, and named as the date of the meeting.


- PilotData contains two subjects, one is collected at NNU, and one is collected at SJTU. 
  - sub-001 has enumerous bad electrodes; 
  - sub-002 hadn't recorded the marker for error port.



- RawData contains six subjects collected at SJTU, which can be download from [here](https://gofile.me/6V7fC/08WYfdHOj)


|sub|exp1|exp2|exp3|shuffled|
|:---:|:---:|:---:|:---:|:---:|
|sub-001|background square, no square marker|white instruction, 8 blocks|white instruction, 5 blocks|no|
|sub-002|background square, no square marker|white instruction, 8 blocks|white instruction, 5 blocks|no|
|sub-003|background square, no square marker|white instruction, 8 blocks|white instruction, 5 blocks|no|
|sub-004|fixation square, no square marker|white instruction, 8 blocks|white instruction, 5 blocks|no|
|sub-005|fixation square, error square marker|grey instruction, 6 blocks|grey instruction, 5 blocks|no|
|sub-006|fixation square, correct square marker|grey instruction, 6 blocks|grey instruction, 5 blocks|yes|

hcp: where is the scipt that converting raw data into BIDS? has the BIDS format been validated?