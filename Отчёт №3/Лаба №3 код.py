def trim_transient_process(data_list, start_idx, end_idx):
    return data_list[start_idx:end_idx]


def calculate_channel_stats(telemetry_dict):
    result = {}

    for key, value in telemetry_dict.items():

        result[key] = sum(value) / len(value)

    return result


def filter_negative_spikes(data_list):
    return list(filter(lambda x: x >= 0, data_list))


if __name__ == "__main__":

    raw_rpm = [0, 450, 1495, 1502, 1498, 1500, 1505, 1100, 0]

    start_idx = 2
    end_idx = 7

    print("=== ТЕЛЕМЕТРИЯ ИСПЫТАТЕЛЬНОГО СТЕНДА ===")

    clean_data = filter_negative_spikes(raw_rpm)
    sliced_data = trim_transient_process(clean_data, start_idx, end_idx)

    stats = calculate_channel_stats({"rpm": sliced_data})

    print(f"Установившийся режим (срез[{start_idx}:{end_idx}]): {sliced_data}")
    print(f"Средняя частота установившегося режима: {stats['rpm']} об/мин")
