def solution(fees, records):
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    
    answer = []
    slot_dict = {}
    time_dict = {}
    
    for record in records:
        car_number = record[6:10]
        time = record[0:5]
        if record[6:10] not in slot_dict:
            slot_dict[car_number] = time
        else:
            if car_number in time_dict:
                time_dict[car_number] += ((int(time[0:2]) - int(slot_dict[car_number][0:2])) * 60) + (int(time[3:5]) - int(slot_dict[car_number][3:5]))
            else:
                time_dict[car_number] = ((int(time[0:2]) - int(slot_dict[car_number][0:2])) * 60) + (int(time[3:5]) - int(slot_dict[car_number][3:5]))
            del slot_dict[car_number]
                
    # 주차장에 남은 차량
    for number, time in slot_dict.items():
        if number not in time_dict:
            time_dict[number] = ((23 - int(time[0:2])) * 60) + (59 - int(time[3:5]))
        else:
            time_dict[number] += ((23 - int(time[0:2])) * 60) + (59 - int(time[3:5]))
            
    # count 
    for number, time in sorted(time_dict.items()):
        # 기본 요금
        if time <= default_time:
            answer.append(default_fee)
        else:
            remain_time = time - default_time
            answer.append(default_fee + (remain_time + unit_time - 1) // unit_time * unit_fee)
    return answer