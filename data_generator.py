import csv
import random

columns = ['crop_id',
            'Soil Type',
            'jan_temp',
            'feb_temp',
            'mar_temp',
            'apr_temp',
            'may_temp',
            'jun_temp',
            'jul_temp',
            'aug_temp',
            'sep_temp',
            'oct_temp',
            'nov_temp',
            'dec_temp',
            'jan_rain',
            'feb_rain',
            'mar_rain',
            'apr_rain',
            'may_rain',
            'jun_rain',
            'jul_rain',
            'aug_rain',
            'sep_rain',
            'oct_rain',
            'nov_rain',
            'dec_rain',
            'jan_sunshine',
            'feb_sunshine',
            'mar_sunshine',
            'apr_sunshine',
            'may_sunshine',
            'jun_sunshine',
            'jul_sunshine',
            'aug_sunshine',
            'sep_sunshine',
            'oct_sunshine',
            'nov_sunshine',
            'dec_sunshine',]

crops = {1: 'WH147',
        2: 0, 
        3: 0, 
        4: 0, 
        5: 0, 
        6: 0, 
        7: 0, 
        8: 0, 
        9: 0, 
        10: 0, 
        11: 0, 
        12: 0, 
        13: 0, 
        14: 0, 
        15: 0, 
        16: 0, 
        17: 0, 
        18: 0, 
        19: 0, 
        20: 0}

def make_trainset_crop_id_1():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.normalvariate(23, 1.7),
                # feb
                columns[3]: random.normalvariate(24, 1.7),
                # mar
                columns[4]: random.normalvariate(25, 1.7),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.normalvariate(22, 1.5),
                # dec
                columns[13]: random.normalvariate(22, 1.6),
                # rainfall
                # jan
                columns[14]: random.normalvariate(25, 1.4),
                # feb
                columns[15]: random.normalvariate(25, 1.4),
                # mar
                columns[16]: random.normalvariate(25, 1.4),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.normalvariate(29, 5),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_2():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_3():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_4():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_5():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_6():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_7():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_8():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_9():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_10():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_11():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_12():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_13():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_14():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_15():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_16():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_17():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_18():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_19():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_20():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

def make_trainset_crop_id_21():
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        rows = 1000
        for i in range(rows):
            writer.writerow({columns[0]: 1, columns[1]: 'black_soil',
                # average temperature
                # jan
                columns[2]: random.randrange(1, 40),
                # feb
                columns[3]: random.randrange(1, 40),
                # mar
                columns[4]: random.randrange(10, 45),
                # apr
                columns[5]: random.randrange(20, 50),
                # may
                columns[6]: random.randrange(20, 50),
                # jun
                columns[7]: random.randrange(20, 30),
                # jul
                columns[8]: random.randrange(20, 30),
                # aug
                columns[9]: random.randrange(20, 30),
                # sep
                columns[10]: random.randrange(20, 30),
                # oct
                columns[11]: random.randrange(20, 30),
                # nov
                columns[12]: random.randrange(20, 30),
                # dec
                columns[13]: random.randrange(1, 40),
                # rainfall
                # jan
                columns[14]: random.randrange(0, 500),
                # feb
                columns[15]: random.randrange(0, 500),
                # mar
                columns[16]: random.randrange(0, 500),
                # apr
                columns[17]: random.randrange(0, 500),
                # may
                columns[18]: random.randrange(0, 500),
                # jun
                columns[19]: random.randrange(150, 200),
                # jul
                columns[20]: random.randrange(150, 200),
                # aug
                columns[21]: random.randrange(150, 200),
                # sep
                columns[22]: random.randrange(150, 200),
                # oct
                columns[23]: random.randrange(150, 200),
                # nov
                columns[24]: random.randrange(50, 100),
                # dec
                columns[25]: random.randrange(50, 100),
                # sunshine
                # jan
                columns[26]: random.randrange(1, 60),
                # feb
                columns[27]: random.randrange(30, 60),
                # mar
                columns[28]: random.randrange(30, 60),
                # apr
                columns[29]: random.randrange(30, 60),
                # may
                columns[30]: random.randrange(30, 60),
                # jun
                columns[31]: random.randrange(30, 60),
                # jul
                columns[32]: random.randrange(30, 60),
                # aug
                columns[33]: random.randrange(30, 60),
                # sep
                columns[34]: random.randrange(30, 60),
                # oct
                columns[35]: random.randrange(30, 60),
                # nov
                columns[36]: random.randrange(30, 60),
                # dec
                columns[37]: random.randrange(30, 60),})

make_trainset_crop_id_1()
print("Successful")