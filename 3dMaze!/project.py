import math
import time

import engine
from engine.events import *
from engine.operators import *
from engine.types import *


@sprite('Stage')
class Stage(Target):
    """Sprite Stage"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "None", [
            {
                'name': "backdrop1",
                'path': "66107f2420d60da5e5b7b4bedee6f405.svg",
                'center': (240, 180),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            75, [
            {
                'name': "End1",
                'path': "a157e8ecfb27debdbef66db73cfc4802.wav"
            }
        ])

        self.var_speed = "-1.164342852003936e-67"
        self.var_sense = 42
        self.var_angle = 48
        self.var_collumn = 49
        self.var_speed2 = "1.2937142800043707e-68"
        self.var_FPS = 33
        self.var_x = 1.22529159164988
        self.var_y = -121.79167620111947
        self.var_dir = 104.0000000000068
        self.var_resolution = 48
        self.var_lvl = 4

        self.list_distance = List(
            [81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 78, 72, 69, 66, 63, 60, 57, 54, 54, 51, 51, 48, 48, 45, 45, 45, 42]
        )
        self.list_endx = StaticList(
            [-190, 224, 220, 240]
        )
        self.list_endy = StaticList(
            [-164, -65, -165, -180]
        )

        self.sprite.layer = 0

    @on_green_flag
    async def green_flag(self, util):
        self.sounds.set_volume(75)
        while True:
            await self.sounds.play("End1")

            await self.yield_()

    @on_pressed('space')
    async def key_space_pressed(self, util):
        if eq(self.sounds.volume, 0):
            self.sounds.set_volume(75)
        else:
            self.sounds.set_volume(0)


@sprite('Sprite1')
class Sprite1(Target):
    """Sprite Sprite1"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           6, 100, "all around", [
            {
                'name': "costume1",
                'path': "b11c3560b80983a19d8619b1dddb0cc8.svg",
                'center': (241, 182),
                'scale': 1
            },
            {
                'name': "costume2",
                'path': "59bfe1cde34842b41cd3921effc5dc30.svg",
                'center': (-120, 182),
                'scale': 1
            },
            {
                'name': "costume3",
                'path': "50a307ca2794b42fc58cd0ac845ad661.svg",
                'center': (241, 182),
                'scale': 1
            },
            {
                'name': "costume4",
                'path': "1efc961ad38ca18157797dbc9b6c00ed.svg",
                'center': (-117, 184),
                'scale': 1
            },
            {
                'name': "costume5",
                'path': "68e3cbbe03c08fd5a4e5777198105fd1.svg",
                'center': (241, 182),
                'scale': 1
            },
            {
                'name': "costume6",
                'path': "53669431aa6bed970806bb215c7d4eac.svg",
                'center': (-115, 183),
                'scale': 1
            },
            {
                'name': "costume7",
                'path': "d6118606ae342c35876c3ff702ceef1e.svg",
                'center': (241, 182),
                'scale': 1
            },
            {
                'name': "costume8",
                'path': "99ccd721fc1fb130b4b84bb71888d48a.svg",
                'center': (-120, 183),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])





        self.sprite.layer = 1

    @on_clone_start
    async def clone_start(self, util):
        self.gotoxy(0, 0)
        self.costume.set_effect('ghost', 0)
        self.costume.switch("costume2")

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(0, 0)
        self.costume.set_effect('ghost', 100)

    @on_broadcast('new level')
    async def broadcast_newlevel(self, util):
        self.costume.switch((self.costume.number + 2))
        if eq(self.costume.number, 3):
            util.sprites.stage.var_lvl = 2
        if eq(self.costume.number, 5):
            util.sprites.stage.var_lvl = 3

    @on_broadcast('start')
    async def broadcast_START(self, util):
        self.create_clone_of(util, "_myself_")
        self.costume.set_effect('ghost', 100)
        self.costume.switch("costume1")


