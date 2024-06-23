label din_intro:
    $ din_set_mode_adv()
    stop music fadeout 3
    $ renpy.pause(2, hard=True)
    $ persistent.sprite_time = "sunset"  
    $ persistent.timeofday = "sunset"
    scene bg din_ext_camp_plain_sight_sunset with Dissolve(2)
    play ambience ambience_ext_road_evening fadein 2
    play music dn_explosions_in_the_sky_your_hand_in_mine fadein 5
    din_narrator "В тихом мире закатного горизонта давно уже ничего не происходит."
    din_narrator "То, что когда-то было лагерем, сейчас - лишь бескрайняя пустошь."
    din_narrator "Разве что одинокая дорога рассекает пейзаж."
    din_narrator "Когда-то она не смотрелась так одиноко."
    din_narrator "Да и жизнь здесь была иной."
    din_narrator "Десятки Пионеров мирились с бесконечность."
    din_narrator "Играли с куклами, умирали, теряли рассудок, строили надежды, планы..."
    din_narrator "Каждого из них я знал. По повадкам, страхам, и имени, если оно было."
    din_narrator "Мог не задумываясь сказать кто как проводит своё время и сколько ему осталось до сумашествия."
    din_narrator "Я видел, как Пионеры менялись, развивались или застывали во времени, отказываясь двигаться дальше."
    din_narrator "А сейчас эта память медленно утекает, как песок сквозь ладони."
    din_narrator "А потом прозошла случайность."
    ## мелькают фоны из ОУД с эффектом помех
    din_narrator "Странная смена со странными событиями."
    din_narrator "Ниточник, кажется так его тогда звали, попробовал новую попытку выхода."
    din_narrator "Эти события я еще помнил хорошо."
    din_narrator "Игра в карты..."
    din_narrator "«Разговор» у костра... "
    din_narrator "И самое невероятное - его план сработал!"
    din_narrator "Мир, в котом мы провели больше смен, чем звезд на холодном небе, дрогнул."
    din_narrator "Исчез лагерь."
    din_narrator "Исчезло время."
    din_narrator "Исчезли перемены."
    din_narrator "И исчезли Пионеры."
    din_narrator "И только две куклы до сих пор бродят по этой пустыне. {w}Неприкаянные и всеми забытые."
    din_narrator "Я и Ниточник."
    din_narrator "Я поднял взгляд к солнцу."
    din_narrator "Забавно, оно теперь не греет и можно смотреть на него сколько угодно."
    din_narrator "Но когда-то дни в лагере были совсем другими."
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ persistent.din_flags['din_intro_completed'] = True
    $ renpy.pause(2, hard=True)
    jump din_ikarus_story