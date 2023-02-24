LC_MINUS = "&kp LC(MINUS)"
LC_PLUS = "&kp LC(PLUS)"
LG_RIGHT = "&kp LG(RIGHT)"
LG_LEFT = "&kp LG(LEFT)"
LC_UP = "&kp LC(UP)"
LC_RIGHT = "&kp LC(RIGHT)"
LC_LEFT = "&kp LC(LEFT)"
LA_RIGHT = "&kp LA(RIGHT)"
LA_LEFT = "&kp LA(LEFT)"
LG_SPACE = "&kp LG(SPACE)"
VOL_UP = "&kp C_VOL_UP"
VOL_DOWN = "&kp C_VOL_DN"
BL_SEL_0 = "&bt BT_SEL 0"
BL_SEL_1 = "&bt BT_SEL 1"
BL_SEL_2 = "&bt BT_SEL 2"
USE_BLE = "&out OUT_BLE"
USE_USB = "&out OUT_USB"
BLE_CLR = "&bt BT_CLR"
EP_ON = "&ext_power EP_ON"
EP_OFF = "&ext_power EP_OFF"
LGLS4 = "&kp LG(LS(NUMBER_4))"
LGLS5 = "&kp LG(LS(NUMBER_5))"
FN_SPACE = "&lt NBC SPACE"
ALT_GRV = "&mt LALT GRAVE"
FN_TAB = "&lt DSK TAB"
REFRESH = "&kp C_AC_REFRESH"
MULTIPLY = "&kp KP_MULTIPLY"
SHZ = "&mt LSHFT Z"
ESCTL = "&mt LCTRL ESC"


def num(n): return f"&kp NUMBER_{n}"


def ctl_n(num): return f"&kp LC(NUMBER_{num})"


layers = {
    "default_layer": {
        "pound_define": "DFT",
        "bindings": f"""
    ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
    ┃ {FN_TAB}   ┃ &lt DSK Q  ┃ &kp W      ┃ &kp E      ┃ &kp R      ┃ &kp T      ┃┃ &kp Y      ┃ &kp U      ┃ &kp I      ┃ &kp O      ┃ &kp P      ┃ &kp BSPC   ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃ &mo NVW    ┃ &lt NVM A  ┃ &kp S      ┃ &kp D      ┃ &kp F      ┃ &kp G      ┃┃ &kp H      ┃ &kp J      ┃ &kp K      ┃ &kp L      ┃ &kp SEMI   ┃ &kp SQT    ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃ &kp LSHFT  ┃ {SHZ}      ┃ &kp X      ┃ &kp C      ┃ &kp V      ┃ &kp B      ┃┃ &kp N      ┃ &kp M      ┃ &kp COMMA  ┃ &kp DOT    ┃ &kp FSLH   ┃ &kp ESC    ┃
    ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
                                           ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
                                           ┃ {ALT_GRV}  ┃ &kp LGUI   ┃ {FN_SPACE} ┃┃ &lt FU TAB ┃ &kp BSPC   ┃ {ESCTL}    ┃
                                           ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
    """
    },
    "tab_layer": {
        "pound_define": "DSK",
        "bindings": f"""
    ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
    ┃  &kp CAPS  ┃            ┃ {LC_LEFT}  ┃ {LC_RIGHT} ┃            ┃ {LC_UP}    ┃┃            ┃            ┃            ┃            ┃            ┃            ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃            ┃            ┃            ┃            ┃            ┃            ┃┃            ┃            ┃            ┃            ┃            ┃            ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃            ┃            ┃            ┃            ┃            ┃            ┃┃            ┃            ┃            ┃            ┃            ┃            ┃
    ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
                                           ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
                                           ┃            ┃            ┃ {LG_SPACE} ┃┃            ┃            ┃            ┃
                                           ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
    """
    },
    "winmask_layer": {
        "pound_define": "WMK",
        "bindings": f"""
    ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
    ┃            ┃            ┃            ┃            ┃            ┃            ┃┃            ┃            ┃            ┃            ┃            ┃            ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃ &mo NVM    ┃            ┃            ┃            ┃            ┃            ┃┃            ┃            ┃            ┃            ┃            ┃            ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃            ┃            ┃            ┃            ┃            ┃            ┃┃            ┃            ┃            ┃            ┃            ┃            ┃
    ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
                                           ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
                                           ┃            ┃            ┃            ┃┃            ┃            ┃            ┃
                                           ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
    """
    },
    "space_layer": {
        "pound_define": "NBC",
        "bindings": f"""
    ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
    ┃ &kp CAPS   ┃ &kp EXCL   ┃ &kp AT     ┃ &kp HASH   ┃ &kp DLLR   ┃ &kp PRCNT  ┃┃ &kp CARET  ┃ &kp AMPS   ┃ {MULTIPLY} ┃ &kp LPAR   ┃ &kp RPAR   ┃ &kp BSPC   ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃            ┃ {num(1)}   ┃ {num(2)}   ┃ {num(3)}   ┃ {num(4)}   ┃ {num(5)}   ┃┃ &kp MINUS  ┃ &kp EQUAL  ┃ &kp BSLH   ┃ &kp LBKT   ┃ &kp RBKT   ┃ &kp GRAVE  ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃            ┃ {num(6)}   ┃ {num(7)}   ┃ {num(8)}   ┃ {num(9)}   ┃ {num(0)}   ┃┃ &kp UNDER  ┃ &kp PLUS   ┃ &kp PIPE   ┃ &kp LBRC   ┃ &kp RBRC   ┃ &kp TILDE  ┃
    ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
                                           ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
                                           ┃            ┃            ┃            ┃┃            ┃            ┃            ┃
                                           ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
    """
    },
    "caps_layer_win": {
        "pound_define": "NVW",
        "bindings": f"""
    ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
    ┃            ┃ &kp C_PP   ┃ &kp C_PREV ┃ &kp C_NEXT ┃ &kp CAPS   ┃ {REFRESH}  ┃┃ &kp PG_UP  ┃ {LG_LEFT}  ┃ &kp UP     ┃ {LG_RIGHT} ┃ &kp PG_DN  ┃            ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃ &mo NVM    ┃ {VOL_DOWN} ┃ {VOL_UP}   ┃ {LGLS4}    ┃ {LGLS5}    ┃            ┃┃ {LA_LEFT}  ┃ &kp LEFT   ┃ &kp DOWN   ┃ &kp RIGHT  ┃ {LA_RIGHT} ┃ &kp DEL    ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃            ┃            ┃            ┃            ┃            ┃ &tog WMK   ┃┃            ┃ {LC_MINUS} ┃            ┃ {LC_PLUS}  ┃            ┃            ┃
    ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
                                           ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
                                           ┃            ┃            ┃            ┃┃            ┃ &none      ┃            ┃
                                           ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
    """
    },
    "caps_layer_mac": {
        "pound_define": "NVM",
        "bindings": f"""
    ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
    ┃            ┃ &kp TAB    ┃ &kp C_PP   ┃ &kp C_PREV ┃ &kp C_NEXT ┃ &kp CAPS   ┃┃ {LA_LEFT}  ┃ {LG_LEFT}  ┃ &kp UP     ┃ {LG_RIGHT} ┃ {LA_RIGHT} ┃            ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃ &mo NVM    ┃            ┃ {VOL_DOWN} ┃ {VOL_UP}   ┃ {LGLS4}    ┃ {LGLS5}    ┃┃ {LA_LEFT}  ┃ &kp LEFT   ┃ &kp DOWN   ┃ &kp RIGHT  ┃ &kp DEL    ┃ &kp DEL    ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃            ┃            ┃            ┃            ┃            ┃            ┃┃            ┃ {LC_MINUS} ┃            ┃ {LC_PLUS}  ┃            ┃            ┃
    ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
                                           ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
                                           ┃            ┃            ┃            ┃┃            ┃ &none      ┃            ┃
                                           ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
    """
    },
    "r2_layer": {
        "pound_define": "FU",
        "bindings": f"""
    ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
    ┃ {EP_OFF}   ┃            ┃            ┃            ┃            ┃            ┃┃ {BLE_CLR}  ┃            ┃            ┃ {USE_BLE}  ┃ {BL_SEL_0} ┃            ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃ &kp F12    ┃ &kp F1     ┃ &kp F2     ┃ &kp F3     ┃ &kp F4     ┃ &kp F5     ┃┃            ┃ &kp LEFT   ┃ &kp DOWN   ┃ {USE_USB}  ┃ {BL_SEL_1} ┃            ┃
    ┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫
    ┃ &kp F11    ┃ &kp F6     ┃ &kp F7     ┃ &kp F8     ┃ &kp F9     ┃ &kp F10    ┃┃            ┃ {LC_MINUS} ┃            ┃            ┃ {BL_SEL_2} ┃            ┃
    ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
                                           ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
                                           ┃ &kp F11    ┃ &kp RGUI   ┃ {LG_SPACE} ┃┃            ┃            ┃            ┃
                                           ┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛
    """
    },
}


