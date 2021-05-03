EDIT_MENU = {"REVERS": "1", "MINUS": "2", "FAST FORWARD": "3", "SLOW_DOWN": "4",
             "VOLUME_UP": "5", "VOLUME_DOWN": "6", "LOW_PASS_FILTER": "7", "FINISH_EDIT": "8"}
START_MENU = {"EDIT_AUDIO": "1", "CREATE_AUDIO": "2", "CLOSE": "3"}
MAX_VALUE = 32767
MIN_VALUE = -32768


def minus_audio(audio_data):
    """
    replace all the audio data with minus of the current audio data
    :param audio_data:
    :return:
    """
    minus_audio_data = []
    for pair in audio_data:
        pair = [MIN_VALUE+1 if i == MIN_VALUE else i for i in pair]  # deny the function from exceeding the value limit
        minus_audio_data.append([pair[0] * -1, pair[1] * -1])
    return minus_audio_data


def change_volume(audi_data, coefficient):
    """
    change the volume of the data accordint to a given coefficient
    :param audi_data: original data
    :param coefficient: coefficient to multiply with
    :return: the changed list of data
    """
    changed_data = []
    for pair in audio_data:
        changed_data.append([int(pair[0] * coefficient), int(pair[1] * coefficient)])
    return changed_data


def volume_up(audio_data):
    """
    turn up the audio by 1.2
    :param audio_data:
    :return:
    """
    changed_data =change_volume(audio_data, 1.2)
    counter = 0
    for pair in changed_data:
        if pair[0] > MAX_VALUE: changed_data[counter][0] = MAX_VALUE
        elif pair[0] < MIN_VALUE: changed_data[counter][0] = MIN_VALUE
        if pair[1] > MAX_VALUE: changed_data[counter][1] = MAX_VALUE
        elif pair[1] < MIN_VALUE: changed_data[counter][1] = MIN_VALUE
        counter += 1
        # deny the function from exceeding the value limit
    return changed_data


def volume_down(audio_data):
    """
    turn down the audio by 1.2
    :param audio_data:
    :return:
    """
    a = 1/1.2
    return change_volume(audio_data, a)


def finish_and_save(audio_data):
    pass


def reverse_filter(audio_data):
    """
    reverse the order of the values in the audio data list
    :param audio_data: list of lists
    :return: reversed_audio_data (list of lists)
    """
    new_audio_data = audio_data[::-1]
    return new_audio_data


def fast_forward_filter(audio_data):
    """

    :param audio_data:
    :return:
    """
    new_audio_data = audio_data[::2]
    return new_audio_data


def average_pairs(list_of_lists):
    """
    gets list of two lists and calculate the average of every argument in
    these lists.
    returns list with the averages
    :param list_of_lists: list of lists
    :return: average (list)
    """
    if list_of_lists == []:
        return []
    average = [0, 0]
    for pair in range(len(list_of_lists)):
        average[0] += list_of_lists[pair][0]
        average[1] += list_of_lists[pair][1]
    average[0] = int(average[0]/len(list_of_lists))
    average[1] = int(average[1]/len(list_of_lists))
    return average


def slow_down_filter(audio_data):
    """
    slows down the m
    :param audio_data:
    :return:
    """
    new_audio_data = []
    for i in range(len(audio_data)*2 - 1):
        if i % 2 == 0:
            new_audio_data.append(audio_data[i//2])
        else:
            new_audio_data.append(average_pairs([audio_data[i//2],
                                                 audio_data[i//2 + 1]]))
    return new_audio_data


def low_pass_filter(audio_data):
    new_audio_data = [average_pairs(audio_data[:2])]
    for i in range(1, len(audio_data)-1):
        new_audio_data.append(average_pairs(audio_data[i-1:i+2]))
    new_audio_data.append(average_pairs((audio_data[-2:])))
    return new_audio_data


if __name__ == '__main__':
    audio_data = [[1111,2222],[MAX_VALUE-30,MIN_VALUE+30],[0,-555]]
    print(audio_data)
    audio_data = volume_up(audio_data)
    print(audio_data)