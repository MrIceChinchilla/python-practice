print('Итак, вы секретный агент, цель которого спасти заложника из рук бандитов. С собой у вас только:\nНож, пистолет с патронами и граната на крайний случай. Удачи!\n\n')
print('Вы стоите прямо перед зданием!\n1) Осмотреть здание\n2) Войти внутрь\n3) Бросить гранату в дверь')
answer = int(input())
if answer == 1:
    print(u'Итак, вы осмотрели здание, оно 3-ёх этажное, спереди балкон. На первом этаже есть 2 окна, но одно из них заколочено досками, рядом с ними лежит молоток, второе окно пустое.\n1) Войти в пустое окно\n2) Вернуться ко входу\n3) Разбить доски молотком\n4) Подойти к пустому окну и взять с собой молоток\n5) Бросить гранату в пустое окно')
    answer1 = int(input())
    if answer1 == 1:
        print('Не успел я подойти к окну, как тут-же меня подстрелили.\n---Наступила мучительная смерть от экспансивных боеприпасов в живот---')
    elif answer1 == 2:
        print('Чёрт! меня заметил снайп...\n---Наступила смерть, хоть и безболезненная, 1 выстрел в голову и всё!---')
    elif answer1 == 3:
        print('Кажется я изрядно пошумел... О нет пришли охранники! Что делать?\n1) Перестрелять их всех!\n2) Спрятаться под заколоченым окном\n3) Закинуть им гранату\n4) Притвориться мёртвым')
        answer2 = int(input())
    elif answer1 == 4:
        print('Я так и думал! Там стоял один из бандитов.\n1) Застрелить гада\n2) Отвлечь охранника броском молотка\n3) Притвориться заложником и выбросить оружия\n4) Подождать')
        answer3 = int(input())
        if answer3 == 1:
            print('Бах! И нет бандита, О нет! из-за угла вбежал другой бандит! Не успел я ничего придумать ничего, как сразу словаил лбом "маслину"\n---Быстрая смерть, что тут сказать---')
        elif answer3 == 2:
            print('Ух-ты, сработало, этот тупица пошёл смотреть что и куда упало. Прям как в фильмах!Ах да мне же нельзя ломать 4-тую стену. Что делать теперь?\n1) Войти в пустое окно\n2) Метнуть в охранника нож\n3) Застрелить бандюгана')
            answer4 = int(input())
            if answer4 == 3:
                print('Бах! И нет бандита, О нет! из-за двери вбежал другой бандит! Не успел я ничего придумать ничего, как сразу словил лбом "маслину"\n---Быстрая смерть, что тут сказать---')
            elif answer4 == 1:
                print('*Скрип доски* Бах!\n---Наступила смерть от рук одного из бандитов---')
            elif answer4 == 2:
                print('Есть! Бандит упал замертво. Пора заходить. Итак вы внутри комнаты.\n1) Осмотреть комнату\n2) Осмотреть тело разбойника')
                answer5 = int(input())
                if answer5 == 1:
                    print('В относительно небольшой комнатке был шкаф, стол и две двери. Судя по всему одна из них ведёт в уборную, в которой горит свет. Я посмотрел в замочную скважину, и там ивправду был ещё один бандит.\n1) Осмотреть тело\n2) Переодеться в бандита и спрятать тело в шкафу\n3) Сбросить тело в окно и спрятаться в шкафу')
                    answer6 = int(input())
                    if answer6 == 1:
                        print('У бандита были: рация, патроны для пистолета, пистолет, нож... Абзац! Из двери вышел другой банди...\n---Ребят не трогайте трупы!---')
                    elif answer6 == 2:
                        print('Скорее! Готово, я настоящий разбойник! Тело в шкафу, а сам я под великоватой, но маскировкой. О нет кто-то идёт из уборной!\n1) Спрятаться вместе с телом в шкафу\n2) Ждать\n3) Выйти из комнаты в корридор')
                        answer7 = int(input())
                        if answer7 == 1:
                            print('Продолжение следует!')
                        elif answer7 == 2:
                            print('Продолжение следует!')
                        elif answer7 == 3:
                            print('Продолжение следует!')
                    elif answer6 == 3:
                        print('Есть! Я спрятался в шкафу и сбросил тело через окно на улицу. Я слышу шаги!\n1) Выйти из шкафа и застрелить бандита\n2) Ждать')
                        answer8 = int(input())
                        if answer8 == 1:
                            print('Продолжение следует!')
                        elif answer8 == 2:
                            print('Продолжение следует!')
                elif answer5 == 2:
                    print('У бандита были: рация, патроны для пистолета, пистолет, нож... Абзац! Из двери вышел другой банди...\n---Ребят не трогайте трупы!---')
        elif answer3 == 3:
            print('Продолжение следует!')
elif answer == 2:
    print('Как только я вошёл внутрь меня просто расстреляли!\n---Наступила мучительная и негуманная казнь---')   
elif answer == 3:
    print('Я быстро открыл дверь, закинул туда гранату и закрыл её. Неужели успех?\nВдруг мне позвонило начальство и сообщило, что заложники уже мертвы. Ведь как сказали бандиты,"Пусть только шмальнут! Я тут всех заложников положу!"\n---Миссия провалена---')
else:
    print('Неверный вариант ответа')
