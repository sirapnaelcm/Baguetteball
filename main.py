@namespace
class SpriteKind:
    Hoop = SpriteKind.create()

def on_button_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . f f f f f f f . . . . . 
                    . . . f 2 2 2 f 2 2 2 f . . . . 
                    . . f 4 4 4 f f 4 4 4 4 f . . . 
                    . f 5 5 5 5 f 5 5 5 5 5 5 f . . 
                    . f 7 7 7 f f f 7 7 7 7 7 f . . 
                    . f f f f f f f f f f f f f . . 
                    . f 9 9 9 f 9 9 9 9 9 9 9 f . . 
                    . f a a a f a a a a a a a f . . 
                    . f f f f f f f 3 f f f f f . . 
                    . f 2 2 2 2 f 2 f f 2 2 2 f . . 
                    . . f 4 4 4 f f 4 4 4 4 f . . . 
                    . . . f 5 5 5 f f 5 5 f . . . . 
                    . . . . f f f f f f f . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Ghosty,
        0,
        -100)
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_on_overlap(sprite, otherSprite):
    game.over(True)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Hoop, on_on_overlap)

projectile: Sprite = None
Ghosty: Sprite = None
scene.set_background_image(img("""
    4444444441444444444444444444444444444444444444444444444444444111111111111111111111111111111111111114444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444441444444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444444144444444
        4444444444144444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444441444444444
        4444444444144444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444441444444444
        4444444444144444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444441444444444
        4444444444144444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444441444444444
        4444444444144444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444441444444444
        4444444444414444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444414444444444
        4444444444414444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444414444444444
        4444444444414444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444414444444444
        4444444444414444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444414444444444
        4444444444441444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444144444444444
        4444444444441444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444144444444444
        4444444444441444444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444444144444444444
        4444444444444144444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444441444444444444
        4444444444444144444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444441444444444444
        4444444444444144444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444441444444444444
        4444444444444414444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444414444444444444
        4444444444444414444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444414444444444444
        4444444444444441444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444144444444444444
        4444444444444441444444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444444144444444444444
        4444444444444444144444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444441444444444444444
        4444444444444444144444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444441444444444444444
        4444444444444444414444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444414444444444444444
        4444444444444444414444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444414444444444444444
        4444444444444444441444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444144444444444444444
        4444444444444444441444444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444444144444444444444444
        4444444444444444444144444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444441444444444444444444
        4444444444444444444144444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444441444444444444444444
        4444444444444444444414444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444414444444444444444444
        4444444444444444444441444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444144444444444444444444
        4444444444444444444441444444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444444144444444444444444444
        4444444444444444444444144444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444
        4444444444444444444444414444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444414444444444444444444444
        4444444444444444444444441444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444144444444444444444444444
        4444444444444444444444441444444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444444144444444444444444444444
        4444444444444444444444444144444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444441444444444444444444444444
        4444444444444444444444444414444444444444444444444444444444444111111111111111111111111111111111111114444444444444444444444444444444444414444444444444444444444444
        4444444444444444444444444441444444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444444144444444444444444444444444
        4444444444444444444444444444144444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444441444444444444444444444444444
        4444444444444444444444444444414444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444414444444444444444444444444444
        4444444444444444444444444444441444444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444444144444444444444444444444444444
        4444444444444444444444444444444144444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444441444444444444444444444444444444
        4444444444444444444444444444444414444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444414444444444444444444444444444444
        4444444444444444444444444444444441444444444444444444444444444144444444444444444444444444444444444414444444444444444444444444444144444444444444444444444444444444
        4444444444444444444444444444444444144444444444444444444444444144444444444444444444444444444444444414444444444444444444444444441444444444444444444444444444444444
        4444444444444444444444444444444444411444444444444444444444444114444444444444444444444444444444444414444444444444444444444444114444444444444444444444444444444444
        4444444444444444444444444444444444444144444444444444444444444414444444444444444444444444444444444414444444444444444444444441444444444444444444444444444444444444
        4444444444444444444444444444444444444414444444444444444444444414444444444444444444444444444444444414444444444444444444444414444444444444444444444444444444444444
        4444444444444444444444444444444444444441144444444444444444444414444444444444444444444444444444444144444444444444444444441144444444444444444444444444444444444444
        4444444444444444444444444444444444444444414444444444444444444411444444444444444444444444444444444144444444444444444444414444444444444444444444444444444444444444
        4444444444444444444444444444444444444444441144444444444444444441444444444444444444444444444444444144444444444444444441144444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444411444444444444444441144444444444444444444444444444441144444444444444444114444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444114444444444444444144444444444444444444444444444411444444444444444411444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444441144444444444444144444444444444444444444444444414444444444444441144444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444411444444444444114444444444444444444444444444414444444444444114444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444114444444444414444444444444444444444444444144444444444411444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444441114444444411444444444444444444444444441144444444411144444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444441114444441144444444444444444444444441444444411144444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444441111444114444444444444444444444411444111144444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444111111444444444444444444444411111444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444441111111111111111111111144444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444111111111111144444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444411444444444444411444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444441144444444444444444114444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444114444444444444444444441144444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444441444444444444444444444444414444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444414444444444444444444444444441444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444144444444444444444444444444444144444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444441444444444444444444444444444444414444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444144444444444444444444444444444444444144444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444144444444444444444444444444444444444144444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444441444444444444444444444444444444444444414444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444441444444444444444444444444444444444444414444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444414444444444444444444444444444444444444441444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444441444444444444444444444444444444444444414444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444441444444444444444444444444444444444444414444444444444444444444444444444444444444444444444444444444
"""))
Ghosty = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .....ffff111111bf.......
            ....fc111cdb1bdfff......
            ....f1b1bcbfbfc111cf....
            ....fbfbfbffff1b1b1f....
            .........fffffffbfbf....
            ..........fffff.........
            ...........fff..........
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
Ghosty.set_position(80, 100)
Ghosty.set_velocity(50, 0)
Ghosty.set_bounce_on_wall(True)
SupaHoop = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            f f f f f f f f f f f f f f f f 
            f 1 1 1 1 1 1 1 1 1 1 1 1 1 1 f 
            f f f f f f f f f f f f f f f f 
            . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 . 
            . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
            . . . 1 1 1 1 1 1 1 1 1 1 . . . 
            . . . . 1 1 1 1 1 1 1 1 . . . . 
            . . . . . 1 1 1 1 1 1 . . . . . 
            . . . . . . 1 1 1 1 . . . . . . 
            . . . . . . . 1 1 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Hoop)
SupaHoop.set_position(80, 5)