init python:
    import time
    from os import path
    
    for file_name in renpy.list_files():
        if "din" in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith("din/images/bg/"):
                renpy.image("bg " + file_path, file_name)

            elif file_name.startswith("din/images/gui/"):
                renpy.image(file_path, file_name)

            elif file_name.startswith("din/images/sprites/"):
                renpy.image(file_path, ConditionSwitch("persistent.sprite_time == 'sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), True, file_name))

            elif file_name.startswith("din/sounds/"):
                globals()[file_path] = file_name

    din_std_set_for_preview = {}
    din_std_set = {}
    store.din_colors = {}
    store.din_names = {}
    store.din_names_list = []
    din_speaker_color = "speaker_color"

    store.din_names_list.append("din_narrator")

    store.din_names_list.append("din_th")

    din_colors["din_teapot"] = {"speaker_color": (85, 19, 19, 255)}
    din_names["din_teapot"] = "Чайник"
    store.din_names_list.append("din_teapot")

    din_colors["din_third"] = {"speaker_color": (0, 73, 121, 255)}
    din_names["din_third"] = "Третий"
    store.din_names_list.append("din_third")

    din_colors["din_third_i"] = {"speaker_color": (0, 73, 121, 255)}
    din_names["din_third_i"] = "Я"
    store.din_names_list.append("din_third_i")

    din_colors["din_nit"] = {"speaker_color": (159, 147, 147, 255)}
    din_names["din_nit"] = "Ниточник"
    store.din_names_list.append("din_nit")

    din_colors["din_nit_he"] = {"speaker_color": (159, 147, 147, 255)}
    din_names["din_nit_he"] = "Он"
    store.din_names_list.append("din_nit_he")

    din_colors["din_hall"] = {"speaker_color": (85, 19, 19, 255)}
    din_names["din_hall"] = "Халл"
    store.din_names_list.append("din_hall")

    din_colors["din_pi_teapot"] = {"speaker_color": (85, 19, 19, 255)}
    din_names["din_pi_teapot"] = "Пионер"
    store.din_names_list.append("din_pi_teapot")

    din_colors["din_gensek"] = {"speaker_color": (139, 0, 0, 255)}
    din_names["din_gensek"] = "Генсек"
    store.din_names_list.append("din_gensek")

    din_colors["din_pi1"] = {"speaker_color": (255, 204, 102, 255)}
    din_names["din_pi1"] = "Пионер"
    store.din_names_list.append("din_pi1")

    din_colors["din_pi2"] = {"speaker_color": (72, 61, 139, 255)}
    din_names["din_pi2"] = "Пионер"
    store.din_names_list.append("din_pi2")

    din_colors["din_pi3"] = {"speaker_color": "#FFFFE0"}
    din_names["din_pi3"] = "Пионер"
    store.din_names_list.append("din_pi3")

    din_colors["din_dv"] = {"speaker_color": "#ffaa00"}
    din_names["din_dv"] = "Алиса"
    store.din_names_list.append("din_dv")

    din_colors["din_sl"] = {"speaker_color": "#ffd200"}
    din_names["din_sl"] = "Славяна"
    store.din_names_list.append("din_sl")

    din_colors["din_un"] = {"speaker_color": "#aa64d9"}
    din_names["din_un"] = "Лена"
    store.din_names_list.append("din_un")

    def din_char_define(character_name, is_nvl = False):
        global DynamicCharacter
        global nvl
        global din_store
        global din_speaker_color
        din_gl = globals()
        
        if character_name == "din_narrator":
            if is_nvl:
                din_gl["din_narrator"] = Character(None, kind = nvl, what_style = "din_text_style")
            
            else:
                din_gl["din_narrator"] = Character(None, what_style = "din_text_style")
            
            return
        
        if character_name == "din_th":
            if is_nvl:
                din_gl["din_th"] = Character(None, kind = nvl, what_style = "din_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            else:
                din_gl["din_th"] = Character(None, what_style = "din_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            return
        
        if is_nvl:
            din_gl[character_name] = DynamicCharacter("%s_name" % character_name, color = store.din_colors[character_name][din_speaker_color], kind = nvl, what_style = "din_text_style", who_suffix = ":")
            din_gl["%s_name" % character_name] = store.din_names[character_name]
        
        else:
            din_gl[character_name] = DynamicCharacter("%s_name" % character_name, color = store.din_colors[character_name][din_speaker_color], what_style = "din_text_style")
            din_gl["%s_name" % character_name] = store.din_names[character_name]

    def din_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global din_store
        
        for character_name in store.din_names_list:
            din_char_define(character_name)

    def din_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global din_narrator
        global din_th
        din_narrator_nvl = din_narrator
        th_nvl = din_th
        
        global din_store
        
        for character_name in store.din_names_list:
            din_char_define(character_name, True)

    def din_reload_names():
        global din_store
        
        for character_name in store.din_names_list:
            din_char_define(character_name)

    din_reload_names()

    def din_frame_animation(image_name, frames_quantity, retention, loop, transition, start = 1, **properties):
        anim_args = []
        
        for i in xrange(start, start + frames_quantity):
            anim_args.append(renpy.display.im.image(image_name + "_" + str(i) + ".png"))
            
            if loop:
                anim_args.append(retention)
                anim_args.append(transition)
        
        return anim.TransitionAnimation(*anim_args, **properties)

    def din_blink(blink_pause):
        renpy.show("blink")
        renpy.pause(blink_pause, hard = True)

    def din_unblink(scene_name, unblink_pause):
        renpy.hide("blink")
        renpy.scene()
        renpy.show(scene_name)
        renpy.show("unblink")
        renpy.pause(unblink_pause, hard = True)

    def din_timing_memorization_m(type, fade):
        global pause_time_m
        global file_name_m
        
        if type == "pause":
            file_name_m = renpy.music.get_playing("music")
            pause_time_m = renpy.music.get_pos("music")
            renpy.music.stop("music", fadeout = fade)

        if type == "continue":
            if pause_time_m == None:
                continue_time_m = "<from 0>" + file_name_m

            else:
                continue_time_m = "<from {}>".format(pause_time_m) + file_name_m

            renpy.music.play(continue_time_m, "music", fadein = fade)

    def din_timing_memorization_a(type, fade):
        global pause_time_a
        global file_name_a
        
        if type == "pause":
            file_name_a = renpy.music.get_playing("ambience")
            pause_time_a = renpy.music.get_pos("ambience")
            renpy.music.stop("ambience", fadeout = fade)

        if type == "continue":
            if pause_time_a == None:
                continue_time_a = "<from 0>" + file_name_a

            else:
                continue_time_a = "<from {}>".format(pause_time_a) + file_name_a

            renpy.music.play(continue_time_a, "ambience", fadein = fade)

    def din_predict_screens():
        for screen_name in din_screens_list:
            renpy.start_predict_screen(screen_name)

    def din_predict_resources():
        for folder_name in din_folders_list:
            renpy.start_predict(folder_name)

    def din_stop_predict_screens():
        for screen_name in din_screens_list:
            renpy.stop_predict_screen(screen_name)

    def din_stop_predict_resources():
        for folder_name in din_folders_list:
            renpy.stop_predict(folder_name)
            
    def din_onload(type):
        global din_lock_quit
        global din_lock_quick_menu

        if type == "lock":
            renpy.config.skipping = None
            din_lock_quit = True
            din_lock_quick_menu = True
            config.allow_skipping = False

        elif type == "unlock":
            din_lock_quit = False
            din_lock_quick_menu = False
            config.allow_skipping = True

    din_onload_curried = renpy.curry(din_onload)

    def din_current_time():
        global din_hour
        
        din_time = time.strftime("%H:%M:%S", time.localtime())
        din_hour, din_min, din_sec = din_time.split(":")
        din_hour = int(din_hour)

    def din_predict_resources_d():
        din_rightnow_r = time.time()

        while time.time() - din_rightnow_r < 6:
            din_predict_resources()
            
            renpy.show("din_first_dot_image", at_list = [din_first_dot_pos])
            renpy.pause(0.7, hard = True)
            renpy.show("din_second_dot_image", at_list = [din_second_dot_pos])
            renpy.pause(0.7, hard = True)
            renpy.show("din_third_dot_image", at_list = [din_third_dot_pos])
            renpy.pause(0.7, hard = True)
            renpy.hide("din_first_dot_image")
            renpy.hide("din_second_dot_image")
            renpy.hide("din_third_dot_image")
            renpy.pause(0.7, hard = True)

    def din_predict_screens_d():
        din_rightnow_s = time.time()

        while time.time() - din_rightnow_s < 3:
            din_predict_screens()

            renpy.show("din_first_dot_image", at_list = [din_first_dot_pos])
            renpy.pause(0.7, hard = True)
            renpy.show("din_second_dot_image", at_list = [din_second_dot_pos])
            renpy.pause(0.7, hard = True)
            renpy.show("din_third_dot_image", at_list = [din_third_dot_pos])
            renpy.pause(0.7, hard = True)
            renpy.hide("din_first_dot_image")
            renpy.hide("din_second_dot_image")
            renpy.hide("din_third_dot_image")
            renpy.pause(0.7, hard = True)

        renpy.show("din_first_dot_image", at_list = [din_first_dot_pos])
        renpy.music.stop("ambience", 2)

    def din_predicting():
        din_predict_resources_d()
        din_predict_screens_d()

    def din_loading_screen():
        renpy.pause(2, hard = True)

        if din_hour in din_night_hours:
            renpy.show("din_ext_camp_entrance_night", at_list = [din_zoom_in_center])
            renpy.show("din_main_menu_frame")
            renpy.show("din_name_header", at_list = [din_name_header_pos])
            renpy.show("din_main_menu_underline", at_list = [din_underline_pos])
            renpy.show("din_loading_text", at_list = [din_loading_text_pos])
            renpy.music.play("sound/ambiences/ext_road_night.ogg", "ambience", fadein = 2)
            renpy.show("din_loading_icon_night", at_list = [din_full_rotate_repeat(1.1, 0.8, 0.5, 0.55)])

        elif din_hour in din_sunset_hours:
            renpy.show("din_ext_camp_entrance_sunset", at_list = [din_zoom_in_center])
            renpy.show("din_main_menu_frame")
            renpy.show("din_name_header", at_list = [din_name_header_pos])
            renpy.show("din_main_menu_underline", at_list = [din_underline_pos])
            renpy.show("din_loading_text", at_list = [din_loading_text_pos])
            renpy.music.play("sound/ambiences/ext_road_evening.ogg", "ambience", fadein = 2)
            renpy.show("din_loading_icon_sunset", at_list = [din_full_rotate_repeat(1.1, 0.8, 0.5, 0.55)])

        elif din_hour in din_morning_hours:
            renpy.show("din_ext_camp_entrance_morning", at_list = [din_zoom_in_center])
            renpy.show("din_main_menu_frame")
            renpy.show("din_name_header", at_list = [din_name_header_pos])
            renpy.show("din_main_menu_underline", at_list = [din_underline_pos])
            renpy.show("din_loading_text", at_list = [din_loading_text_pos])
            renpy.music.play("sound/ambiences/ext_road_evening.ogg", "ambience", fadein = 2)
            renpy.show("din_loading_icon_morning", at_list = [din_full_rotate_repeat(1.1, 0.8, 0.5, 0.55)])

        else:
            renpy.show("din_ext_camp_entrance_day", at_list = [din_zoom_in_center])
            renpy.show("din_main_menu_frame")
            renpy.show("din_name_header", at_list = [din_name_header_pos])
            renpy.show("din_main_menu_underline", at_list = [din_underline_pos])
            renpy.show("din_loading_text", at_list = [din_loading_text_pos])
            renpy.music.play("sound/ambiences/ext_road_day.ogg", "ambience", fadein = 2)
            renpy.show("din_loading_icon_day", at_list = [din_full_rotate_repeat(1.1, 0.8, 0.5, 0.55)])

        renpy.transition(Dissolve(2))
        renpy.pause(2.0, hard = True)
        din_predicting()

    def din_set_main_menu_cursor():
        config.mouse = {"default": [(din_gui_path + "misc/din_cursor.png", 0, 0)]}

    din_set_main_menu_cursor_curried = renpy.curry(din_set_main_menu_cursor)

    def din_set_timeofday_cursor():
        global din_set_timeofday_cursor_var

        if din_set_timeofday_cursor_var:
            config.mouse = {"default": [(din_gui_path + "dialogue_box/" + persistent.timeofday + "/cursor.png", 0, 0)]}

    din_set_timeofday_cursor_curried = renpy.curry(din_set_timeofday_cursor)

    def din_set_null_cursor():
        config.mouse = {"default": [(din_gui_path + "misc/din_none.png", 0, 0)]}

    din_set_null_cursor_curried = renpy.curry(din_set_null_cursor)

init:
    $ din_lock_quit_game_main_menu_var = True
    $ din_lock_quit = False
    $ din_lock_quick_menu = False

    $ din_take_everything = False
    $ din_winterlong_story_bar = False

    if persistent.din_ikarus_story_completed == None:
        $ persistent.din_ikarus_story_completed = False

    if persistent.din_winterlong_story_completed == None:
        $ persistent.din_winterlong_story_completed = False

    if persistent.din_rolegame_story_completed == None:
        $ persistent.din_rolegame_story_completed = False

    $ din_wiperight = CropMove(.5, "wiperight")
    $ din_wipeleft = CropMove(.5, "wipeleft")

    $ din_screens_list = [
        "din_main_menu", "din_preferences_main_menu", "din_load_main_menu", "din_achievements", "din_quit_main_menu", "din_preferences", 
        "din_save", "din_load", "din_say", "din_nvl", "din_game_menu_selector", "din_quit", "din_yesno_prompt", "din_text_history", "din_choice", "din_help"
    ]

    $ din_folders_list = ["din/images/bg*.*", "din/images/sprites*.*"]

    $ din_set_timeofday_cursor_var = False

    $ din_night_hours = [22, 23, 24, 0, 1, 2, 3, 4, 5, 6]
    $ din_sunset_hours = [20, 21]
    $ din_morning_hours = [7, 8]

    image din_name_header = Text("Дни нигде", size = 180, font = "din/images/gui/fonts/AG_Futura Regular.ttf")
    image din_loading_text = Text("Загрузка", size = 125, font = "din/images/gui/fonts/AG_Futura Regular.ttf")

    image bg din_stars_anim = din_frame_animation("din/images/bg/din_stars_anim/din_stars", 2, 1.5, True, Dissolve(1.5))
    image bg din_fireplace_winterlong_anim = din_frame_animation("din/images/bg/din_fireplace_winterlong_anim/din_fireplace_winterlong", 10, 1.8, True, Dissolve(1.2))
    image din_main_menu_day_anim = din_frame_animation("din/images/gui/main_menu/day/din_day", 5, 4, True, Dissolve(2))
    image din_main_menu_night_anim = din_frame_animation("din/images/gui/main_menu/night/din_night", 5, 4, True, Dissolve(2))
    image din_main_menu_sunset_anim = din_frame_animation("din/images/gui/main_menu/sunset/din_sunset", 5, 4, True, Dissolve(2))
    image din_main_menu_morning_anim = din_frame_animation("din/images/gui/main_menu/morning/din_morning", 5, 4, True, Dissolve(2))

    image din_gensek_silhouette_normal = im.MatrixColor("din/images/sprites/din_pi normal.png", im.matrix.tint(0, 0, 0))

    transform din_buttons_atl():
        on idle:
            easein 0.5 zoom 1.0

        on hover:
            easein 0.5 zoom 1.018

    transform din_full_rotate_repeat(l, z, x, y):
        parallel:
            zoom z
            xalign x
            yalign y 
            rotate_pad True
            rotate 0
            linear l rotate 360
            repeat

    transform din_name_header_pos():
        xalign 0.5
        yalign 0.045

    transform din_underline_pos():
        xalign 0.5 ypos 240

    transform din_loading_text_pos():
        xalign 0.5 ypos 840

    transform din_first_dot_pos():
        xpos 1216
        ypos 934

    transform din_second_dot_pos():
        xpos 1235
        ypos 934

    transform din_third_dot_pos():
        xpos 1254
        ypos 934

    transform din_zoom_in_center():
        xalign 0.5 yalign 0.5 zoom 1.0
        pause 2.0
        linear 20 zoom 2.0 xalign 0.5 yalign 0.5