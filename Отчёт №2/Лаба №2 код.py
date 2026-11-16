from random import randint

def pneumatic_drive_move(t_max=1, dt=0.1, end_pos=20):
   
    current_time = 0
    current_pos = 0
    status = "ОК"

    while True:

        if current_time > t_max:
            status = "Таймаут"
            break

        if current_pos >= end_pos:
            break

        current_time += dt
        current_pos += randint(1, 3)

    return current_pos, status

if __name__ == "__main__":
    print(pneumatic_drive_move())
