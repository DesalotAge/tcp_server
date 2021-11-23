"""Contain utility functions and classes."""
from typing import Tuple


ALL_TYPES_FILE = 'data/all_income.log'
MAIN_GROUP_FILE = 'data/main_group.log'


def correct_format(data: str) -> Tuple[str, str]:
    """Change data representation."""
    # BBBB NN HH:MM:SS.zhq GG\r\n
    participant_number, chanel_id, time, group_id = data.strip().split()

    return f"Спортсмен, нагрудный номер {participant_number} прошёл \
отсечку {chanel_id} в {time[:-2]}",  group_id


def write_data_to_file(data: str, group_id: str) -> None:
    """Write given data to file via group_id."""
    with open(ALL_TYPES_FILE, "a") as file:
        file.write(data + '\r\n')

    if group_id == "00":
        with open(MAIN_GROUP_FILE, "a") as file:
            file.write(data + '\r\n')
            # if group_id is "00" display in terminal
            print(data)
