label din_ikarus_story:
    $ renpy.block_rollback()
    $ din_set_mode_adv()
    stop music fadeout 3
    $ renpy.pause(2, hard=True)
    $ din_story_intro('Икарус\nДень Чайника', 'day', 'bg ext_road_day', 'din_hall pos2 smile', 'Икарус', 'День Чайника', 'ext_road_day')
    scene bg black with Dissolve(2)
    scene bg din_ext_power_line_day with Dissolve(2)
    $ din_onload("unlock")
    play music din_the_last_days_the_time_will_never_come_back fadein 4
    play ambience ambience_camp_entrance_day fadein 2
    din_th "У-у-ух, чертова железяка!"
    din_narrator "Карабкаться по линиям электропередач было на удивление непросто."
    din_narrator "Странно, что я делаю это впервые. Занятие-то нетривиальное."
    din_narrator "Вообще, эти прутья, наверное, должны находиться под напряжением. {w}Черт их знает."
    din_narrator "Но факт фактом: в этих линиях самого электричества {i}нет{/i}."
    din_narrator "Я думал, что по ним ток из космоса поступает в лагерь, чтобы питать лампочки и прочую лабуду, но оказывается, источником энергии служат розетки."
    din_narrator "То есть буквально! Можно обрубить все провода за ними и подключить колонку, к примеру, и она заработает, как ни в чем не бывало."
    din_narrator "Я, конечно, не эксперт, но ка-а-ажется, так быть не должно."
    din_narrator "Но!{w} Всегда есть возможность выкорчевать эту розетку и носить её с собой, как вечный двигатель. {w}Удобно? Удобно!"
    play sound sfx_wind_gust
    din_teapot "Га-а-а-а!"
    din_narrator "Налетевший поток кислорода и примесей пошатнул мою дорогу к небу."
    din_narrator "Нет, я не был НАСТОЛЬКО толстым. Но большущий... {w}плащ? {w=0.5}холст? {w=0.5}покрывало? которое я сшил своими трудящими руками и привязал к себе десятками метров гитарных струн, делал меня открытым всем ветрам."
    din_narrator "Так что теперь я был похож на куклу-шаталку, а не на человека."
    din_narrator "Зато она лёгкая. Не знаю, как я бы с тонной металла полез на свою башню."
    din_nit "Если будешь падать, то не на меня, будь добр!"
    din_narrator "Донесся сзади спокойный возглас. {w}В состоянии концентрации я даже забыл, что за мной еще карабкается мой подручный."
    din_th "Ну не пристало же мне делать всё одному, в самом деле?"
    din_teapot "Ты — мой первый приоритет при падении, так что и в радости, и в горе я утащу тебя на дно с собой."
    din_narrator "Не оглядываясь бросил я."
    din_narrator "Поворачивать голову в целом и шею в частности из-за моего груза было неудобно, так что нормально пообщаться — это не сегодня."
    din_th "Только вперед!"
    din_narrator "Хотя я пыхтел, как проклятый, Ниточник испытывал полнейшее спокойствие. Будто и не он вместе со мной взбирался по этим электроскалам уже как второй час."
    din_th "Надо будет подкачаться к лету."
    din_narrator "Я мысленно похихикал, а потом влепил себе такую же мысленную затрещину за скучный каламбур."
    din_narrator "Наконец-то наша вертикальная дорога подошла к концу — мы добрались до вершины."
    din_narrator "Сначала я, а потом и мой компаньон."
    din_narrator "Устроившись поудобнее, насколько это вообще возможно с помощью трёх хлипких железных ниточек, я принялся разворачивать свой летучий плащ."
    show din_nit normal_r at center with dissolve
    din_teapot "Что застрял? Помогай давай, солнце еще в зените."
    din_nit "Куда ты спешишь?"
    din_narrator "Он стал помогать, но всё же упускать повод для беседы было не в его привычках."
    din_teapot "Честное слово, Ниточник, если через две минуты тридцать четыре секунды мы проморгаем тот порыв ветра, то догонять его я отправлю тебя. {w}Хм, дежавю."
    din_nit "Почему ты позвал именно меня?"
    din_teapot "А кого еще? Ну, мог новеньких позвать познакомиться. Но они бы не оценили. "
    din_teapot "Нет, можно было наплести, что выход в небесах и запустить их в космос, но я-то хочу это сделать сам! {w}И они облажаться могут."
    din_nit "Резонно."
    din_teapot "Кто еще остается... {w}У более-менее вменяемых личностей своя туса, силачи из первой десятки порвут меня на флаг..."
    din_teapot "Чем ты, кстати, вообще занимаешься, пока я тебя не дергаю?"
    din_nit "Завожу новые знакомства."
    din_teapot "Ты про того третьего Третьего? Мне кажется, он немного того. {w}Зато какое крутое имя себе взял! И как мне такое в голову не пришло!"
    din_nit "Не только про него. {w}Я тебе рассказывал про кружок художников?"
    din_teapot "Скорее всего да, но смен эдак с семьдесят-семьсот назад. {w}А, может, и не рассказывал. {w}Давай заново."
    din_nit "История не такая уж и большая. Но всё же."
    din_nit "Одному Пионеру, Ожидателю, как-то в голову стрельнула мысль: что если обратиться к какой-то сверхсильной сущности, чтобы та вытащила его во Внешний мир?"
    din_teapot "Вроде помощи извне? Хитро."
    din_narrator "Я даже перестал крепить пару струн к ЛЭПу, чтобы не упустить деталей истории."
    din_nit "Да, идея очень любопытная. Но кого именно вызывать на помощь? {w}В библиотеке есть только упоминания об оккультных трудах. {w}Тупик."
    din_nit "Долго Ждатель думу думал, собрал маленькую группку единомышленников, но всё упиралось в эту проблему."
    din_teapot "Только не говори, что он начал поклоняться легенде о девочке-кошке. {w}Я в тебя плюну!"
    show din_nit smil3_r with dspr
    din_nit "Хорошая идея, когда я с подветренной стороны..."
    din_narrator "Нит только сострадательно улыбнулся. {w}Как же раздражает, когда он прав!"
    din_teapot "Так что там было дальше?"
    din_nit "Он как-то пришел в общую столовую после сна-озарения. По факту, простого бреда."
    din_nit "Тем не менее, в этом бреде довольно четко описывался «ритуал призыва»."
    din_nit "Он собрал свой культ, устроил кровожадный фестиваль в своём лагере и принялся вырисовывать очень аккуратную фигуру на полу библиотеки."
    din_narrator "Нит взял раздражающую паузу. {w}Знает же, что меня это бесит!"
    din_teapot "Ну? {w}Чем всё закончилось?"
    show din_nit normal_r with dspr
    din_narrator "Он пафосно взглянул на солнце."
    din_nit "А это ты узнаешь в следующий раз."
    din_teapot "С какого такого перепуг..."
    hide din_nit with dissolve
    ## Внизу важный коммент \..\
    ##надо поискать код, чтобы менялась анимация посреди фразы
    ##антизум, постоянное резкое шатание камеры, звук ветра
    play sound sfx_wind_gust
    scene bg din_ext_power_line_day:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 0.8 zoom 1.1

        parallel:
            ease 0.8 xalign 0.48
            ease 0.8 xalign 0.52
            repeat

        parallel:
            ease 1.3 rotate 1.5 zoom 1.05
            ease 1.3 rotate -1.05 zoom 1.035
            repeat

    play sound_loop sfx_gusty_wind fadein 2
    din_teapot "{din_shrinking_text}АААААААААААААА!!!{/din_shrinking_text}"
    din_teapot "НИТ, ТВАААААРЬ!"
    din_narrator "За его, возможно, выдуманной историей я пропустил тот самый порыв ветра!"
    din_narrator "Я отлетел от ЛЭПа метров на двадцать вверх! Если бы не привязанные струны, то улетел бы прямо в небо!"
    din_narrator "Только сейчас посмотрел вниз и понял НАСКОЛЬКО тут высоко!"
    din_th "Несмотретьвниз-несмотретьвниз-несмотретьвниз-несмотретьвниз..."
    show din_nit smil3_r at center with dissolve
    $ renpy.pause(0.2, hard=True)
    hide din_nit with dissolve
    din_narrator "Пока ветер вертел мною во все стороны мне удалось выхватить лыбящуюся рожу Нита."
    din_teapot "ЕСЛИ Я ВЫЖИВУ, ТО ПРЕВРАЩУ ТВОЮ ЖИЗНЬ В СУЩИЙ АД, СЛЫШИШЬ?!"
    din_th "И если не выживу, тоже превращу!"
    din_th "Он точно умеет читать по губам. Надеюсь, он уже начал прощаться с родственниками!"
    din_th "Святые огоньки, когда вернусь на твердую землю, ни за что больше не полезу сюда!"
    stop music fadeout 4
    stop ambience fadeout 4
    stop sound_loop fadeout 4
    scene bg black with Dissolve(2)
    $ renpy.pause(2, hard=True)
    