@sprite('Sprite2')
class Sprite2(Target):
    """Sprite Sprite2"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 240
        self._ypos = 28.571428571428573
        self._direction = 150.00000000000682
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "don't rotate", [
            {
                'name': "costume1",
                'path': "f43bf8a3347c88e4e1bbe3df4cad8cd7.png",
                'center': (1, 1),
                'scale': 2
            },
            {
                'name': "costume2",
                'path': "dced9493b4968cb7f8697b6da1fd4c98.png",
                'center': (2, 5),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_tic = 27



        self.sprite.layer = 2

    @on_green_flag
    async def green_flag(self, util):
        util.sprites.stage.var_lvl = 1
        self.create_clone_of(util, "_myself_")
        self.costume.switch("costume1")
        self.gotoxy(0, 0)
        self.costume.set_effect('ghost', 100)
        util.sprites.stage.var_dir = 0
        util.sprites.stage.var_x = 0
        util.sprites.stage.var_y = 0

    @warp
    async def my_move(self, util, arg_speed):
        util.sprites.stage.var_speed2 = str(tonum(util.sprites.stage.var_speed2) + arg_speed)
        util.sprites.stage.var_speed2 = str((tonum(util.sprites.stage.var_speed2) * 0.8))
        self.move(tonum(util.sprites.stage.var_speed2))
        if (self.get_touching(util, "Sprite1") or self.get_touching(util, "Sprite5")):
            if not self.get_touching(util, "Sprite5"):
                self.move((tonum(util.sprites.stage.var_speed2) * -1))
                util.sprites.stage.var_speed2 = "0"
            else:
                util.sprites.stage.var_lvl += 1
                util.send_broadcast("new level")
                self.gotoxy(0, 0)
                util.sprites.stage.var_x = 0
                util.sprites.stage.var_y = 0

    @warp
    async def my_DRAW(self, util, ):
        self.gotoxy(-235, 180)
        self.pen.set_size(10)
        self.pen.clear_all()
        self.pen.up()
        util.sprites.stage.var_collumn = 1
        for _ in range(len(util.sprites.stage.list_distance)):
            if eq(letter_of(str(util.sprites.stage.list_distance[toint(util.sprites.stage.var_collumn)]), 3), "i"):
                self.pen.exact_color("#ccffdd")
            else:
                self.pen.exact_color("#02ffff")
            if eq(letter_of(str(util.sprites.stage.list_distance[toint(util.sprites.stage.var_collumn)]), 3), "i"):
                self.pen.set_shade(tonum(util.sprites.stage.list_distance[toint(util.sprites.stage.var_collumn)]))
                util.sprites.stage.list_distance[toint(util.sprites.stage.var_collumn)] = (letter_of(str(util.sprites.stage.list_distance[toint(util.sprites.stage.var_collumn)]), 1) + letter_of(str(util.sprites.stage.list_distance[toint(util.sprites.stage.var_collumn)]), 2))
            else:
                self.pen.set_shade((tonum(util.sprites.stage.list_distance[toint(util.sprites.stage.var_collumn)]) * div(50, 80)))
            self.ypos = div(-1200, util.sprites.stage.list_distance[toint(util.sprites.stage.var_collumn)])
            self.pen.down()
            self.ypos = div(1200, util.sprites.stage.list_distance[toint(util.sprites.stage.var_collumn)])
            self.pen.up()
            self.xpos += 10
            util.sprites.stage.var_collumn += 1

    @warp
    async def my_script(self, util, ):
        self.var_tic += 2
        self.gotoxy(util.sprites.stage.var_x, util.sprites.stage.var_y)
        self.direction = util.sprites.stage.var_dir
        if gt(util.timer(), ".5"):
            util.sprites.stage.var_FPS = self.var_tic
            self.var_tic = 1
            util.timer.reset()
        if util.inputs["right arrow"]:
            util.sprites.stage.var_speed = str(tonum(util.sprites.stage.var_speed) + 2)
        if util.inputs["left arrow"]:
            util.sprites.stage.var_speed = str(tonum(util.sprites.stage.var_speed) + -2)
        util.sprites.stage.var_speed = str((tonum(util.sprites.stage.var_speed) * 0.8))
        self.direction += tonum(util.sprites.stage.var_speed)
        if (util.inputs["w"] or util.inputs["up arrow"]):
            await self.my_move(util, 0.5)
        else:
            if (util.inputs["s"] or util.inputs["down arrow"]):
                await self.my_move(util, -0.5)
        util.sprites.stage.var_speed2 = str((tonum(util.sprites.stage.var_speed2) * 0.8))
        util.sprites.stage.var_x = self.xpos
        util.sprites.stage.var_y = self.ypos
        util.sprites.stage.var_dir = self.direction

    @warp
    async def my_sense2(self, util, ):
        while not ((self.get_touching(util, "Sprite1") or eq(util.sprites.stage.var_sense, 81)) or self.get_touching(util, "Sprite5")):
            self.move(3)
            util.sprites.stage.var_sense += 3
        if self.get_touching(util, "Sprite5"):
            util.sprites.stage.list_distance.append((str(util.sprites.stage.var_sense) + "i"))
        else:
            util.sprites.stage.list_distance.append(util.sprites.stage.var_sense)

    @on_broadcast('start')
    async def broadcast_START(self, util):
        while True:
            await self.my_script(util, )
            await self.my_sense(util, )
            await self.my_DRAW(util, )

            await self.yield_()

    @warp
    async def my_sense(self, util, ):
        util.sprites.stage.list_distance.delete_all()
        util.sprites.stage.var_sense = 0
        util.sprites.stage.var_angle = -48
        for _ in range(48):
            util.sprites.stage.var_sense = 0
            self.gotoxy(util.sprites.stage.var_x, util.sprites.stage.var_y)
            self.direction = (util.sprites.stage.var_angle + util.sprites.stage.var_dir)
            await self.my_sense2(util, )
            util.sprites.stage.var_angle += 2


@sprite('Sprite3')
class Sprite3(Target):
    """Sprite Sprite3"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 180.30632289791248
        self._ypos = 104.55208094972014
        self._direction = -165.99999999999318
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "all around", [
            {
                'name': "costume1",
                'path': "b75b8e1be293f63eafb360bed73362b3.png",
                'center': (1, 1),
                'scale': 2
            },
            {
                'name': "costume2",
                'path': "63a6c020bc31321f5440d7700f38ff55.png",
                'center': (2, 5),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 3

    @on_green_flag
    async def green_flag(self, util):
        self.costume.clear_effects()
        self.costume.switch("costume2")
        self.shown = False

    @on_broadcast('start')
    async def broadcast_START(self, util):
        self.shown = True
        while True:
            self.costume.size = 100
            self.gotoxy((div(util.sprites.stage.var_x, 4) + 180), (div(util.sprites.stage.var_y, 4) + 135))
            self.direction = (util.sprites.stage.var_dir + 90)

            await self.yield_()


@sprite('Sprite4')
class Sprite4(Target):
    """Sprite Sprite4"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "3d",
                'path': "2d07382d3204a859205776e32085c927.svg",
                'center': (289, 248),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 6

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(0, 0)
        self.shown = True
        self.costume.set_effect('ghost', 100)
        self.costume.switch("3d")
        util.send_broadcast("MENU")
        while not not util.inputs.mouse_down:
            await self.yield_()
        while not util.inputs.mouse_down:
            await self.yield_()
        while True:
            self.front_layer(util)

            await self.yield_()


@sprite('Sprite5')
class Sprite5(Target):
    """Sprite Sprite5"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 240
        self._ypos = -180
        self._direction = 180
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "929fdf0500d9b12dc32710b7e52193b7.png",
                'center': (16, 16),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_rand = 9



        self.sprite.layer = 5

    @on_green_flag
    async def green_flag(self, util):
        self.shown = True
        self.costume.set_effect('ghost', 100)
        self.gotoxy(0, 0)
        util.sprites.stage.list_endy.hide()
        util.sprites.stage.list_endx.hide()

    @on_broadcast('new level')
    async def broadcast_newlevel(self, util):
        self.gotoxy(tonum(util.sprites.stage.list_endx[toint(util.sprites.stage.var_lvl)]), tonum(util.sprites.stage.list_endy[toint(util.sprites.stage.var_lvl)]))
        if eq(util.sprites.stage.var_lvl, 4):
            self.shown = False

    @on_broadcast('start')
    async def broadcast_START(self, util):
        self.costume.set_effect('ghost', 100)
        self.gotoxy(tonum(util.sprites.stage.list_endx[1]), tonum(util.sprites.stage.list_endy[1]))


@sprite('Sprite6')
class Sprite6(Target):
    """Sprite Sprite6"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "199c9cb3664af07f4ce290bd0f8abb79.svg",
                'center': (295, 256),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 4

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(0, 0)
        self.shown = False

    @on_broadcast('menu')
    async def broadcast_menu(self, util):
        while not not util.inputs.mouse_down:
            await self.yield_()
        self.shown = True
        while not util.inputs.mouse_down:
            await self.yield_()
        self.shown = False
        util.send_broadcast("START")




if __name__ == '__main__':
    engine.start_program()
