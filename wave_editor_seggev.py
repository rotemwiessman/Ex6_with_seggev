# 
# FILE : .py
# WRITER : Seggev Haimovich , seggev , 206729295
# EXERCISE : intro2cs2 ex? 2021
# DESCRIPTION: 
# STUDENTS I DISCUSSED THE EXERCISE WITH: none
# WEB PAGES I USED: none
# NOTES: none
#
from copy import deepcopy


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
