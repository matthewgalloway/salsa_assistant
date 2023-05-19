from django.utils.translation import gettext as _
import datetime

default_date = datetime.datetime(2000, 1, 1)
BASE_MOVES = (("CrossBody-InsideTurn",_("CrossBody-InsideTurn")),
              ("CrossBody-OutsideTurn",_("CrossBody-OutsideTurn")),
              ("CrossBody",_("CrossBody")),
              ("InsideTurn",_("InsideTurn")),
              ("OutsideTurn",_("OutsideTurn")),
              ("Leader hammerlock",_("Leader hammerlock")),
              ("Follower hammerlock",_("Follower hammerlock")),
              ("Copa", _("Copa")),
              ("OpenBreak",_("OpenBreak")),
              ("Titanic", _("Titanic")),
              ("RightSidePass", _("RightSidePass")),
              ("BodyWrap",_("BodyWrap")))

HOLDS = (("Left2Left", _("Left2Left")),
        ("Right2Right", _("Right2Right")),
        ("Right2Left", _("Right2Left")),
        ( "Left2Right", _("Left2Right")),
        ( "ClosedPosition", _("ClosedPosition")),
        ("Both Normal Hold", _("Both Normal Hold")),
        ("BodyWrap-LeftOverRight", _("BodyWrap-LeftOverRight")),
        ("BodyWrap-RightOverLeft",_("BodyWrap-RightOverLeft")),
        ("Both - Right Over Left",_("Both - Right Over Left")),
        ("Both - Left Over Right",_("Both - Left Over Right")),
        ( "Free Spin", _("Free Spin"))
        )

DIFFICULTY_LEVELS = (("5", _("Can always do in socials")),
                     ("4", _("Can sometimes do in socials")),
                     ("3", _("Cant do in socials but can do in class")),
                     ( "4", _("Cant do in class")),
                     ("5", _("Never Tried")))

MEMORY_DIFFICULTY = (("3", _("Easy")),
        ("2", _("Good")),
        ("1", _("Again")))  


difficulty_levels_dict = {key: value for key, value in DIFFICULTY_LEVELS}
memory_difficulty_dict = {key: value for key, value in MEMORY_DIFFICULTY}