label din_ikarus_story_interlude:
    $ din_set_mode_adv()
    $ din_timeofday = "day"
    scene bg din_ext_camp_plain_sight_day with Dissolve(2)
    play music din_higurashi_when_they_cry_chiyouraiki_no_sora fadein 5
    din_th "Сегодня, похоже, какой-то праздник."
    din_th "Вернее, не сегодня. {w}Сейчас."
    din_th "Всё еще не отвык от старого способа оценивать время. {w}От привычек длиною в сотни циклов не так просто избавиться."
    din_nit_he "Так и не скажешь, что сегодня должен проводиться новый турнир."
    din_narrator "Голос за моей спиной больно разрезал длившуюся уже семьсот одиннадцатый час тишину."
    din_nit_he "Конечно, если бы никто снова не провалил сроки."
    din_third_i "С тех пор, как все уехали, проводить его попросту некому. {w}Ты считал время от самого нашего появления?"
    din_nit_he "Здесь не так много других занятий."
    din_narrator "Однообразная равнина, одинокая стена, за ней — бесконечная дорога."
    din_narrator "Это тюрьма или свобода?"
    din_third_i "Зачем ты пришел ко мне?"
    din_narrator "Я не хотел отворачиваться от бескрайнего горизонта."
    din_nit_he "Смешной вопрос. Ты — единственный одушевлённый объект помимо меня. {w}Одушевлённый весьма условно, но всё же."
    din_nit_he "Почему не называешь меня по имени?"
    din_third_i "А нужно?"
    din_nit_he "Запутаешься в собственных мыслях. Потом не сможешь в памяти отличить меня от себя."
    din_third_i "Это произойдет еще не скоро."
    din_nit_he "Когда не ограничен по срокам жизни, то приходится планировать всё на пару шагов вперёд."
    din_third_i "Зато в моей жизни, по крайней мере, будут сюрпризы."
    din_nit_he "Самообман."
    din_narrator "Мне нечего было сказать в ответ."
    $ renpy.pause(3, hard=True)
    din_third_i "И всё же, зачем ты пришел?"
    din_nit_he "Попросить об одолжении."
    din_third_i "Отказываюсь."
    din_nit_he "Не выслушав? Странно."
    din_th "Эта неожиданная выходка доставила мне эхо удовольствия."
    din_th "Пусть это просто импульс и поступок против логики, но что с того?"
    din_nit_he "Тогда подойду снова через тысячу часов."
    din_third_i "А если я снова откажу?"
    din_nit_he "Тогда через другую тысячу. И потом еще через одну."
    din_third_i "Думаешь, результат когда-то изменится?"
    din_nit_he "Знаю. {w}В вечности меняется всё, кроме неё самой."
    din_nit_he "Увидимся."
    play sound sfx_bush_leaves
    din_narrator "За спиной почти неслышно зашумела трава."
    din_th "Тысяча часов? {w}Дурацкие игры."
    din_th "Ну и пускай."
    $ renpy.pause(3, hard=True)
    din_third_i "Стой! Что за просьба?"
    stop music fadeout 4
    scene bg black with Dissolve(2)
    $ renpy.pause(2, hard=True)
    jump din_winterlong_story