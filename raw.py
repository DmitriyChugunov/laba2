# def list_recorder(ref_list):                                      # создаем def с названием как в задании
#     name = ref_list[0]                                            # создаем переменные name и surnam со значениями взятые из списка ref_list
#     surnam = ref_list[1]
#
#     for name, surnam in zip(name, surnam):                        # проверяем
#         name_surname = [name, surnam]
#         recorder_list.append(name_surname)
#     print(recorder_list)                                              # выводим наш ответ
# recorder_list = []                                                    # переменная со списком в который мы будем вносить наши имена с фамилиями
# ref_list = [["Анастасия", "Платон", "Владислав"], ["Данильченко", "Жуков", "Баранов"]]                # имена с фамилиями
# list_recorder(ref_list)
import re

# # # задача 2
# num = [1, 2, 1, 2, 3, 1, 2, 3, 4]      # переменная со значениями
# def del_rep(num):                      # функция del_rep(num)
#     nums = list(set(num))              #
#     sort_num = sorted(nums)           # в переменную sort_num присваиваем отсортированный nums
#     return sort_num                   # в функцию выводим переменную sort_num
# result = del_rep(num)                 # присваеваем переменной result ответ функции
# print(result)                         # выводим результат

# задача 3
# nums = [10, 20, 30,49, 50]           # переменная с числами
# limit = 50                            # делаем лимит
# def lim_max(nums, limit):             # делаем def
#     a = 0                             # переменная с индексом
#     res = []                          # переменная с результатом
#     for i in range(len(nums)):        # делаем повторения по числу значений в nums
#         if limit < nums[a]:           # если лимит меньше чем значение nums
#             a += 1                    # ничего не делаем и перескакиваем на индекс выше
#         else:
#             res.append(nums[a])       # добавляем в список res значения nums[a]
#             a += 1                    # перескакиваем на значение выше
#     return res                        # возвращаем результат
# ress = lim_max(nums, limit)           # в переменную добавляем ответ(чтобы было легче)
# ress1 = ress[-2]                      # ответ будет по индексу -2
# print(ress1)


# задача 4
# temp = int(input("Введите температуру: "))        # получаем значение
# def temp_cat(temp):                               # создаем функцию
#     if temp < -20:                                # при помощи if и elif присваеваем значения от 0 до 4
#         a = 0
#         return a
#     elif -20 <= temp <= 0:
#         a = 1
#         return a
#     elif 0 <= temp <= 15:
#         a = 2
#         return a
#     elif 15 <= temp <= 25:
#         a = 3
#         return a
#     else:
#         a = 4
#         return a
# res = temp_cat(temp)                          # в переменную res помещаем ответ функции
# if res == 0:                                  # также при помощи if находим нужный нам ответ и выводим его
#     print("Холодно")
# if res == 1:
#     print("Прохладно")
# if res == 2:
#     print("Зябко")
# if res == 3:
#     print("Тепло")
# if res == 4:
#     print("Жарко")


# phones = ['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '123 456 7890']


# def check_phn(phones):
#     formatted_phone = []
#     for phone in phones:
#         cleaned_phone = ''.join(filter(str.isdigit, phone))
#         if len(cleaned_phone) != 11:
#             formatted_phone.append(-1)
#             continue
#         if cleaned_phone[0] not in ['7', '8']:
#             formatted_phone.append(-1)
#             continue
#         formatted_phone = cleaned_phone[:-1] + ' (' + cleaned_phone[1 + 4] + ') ' + cleaned_phone[ 4:7] + '-' + cleaned_phone[ 7:9] + '-' + cleaned_phone[9:]
#         formatted_phone.append(formatted_phone)
#     return formatted_phone
#
#
# result = format_phones(phones)
# print(result)