def parse_layer_bindings(bindings):
    return "\n            ".join([line for i, line in enumerate(
        bindings.replace("┃            ", "  &trans     ").split("\n")
    ) if i in [2, 4, 6, 9]]).replace("┃", " ")


def parse_layer(name, bindings):
    return f"""
        {name} {{
            bindings = <
            {parse_layer_bindingsrse_layer_bindings(bindings)}
            >;
        }};"""


def get_layout():
    output = ''
    defs = []
    for i, (name, layer_dict) in enumerate(layers.items()):
        bindings = layer_dict['bindings']
        defs.append(f"#define {layer_dict['pound_define']} {i}")
        output += parse_layer(name, bindings)

    define_block = "\n".join(defs)
    return f"""
#include <behaviors.dtsi>
#include <dt-bindings/zmk/keys.h>
#include <dt-bindings/zmk/bt.h>

{define_block}

/ {{
  chosen {{
    zmk,matrix_transform = &default_transform;
    //zmk,matrix_transform = &five_column_transform;
  }};
}};

/ {{
    combos {{
        compatible = "zmk,combos";
        combo_ret {{
            timeout-ms = <50>;
            key-positions = <21 22>;
            bindings = <&kp RETURN>;
        }};
        combo_rsh {{
            timeout-ms = <50>;
            key-positions = <33 34>;
            bindings = <&kp RSHFT>;
        }};
        combo_squote {{
            timeout-ms = <50>;
            key-positions = <19 20 21>;
            bindings = <&kp SQT>;
        }};
        combo_backtick {{
            timeout-ms = <50>;
            key-positions = <31 32 33>;
            bindings = <&kp GRAVE>;
        }};
        combo_dquote {{
            timeout-ms = <50>;
            key-positions = <7 8 9>;
            bindings = <&kp DQT>;
        }};
    }};
}};
/ {{
    keymap {{
        compatible = "zmk,keymap";
        {output}
    }};
}};
    """


print("generating layout...")
with open("./config/corneish_zen.keymap", "w") as f:
    f.write(get_layout())
print("finished!")
