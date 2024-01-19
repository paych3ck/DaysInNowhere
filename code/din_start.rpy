init python:
    mods["din_start"] = u"{font=din/images/gui/fonts/AG_Futura Regular.ttf}{size=50}Дни нигде{/font}{/size}"

    try:
        modsImages["din_start"] = ("din/images/gui/misc/din_tabular_list_preview.png", False)

    except:
        pass

label din_start:
    $ din_onload("lock")
    $ din_screens_save_act()
    scene bg black with Dissolve(2)
    $ din_current_time()

    if din_hour in din_night_hours:
        scene din_ext_camp_entrance_night
        
    elif din_hour in din_sunset_hours:
        scene din_ext_camp_entrance_sunset
        
    elif din_hour in din_morning_hours:
        scene din_ext_camp_entrance_morning
        
    else:
        scene din_ext_camp_entrance_day

    show din_intro_frame at truecenter

    show din_intro_logo at truecenter

    with Dissolve(2)
    $ renpy.pause(0.5, hard = True) 
    play sound din_intro_sample
    $ renpy.pause(8, hard = True)
    scene bg black with Dissolve(2)
    $ persistent.timeofday = "day"
    $ din_set_mode_adv()
    $ din_onload("unlock")
    $ din_set_main_menu_cursor()
    $ renpy.transition(Dissolve(2))